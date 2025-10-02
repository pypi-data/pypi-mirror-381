@echo off
REM Installation script for Camera Master

echo ======================================
echo Camera Master - Installation
echo ======================================
echo.

REM Check Python version
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)
echo.

REM Upgrade pip
echo [1/3] Upgrading pip...
python -m pip install --upgrade pip
echo Done.
echo.

REM Install dependencies
echo [2/3] Installing dependencies...
echo This may take several minutes...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)
echo Done.
echo.

REM Install package
echo [3/3] Installing Camera Master...
pip install -e .
if errorlevel 1 (
    echo ERROR: Failed to install Camera Master!
    pause
    exit /b 1
)
echo Done.
echo.

REM Test installation
echo ======================================
echo Testing Installation...
echo ======================================
python test_installation.py
if errorlevel 1 (
    echo.
    echo Installation completed with some issues.
    echo Please check the errors above.
) else (
    echo.
    echo ======================================
    echo Installation Successful!
    echo ======================================
    echo.
    echo Camera Master is ready to use!
    echo.
    echo Quick Start:
    echo   1. Run: python examples\demo_attendance.py
    echo   2. Run: camera-master --help
    echo   3. Read: QUICKSTART.md
)
echo.

pause
