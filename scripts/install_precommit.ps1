# Install and enable pre-commit hooks (PowerShell)
Set-Location -Path (Join-Path $PSScriptRoot "..")

if (Get-Command poetry -ErrorAction SilentlyContinue) {
  Write-Output "Installing pre-commit in Poetry environment..."
  poetry add --dev pre-commit -n
  poetry run pre-commit install
  Write-Output "Pre-commit installed via Poetry and hooks registered."
} else {
  Write-Output "Installing pre-commit globally (recommended to use virtualenv or Poetry)..."
  python -m pip install --upgrade pip
  python -m pip install pre-commit
  pre-commit install
  Write-Output "Pre-commit installed and hooks registered."
}
