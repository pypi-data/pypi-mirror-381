#!/bin/bash
# Installation script for Camera Master

echo "======================================"
echo "Camera Master - Installation"
echo "======================================"
echo ""

# Check Python version
python3 --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python is not installed!"
    echo "Please install Python 3.8 or higher"
    exit 1
fi
echo ""

# Upgrade pip
echo "[1/3] Upgrading pip..."
python3 -m pip install --upgrade pip
echo "Done."
echo ""

# Install dependencies
echo "[2/3] Installing dependencies..."
echo "This may take several minutes..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies!"
    exit 1
fi
echo "Done."
echo ""

# Install package
echo "[3/3] Installing Camera Master..."
pip3 install -e .
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install Camera Master!"
    exit 1
fi
echo "Done."
echo ""

# Test installation
echo "======================================"
echo "Testing Installation..."
echo "======================================"
python3 test_installation.py
if [ $? -ne 0 ]; then
    echo ""
    echo "Installation completed with some issues."
    echo "Please check the errors above."
else
    echo ""
    echo "======================================"
    echo "Installation Successful!"
    echo "======================================"
    echo ""
    echo "Camera Master is ready to use!"
    echo ""
    echo "Quick Start:"
    echo "  1. Run: python3 examples/demo_attendance.py"
    echo "  2. Run: camera-master --help"
    echo "  3. Read: QUICKSTART.md"
fi
echo ""
