# Build and Installation Guide for Camera Master

## For Developers

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/RNSsanjay/camera-master.git
   cd camera-master
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   ```

4. **Install development dependencies**
   ```bash
   pip install pytest pytest-cov black flake8 mypy
   ```

### Building the Package

#### Build wheel and source distribution
```bash
python setup.py sdist bdist_wheel
```

This creates:
- `dist/camera-master-0.1.0.tar.gz` (source distribution)
- `dist/camera_master-0.1.0-py3-none-any.whl` (wheel)

#### Check the build
```bash
pip install twine
twine check dist/*
```

### Testing the Build

#### Install from local build
```bash
pip install dist/camera_master-0.1.0-py3-none-any.whl
```

#### Run tests
```bash
python test_installation.py
```

#### Run examples
```bash
python examples/demo_attendance.py
```

## For End Users

### Quick Installation

```bash
# Install from local directory
cd camera-master
pip install -e .
```

### Installation from PyPI (once published)

```bash
pip install camera-master
```

### Verify Installation

```bash
# Check version
python -c "import camera_master; print(camera_master.__version__)"

# Run installation test
python test_installation.py

# Test CLI
camera-master --help
```

## Publishing to PyPI

### Prerequisites

1. Create accounts on:
   - [Test PyPI](https://test.pypi.org/account/register/)
   - [PyPI](https://pypi.org/account/register/)

2. Create API tokens for both platforms

3. Configure `.pypirc`:
   ```ini
   [distutils]
   index-servers =
       pypi
       testpypi

   [pypi]
   username = __token__
   password = <your-pypi-token>

   [testpypi]
   username = __token__
   password = <your-test-pypi-token>
   ```

### Build for Release

1. **Update version** in `setup.py` and `pyproject.toml`

2. **Clean previous builds**
   ```bash
   rm -rf build dist *.egg-info
   ```

3. **Build package**
   ```bash
   python setup.py sdist bdist_wheel
   ```

4. **Check package**
   ```bash
   twine check dist/*
   ```

### Upload to Test PyPI (recommended first)

```bash
twine upload --repository testpypi dist/*
```

Test installation:
```bash
pip install --index-url https://test.pypi.org/simple/ camera-master
```

### Upload to PyPI

```bash
twine upload dist/*
```

## Package Structure

```
camera-master/
├── camera_master/              # Main package
│   ├── __init__.py            # Package initialization
│   ├── attendance.py          # Face recognition attendance
│   ├── gesture.py             # Gesture recognition
│   ├── emotion.py             # Emotion analysis
│   ├── visualization.py       # Data visualization
│   ├── reports.py             # Report generation
│   ├── utils.py               # Utility functions
│   ├── attention.py           # Attention tracking
│   ├── mask_detection.py      # Mask detection
│   ├── age_gender.py          # Age/gender estimation
│   ├── fatigue.py             # Fatigue detection
│   ├── spoof.py               # Spoof detection
│   ├── mood_tracker.py        # Mood tracking
│   ├── access_control.py      # Access control
│   ├── gamification.py        # Gamification engine
│   └── cli.py                 # Command-line interface
├── examples/                   # Example scripts
│   ├── demo_attendance.py
│   ├── demo_emotion.py
│   ├── demo_comprehensive.py
│   └── demo_gesture_interaction.py
├── setup.py                   # Setup configuration
├── pyproject.toml             # Modern Python project config
├── requirements.txt           # Dependencies
├── README.md                  # Main documentation
├── QUICKSTART.md              # Quick start guide
├── LICENSE                    # MIT License
├── MANIFEST.in                # Package manifest
├── .gitignore                 # Git ignore rules
└── test_installation.py       # Installation test
```

## Version Management

### Semantic Versioning

- **MAJOR**: Breaking changes (1.0.0)
- **MINOR**: New features, backward compatible (0.1.0)
- **PATCH**: Bug fixes (0.1.1)

### Release Checklist

- [ ] Update version in `setup.py`
- [ ] Update version in `pyproject.toml`
- [ ] Update version in `camera_master/__init__.py`
- [ ] Update CHANGELOG.md
- [ ] Run all tests
- [ ] Update documentation
- [ ] Build package
- [ ] Test on Test PyPI
- [ ] Upload to PyPI
- [ ] Create GitHub release
- [ ] Tag release in git

## Troubleshooting Build Issues

### Issue: "No module named 'setuptools'"
```bash
pip install --upgrade setuptools wheel
```

### Issue: "error: invalid command 'bdist_wheel'"
```bash
pip install wheel
```

### Issue: Build fails due to C extensions
- This package is pure Python, no C extensions needed
- If you see this error, check your dependencies

### Issue: Import errors after installation
```bash
# Reinstall in development mode
pip install -e .

# Or force reinstall
pip install --force-reinstall -e .
```

## Development Workflow

1. **Make changes** to code
2. **Test locally**:
   ```bash
   python test_installation.py
   python examples/demo_attendance.py
   ```
3. **Run linters**:
   ```bash
   black camera_master/
   flake8 camera_master/
   ```
4. **Update version** if needed
5. **Commit changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
6. **Build and test**:
   ```bash
   python setup.py sdist bdist_wheel
   pip install dist/camera_master-0.1.0-py3-none-any.whl
   ```
7. **Push to repository**:
   ```bash
   git push origin main
   ```

## Continuous Integration

### GitHub Actions Example

Create `.github/workflows/test.yml`:

```yaml
name: Test Package

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', 3.11]
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Test installation
      run: python test_installation.py
```

## Distribution Checklist

Before distributing to users:

- [ ] All tests pass
- [ ] Examples work correctly
- [ ] Documentation is complete
- [ ] README is up to date
- [ ] License is included
- [ ] Dependencies are specified correctly
- [ ] CLI commands work
- [ ] Package installs cleanly
- [ ] No hardcoded paths
- [ ] Compatible with target Python versions

## Support

For build and installation issues:
- Check the troubleshooting sections
- Run `python test_installation.py`
- Open an issue on GitHub
- Contact maintainers

---

Last updated: 2025
