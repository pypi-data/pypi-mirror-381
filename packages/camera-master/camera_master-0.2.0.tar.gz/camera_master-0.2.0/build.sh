#!/bin/bash
# Build script for Camera Master package

echo "======================================"
echo "Camera Master - Build Script"
echo "======================================"
echo ""

# Clean previous builds
echo "[1/5] Cleaning previous builds..."
rm -rf build dist *.egg-info
echo "Done."
echo ""

# Install/upgrade build tools
echo "[2/5] Installing build tools..."
python -m pip install --upgrade pip setuptools wheel twine --quiet
echo "Done."
echo ""

# Build package
echo "[3/5] Building package..."
python setup.py sdist bdist_wheel
if [ $? -ne 0 ]; then
    echo "ERROR: Build failed!"
    exit 1
fi
echo "Done."
echo ""

# Check build
echo "[4/5] Checking build..."
twine check dist/*
if [ $? -ne 0 ]; then
    echo "WARNING: Build check found issues"
else
    echo "Done."
fi
echo ""

# Test installation
echo "[5/5] Testing installation..."
pip install --force-reinstall dist/camera_master-0.1.0-py3-none-any.whl --quiet
python test_installation.py
if [ $? -ne 0 ]; then
    echo "ERROR: Installation test failed!"
    exit 1
fi
echo ""

echo "======================================"
echo "Build Complete!"
echo "======================================"
echo ""
echo "Build artifacts in: dist/"
echo "  - camera-master-0.1.0.tar.gz"
echo "  - camera_master-0.1.0-py3-none-any.whl"
echo ""
echo "To install locally:"
echo "  pip install dist/camera_master-0.1.0-py3-none-any.whl"
echo ""
echo "To upload to Test PyPI:"
echo "  twine upload --repository testpypi dist/*"
echo ""
echo "To upload to PyPI:"
echo "  twine upload dist/*"
echo ""
