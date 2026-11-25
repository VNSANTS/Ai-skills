#!/usr/bin/env python3
"""Exercise the Codex CLI skill loader in a disposable project without a model request."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]


async def discover(executable: str, project: Path) -> set[str]:
    pkg = project / ".agents" / "skills"
    process = await asyncio.create_subprocess_exec(
        executable, "app-server", "--stdio", "-c", f'projects.{json.dumps(str(project))}.trust_level="trusted"',
        cwd=project, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, limit=8 * 1024 * 1024)
    async def send(packet):
        process.stdin.write((json.dumps(packet) + "\n").encode())
        await process.stdin.drain()

    async def response(request_id):
        while line := await process.stdout.readline():
            packet = json.loads(line)
            if packet.get("id") == request_id:
                if "error" in packet:
                    raise RuntimeError(packet["error"])
                return packet["result"]
        raise RuntimeError("Codex app-server exited before returning skills/list")

    try:
        async with asyncio.timeout(45):
            await send({"id": 1, "method": "initialize", "params": {
                "clientInfo": {"name": "skill-discovery-check", "version": "1.0"}}})
            await response(1)
            await send({"method": "initialized"})
            await send({"id": 2, "method": "skills/list", "params": {
                "cwds": [str(project)], "forceReload": True}})
            result = await response(2)
        names = set()
        for scan in result["data"]:
            if Path(scan["cwd"]).resolve() != project:
                continue
            for error in scan.get("errors", []):
                if Path(error["path"]).is_relative_to(pkg):
                    raise ValueError(f"{error['path']}: {error['message']}")
            for skill in scan["skills"]:
                path = skill.get("path")
                if path and Path(path).is_relative_to(pkg) and skill.get("enabled", True):
                    names.add(skill["name"])
        return names
    finally:
        if process.returncode is None:
            process.terminate()
        try:
            await asyncio.wait_for(process.wait(), 5)
        except TimeoutError:
            process.kill()
            await process.wait()


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--codex", default="codex", help="Codex CLI binary on PATH or its absolute path")
    executable = cli.parse_args().codex
    expected = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
    if not expected:
        raise SystemExit("No skills to test")
    with TemporaryDirectory(prefix="codex-skill-check-") as workspace:
        project = Path(workspace).resolve()
        subprocess.run(["git", "init", "--quiet", str(project)], check=True)
        for name in expected:
            shutil.copytree(ROOT / "skills" / name, project / ".agents" / "skills" / name)
        actual = asyncio.run(discover(executable, project))
        if actual != expected:
            raise SystemExit(f"Missing: {sorted(expected - actual)}; unexpected: {sorted(actual - expected)}")
        print(f"Codex skills/list: {len(actual)} project skills discovered")


if __name__ == "__main__":
    main()
