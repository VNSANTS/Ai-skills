# Imports all tracked files from a GitHub repository into repositories/<name>.
# Does not execute scripts from the source; does not preserve full Git history.
[CmdletBinding()]
param(
    [string]$Source = 'https://github.com/ctresb/leis.git',
    [string]$Branch = 'main',
    [string]$Destination = 'repositories/leis'
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = (& git rev-parse --show-toplevel 2>&1 | Select-Object -First 1).Trim()
if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $root)) {
    throw 'Run from inside a Git clone of VNSANTS/Ai-skills.'
}
if ($Destination -notmatch '^repositories/[a-zA-Z0-9._/-]+$' -or $Destination -match '(^|/)\.\.(/|$)') {
    throw 'Unsafe destination; choose a path inside repositories/.'
}
$target = Join-Path $root ($Destination -replace '/', [IO.Path]::DirectorySeparatorChar)
if (Test-Path -LiteralPath $target) {
    throw "Destination already exists: $target. Nothing was overwritten."
}
$clone = Join-Path ([IO.Path]::GetTempPath()) ("nexus-repo-copy-" + [guid]::NewGuid().ToString('N'))
try {
    Write-Host 'Cloning the full tracked-file snapshot, without the complete history...'
    & git -c core.longpaths=true clone --depth 1 --single-branch --branch $Branch -- $Source $clone
    if ($LASTEXITCODE -ne 0) { throw 'Clone failed. Nothing imported.' }
    $commit = (& git -C $clone rev-parse HEAD).Trim()
    if ($LASTEXITCODE -ne 0) { throw 'Failed to read source commit.' }
    $tracked = @(& git -c core.quotePath=false -C $clone ls-files)
    if ($LASTEXITCODE -ne 0) { throw 'Failed to enumerate source files.' }
    $submodules = @(& git -C $clone ls-files --stage | Where-Object { $_ -match '^160000 ' })
    if ($submodules.Count -gt 0) {
        throw 'Source has submodules: these must be archived separately before claiming full coverage.'
    }
    New-Item -ItemType Directory -Path $target -Force | Out-Null
    & robocopy.exe $clone $target /E /XD (Join-Path $clone '.git') /COPY:DAT /DCOPY:DAT /R:1 /W:1 /MT:8 /NFL /NDL /NJH /NJS
    if ($LASTEXITCODE -ge 8) { throw "Copy failed (robocopy exit code $LASTEXITCODE)." }
    $missing = 0
    foreach ($relative in $tracked) {
        $path = Join-Path $target ($relative -replace '/', [IO.Path]::DirectorySeparatorChar)
        if (-not (Test-Path -LiteralPath $path)) { $missing++ }
    }
    if ($missing -gt 0) { throw "$missing files missing. Do not commit this incomplete snapshot." }
    $record = @"
# External source snapshot

Source: $Source
Branch: $Branch
Source commit: $commit
Tracked files copied: $($tracked.Count)

Independent copy of tracked working-tree files, NOT a full Git history mirror.
Confirm whether the original repository uses Git LFS and verify any LFS objects.
"@
    Set-Content -LiteralPath (Join-Path $target 'NEXUS_BACKUP_MANIFEST.md') -Value $record -Encoding utf8
    Write-Host "Copied $($tracked.Count) tracked files into $Destination at source commit $commit."
    Write-Host "Review file limits, then use: git add -- $Destination"
    Write-Host 'No source code was executed. Nothing was committed or pushed.'
}
finally {
    if (Test-Path -LiteralPath $clone) { Remove-Item -LiteralPath $clone -Recurse -Force }
}
