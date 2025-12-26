<#
Builds a single-file Windows executable using PyInstaller.
Usage:
  - From project root: .\scripts\build_exe.ps1
  - Or specify name: .\scripts\build_exe.ps1 -Name my-app
#>
param(
  [string]$Name = "mouse-recorder",
  [string]$Spec = "src/mouse_recorder/cli.py"
)

# Change to project root (script location is scripts/)
Set-Location -Path (Join-Path $PSScriptRoot "..")

if (Get-Command poetry -ErrorAction SilentlyContinue) {
  Write-Output "Using Poetry environment to run PyInstaller..."
  poetry run pyinstaller --onefile --name $Name $Spec
} else {
  Write-Output "Running PyInstaller directly (make sure pyinstaller is installed)..."
  pyinstaller --onefile --name $Name $Spec
}

Write-Output "Build finished. Artifact should be in the 'dist' directory."