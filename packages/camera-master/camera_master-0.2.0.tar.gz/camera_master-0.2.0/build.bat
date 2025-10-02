@echo off
REM Build script for Camera Master package

echo ======================================
echo Camera Master - Build Script
echo ======================================
echo.

REM Clean previous builds
echo [1/5] Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist camera_master.egg-info rmdir /s /q camera_master.egg-info
echo Done.
echo.

REM Install/upgrade build tools
echo [2/5] Installing build tools...
python -m pip install --upgrade pip setuptools wheel twine --quiet
echo Done.
echo.

REM Build package
echo [3/5] Building package...
python setup.py sdist bdist_wheel
if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)
echo Done.
echo.

REM Check build
echo [4/5] Checking build...
twine check dist/*
if errorlevel 1 (
    echo WARNING: Build check found issues
) else (
    echo Done.
)
echo.

REM Test installation
echo [5/5] Testing installation...
pip install --force-reinstall dist\camera_master-0.1.0-py3-none-any.whl --quiet
python test_installation.py
if errorlevel 1 (
    echo ERROR: Installation test failed!
    pause
    exit /b 1
)
echo.

echo ======================================
echo Build Complete!
echo ======================================
echo.
echo Build artifacts in: dist\
echo   - camera-master-0.1.0.tar.gz
echo   - camera_master-0.1.0-py3-none-any.whl
echo.
echo To install locally:
echo   pip install dist\camera_master-0.1.0-py3-none-any.whl
echo.
echo To upload to Test PyPI:
echo   twine upload --repository testpypi dist/*
echo.
echo To upload to PyPI:
echo   twine upload dist/*
echo.

pause
