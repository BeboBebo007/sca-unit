$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$pythonPath = ".\.venv\Scripts\python.exe"
$envPath = ".\.env.local"
$url = "http://127.0.0.1:8765"
if (-not (Test-Path $pythonPath)) { throw "Python virtual environment was not found." }
if (-not (Test-Path $envPath)) { throw "Local environment file was not found." }
Write-Host "Starting SCA-Unit local demo..."
Write-Host "Web interface: $url"
Write-Host "Press Ctrl+C to stop the service."
Start-Process $url
& $pythonPath -m private_server.start_local
