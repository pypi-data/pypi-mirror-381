# Camera Master Deployment Script
# Deploys to PyPI using twine

Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host " Camera Master - PyPI Deployment" -ForegroundColor Cyan
Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Clean old builds
Write-Host "[1/6] Cleaning old builds..." -ForegroundColor Yellow
Remove-Item -Recurse -Force dist, build -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Filter "*.egg-info" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Write-Host " Old builds cleaned!" -ForegroundColor Green
Write-Host ""

# Step 2: Install/upgrade build tools
Write-Host "[2/6] Checking build tools..." -ForegroundColor Yellow
pip install --upgrade build twine --quiet
Write-Host " Build tools ready!" -ForegroundColor Green
Write-Host ""

# Step 3: Build the package
Write-Host "[3/6] Building package..." -ForegroundColor Yellow
python -m build
if ($LASTEXITCODE -eq 0) {
 Write-Host " Package built successfully!" -ForegroundColor Green
} else {
 Write-Host " Build failed!" -ForegroundColor Red
 exit 1
}
Write-Host ""

# Step 4: Check the package
Write-Host "[4/6] Validating package..." -ForegroundColor Yellow
twine check dist/*
if ($LASTEXITCODE -eq 0) {
 Write-Host " Package validation passed!" -ForegroundColor Green
} else {
 Write-Host " Validation failed!" -ForegroundColor Red
 exit 1
}
Write-Host ""

# Step 5: Display package info
Write-Host "[5/6] Package Information:" -ForegroundColor Yellow
Get-ChildItem dist/ | ForEach-Object {
 Write-Host " - $($_.Name)" -ForegroundColor Cyan
}
Write-Host ""

# Step 6: Upload to PyPI
Write-Host "[6/6] Uploading to PyPI..." -ForegroundColor Yellow
Write-Host " Using API token for authentication..." -ForegroundColor Cyan

# Load token from environment variable
$token = $env:PYPI_API_TOKEN

if (-not $token) {
    Write-Host ""
    Write-Host "ERROR: PYPI_API_TOKEN environment variable not set!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please set your PyPI token first:" -ForegroundColor Yellow
    Write-Host "  PowerShell: `$env:PYPI_API_TOKEN='your-token-here'" -ForegroundColor Cyan
    Write-Host "  CMD: set PYPI_API_TOKEN=your-token-here" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Or create a .env file with PYPI_API_TOKEN=your-token" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

$username = if ($env:PYPI_USERNAME) { $env:PYPI_USERNAME } else { "__token__" }

twine upload dist/* --username $username --password $token

if ($LASTEXITCODE -eq 0) {
 Write-Host ""
 Write-Host "===========================================================" -ForegroundColor Green
 Write-Host " DEPLOYMENT SUCCESSFUL!" -ForegroundColor Green
 Write-Host "===========================================================" -ForegroundColor Green
 Write-Host ""
 Write-Host " Package: camera-master v0.1.0" -ForegroundColor Cyan
 Write-Host " Author: RNS Sanjay" -ForegroundColor Cyan
 Write-Host " PyPI: https://pypi.org/project/camera-master/" -ForegroundColor Cyan
 Write-Host ""
 Write-Host "Install with:" -ForegroundColor Yellow
 Write-Host " pip install camera-master" -ForegroundColor White
 Write-Host ""
 Write-Host "View your package:" -ForegroundColor Yellow
 Write-Host " https://pypi.org/project/camera-master/" -ForegroundColor White
 Write-Host ""
} else {
 Write-Host ""
 Write-Host "===========================================================" -ForegroundColor Red
 Write-Host " DEPLOYMENT FAILED!" -ForegroundColor Red
 Write-Host "===========================================================" -ForegroundColor Red
 Write-Host ""
 Write-Host "Common issues:" -ForegroundColor Yellow
 Write-Host " 1. Package name already exists - update version in setup.py" -ForegroundColor White
 Write-Host " 2. Invalid credentials - check token" -ForegroundColor White
 Write-Host " 3. Network issues - check internet connection" -ForegroundColor White
 Write-Host ""
 Write-Host "See PYPI_DEPLOYMENT.md for troubleshooting" -ForegroundColor Cyan
 Write-Host ""
 exit 1
}
