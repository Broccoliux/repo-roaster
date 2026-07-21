$ErrorActionPreference = 'Stop'

$python = "f:/OneDrive/Desktop/cloned repos/repo-roaster/venv/Scripts/python.exe"

if (-not (Test-Path $python)) {
    Write-Error "Python environment not found at $python"
    exit 1
}

& $python -m pip show wakatime | Out-Null
if ($LASTEXITCODE -ne 0) {
    & $python -m pip install wakatime
}

& $python -c "import wakatime; print('WakaTime ready')"
