# PyPI Deployment Guide for Camera Master

## Package Information
- **Package Name:** camera-master
- **Version:** 0.1.0
- **Author:** RNS Sanjay
- **PyPI Username:** sanjay_n

## Deployment Steps

### Step 1: Install Required Tools
```bash
pip install --upgrade build twine
```

### Step 2: Clean Previous Builds
```bash
# Remove old build directories
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
```

### Step 3: Build the Package
```bash
python -m build
```

This creates:
- `dist/camera-master-0.1.0.tar.gz` (source distribution)
- `dist/camera_master-0.1.0-py3-none-any.whl` (wheel distribution)

### Step 4: Check the Build
```bash
twine check dist/*
```

### Step 5: Upload to PyPI (Using API Token)

**IMPORTANT: Set your PyPI token as an environment variable first!**

```powershell
# PowerShell
$env:PYPI_API_TOKEN="your-actual-token-here"

# Or permanently (PowerShell)
[System.Environment]::SetEnvironmentVariable('PYPI_API_TOKEN', 'your-token', 'User')

# CMD
set PYPI_API_TOKEN=your-token-here
```

**Option A: Using API Token (Recommended)**
```bash
twine upload dist/* --username __token__ --password $env:PYPI_API_TOKEN
```

**Option B: Manual Upload**
```bash
# Set token first, then upload
twine upload dist/*
```

### Step 6: Verify Upload
Visit: https://pypi.org/project/camera-master/

### Step 7: Install from PyPI
```bash
pip install camera-master
```

## Troubleshooting

### Error: Package already exists
If you get "File already exists" error:
1. Update version in `setup.py` (e.g., 0.1.0 → 0.1.1)
2. Rebuild: `python -m build`
3. Upload again

### Error: Invalid credentials
- Verify username: `sanjay_n`
- Verify token is correct
- Use `--username __token__` with token (not your username)

### Error: README rendering
Run: `twine check dist/*` to validate README

## Quick Deploy Script

Save this as `deploy.ps1`:

```powershell
# Camera Master Deployment Script

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Camera Master - PyPI Deployment" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan

# Clean old builds
Write-Host "`nCleaning old builds..." -ForegroundColor Yellow
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue

# Build package
Write-Host "`nBuilding package..." -ForegroundColor Yellow
python -m build

# Check build
Write-Host "`nChecking package..." -ForegroundColor Yellow
twine check dist/*

# Upload (requires PYPI_API_TOKEN environment variable)
Write-Host "`nUploading to PyPI..." -ForegroundColor Yellow
Write-Host "Note: Ensure PYPI_API_TOKEN is set in your environment" -ForegroundColor Cyan
twine upload dist/* --username __token__ --password $env:PYPI_API_TOKEN

Write-Host "`n==================================" -ForegroundColor Green
Write-Host "Deployment Complete!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
Write-Host "`nView at: https://pypi.org/project/camera-master/" -ForegroundColor Cyan
```

**Using Environment Variable:**
```powershell
# Set token first
$env:PYPI_API_TOKEN="your-token-here"

# Then run deployment

## After Deployment

### Update README Badge
Add to README.md:
```markdown
[![PyPI version](https://badge.fury.io/py/camera-master.svg)](https://badge.fury.io/py/camera-master)
[![Downloads](https://pepy.tech/badge/camera-master)](https://pepy.tech/project/camera-master)
```

### Announce Release
1. Update GitHub release
2. Tag version: `git tag v0.1.0`
3. Push tag: `git push origin v0.1.0`

## Security Notes

WARNING: **IMPORTANT:** Never commit credentials to Git!
- API tokens are stored in this file for deployment
- Add `PYPI_DEPLOYMENT.md` to `.gitignore`
- Or use environment variables:
 ```bash
 $env:TWINE_USERNAME = "__token__"
 $env:TWINE_PASSWORD = "pypi-AgE..."
 twine upload dist/*
 ```

## Version Updates

When releasing new versions:
1. Update version in `setup.py`
2. Update version in `camera_master/__init__.py`
3. Create changelog entry
4. Build and deploy
5. Tag git commit

Example:
```bash
# Update version to 0.1.1
# Edit setup.py: version="0.1.1"
# Edit __init__.py: __version__ = "0.1.1"

python -m build
twine upload dist/*
git tag v0.1.1
git push origin v0.1.1
```

## Contact
- Email: 2005sanjaynrs@gmail.com
- GitHub: RNSsanjay
- PyPI: https://pypi.org/user/sanjay_n/
