# Import a tracked-file snapshot into repositories/<name> from inside the receiving Git clone.
[CmdletBinding()]
param(
    [ValidateNotNullOrEmpty()][string]$Source = 'https://github.com/ctresb/leis.git',
    [ValidateNotNullOrEmpty()][string]$Branch = 'main',
    [ValidateNotNullOrEmpty()][string]$Destination = 'repositories/leis',
    [switch]$Stage
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([IO.Path]::DirectorySeparatorChar -eq '\') {
    # Use Git for Windows' own Bash. A bash.exe on the user's PATH can launch WSL instead.
    $execPath = & git --exec-path
    if ($LASTEXITCODE -ne 0) { throw 'Git for Windows with Git Bash is required.' }
    $directory = [IO.DirectoryInfo]::new($execPath)
    $bash = $null
    while ($directory -and -not $bash) {
        foreach ($relative in @('bin\bash.exe', 'usr\bin\bash.exe')) {
            $candidate = Join-Path $directory.FullName $relative
            if ([IO.File]::Exists($candidate)) {
                $bash = $candidate
                break
            }
        }
        $directory = $directory.Parent
    }
    if (-not $bash) { throw 'Could not find the Bash included with Git for Windows.' }

    # Windows can also redirect paths through junctions or other reparse points.
    $root = & git rev-parse --show-toplevel
    if ($LASTEXITCODE -ne 0) { throw 'Run from inside the receiving Git clone.' }
    if ($Destination -match '^repositories(?:/[a-zA-Z0-9._-]+)+/?$') {
        $path = [string]$root
        foreach ($part in $Destination.TrimEnd('/').Split('/')) {
            if ($part.EndsWith('.')) { break }
            $path = Join-Path $path $part
            $item = Get-Item -LiteralPath $path -Force -ErrorAction SilentlyContinue
            if ($null -eq $item) { break }
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw "Destination crosses a filesystem link: $path"
            }
        }
    }
} else {
    $bash = (Get-Command bash -CommandType Application | Select-Object -First 1).Source
}

$scriptPath = (Join-Path $PSScriptRoot 'import-repository-snapshot.sh').Replace('\', '/')
$arguments = @($scriptPath, $Source, $Branch, $Destination)
if ($Stage) { $arguments += '--stage' }
& $bash @arguments
if ($LASTEXITCODE -ne 0) { throw "Snapshot import failed (exit code $LASTEXITCODE)." }
