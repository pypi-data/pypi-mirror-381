# PyPI Publishing Guide for Drudge CLI

## 📦 Package Files Created

✅ **pyproject.toml** - Modern Python package configuration (PEP 621)
✅ **setup.py** - Backward compatibility wrapper
✅ **MANIFEST.in** - Package data inclusion rules
✅ **LICENSE** - MIT License for open source distribution

## 🚀 Step-by-Step Publishing Process

### Step 1: Install Build Tools

```bash
# Install required build tools
pip install --upgrade build twine
```

### Step 2: Build the Package

```bash
# Clean any previous builds
rm -rf dist/ build/ src/*.egg-info

# Build source distribution and wheel
python -m build

# This creates:
# - dist/drudge-cli-2.0.0.tar.gz (source distribution)
# - dist/drudge_cli-2.0.0-py3-none-any.whl (wheel)
```

### Step 3: Test the Package Locally

```bash
# Create a test virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from the built wheel
pip install dist/drudge_cli-2.0.0-py3-none-any.whl

# Test the installation
drudge --help
drudge version

# Deactivate and remove test environment
deactivate
rm -rf test_env
```

### Step 4: Create PyPI Account

1. Go to https://pypi.org/account/register/
2. Register a new account
3. Verify your email address

### Step 5: Create API Token

1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name: "drudge-cli-upload"
4. Scope: "Entire account" (or specific project after first upload)
5. Copy the token (starts with `pypi-...`)
6. **Save it securely** - you can only see it once!

### Step 6: Configure PyPI Credentials

Create `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE
repository = https://test.pypi.org/legacy/
```

**Security Note**: Keep this file private! Add to `.gitignore` if in project.

### Step 7: Upload to TestPyPI (Recommended First)

```bash
# Upload to TestPyPI first to verify
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ drudge-cli
```

### Step 8: Upload to PyPI (Production)

```bash
# Upload to real PyPI
twine upload dist/*

# Or with explicit credentials
twine upload -u __token__ -p pypi-YOUR_TOKEN_HERE dist/*
```

### Step 9: Verify Publication

1. Visit: https://pypi.org/project/drudge-cli/
2. Check that all information displays correctly
3. Test installation:

```bash
pip install drudge-cli
drudge --help
```

### Step 10: Create Git Tag and GitHub Release

```bash
# Tag the release
git tag -a v2.0.0 -m "🚀 Release v2.0.0 - First PyPI Publication

Features:
- Professional Python package structure
- Available on PyPI: pip install drudge-cli
- Comprehensive task management
- Rich CLI interface
- Automatic backups
- Daily summaries and reports"

# Push the tag
git push origin v2.0.0
```

Then create a GitHub Release:
1. Go to https://github.com/Trik16/drudge/releases/new
2. Select tag: v2.0.0
3. Release title: "🚀 Drudge CLI v2.0.0 - PyPI Release"
4. Copy the tag message as description
5. Attach dist files (optional)
6. Click "Publish release"

## 🔄 For Future Updates

### Version Update Checklist

1. **Update version** in `pyproject.toml`
2. **Update version** in `src/worklog/__init__.py`
3. **Update CHANGELOG** (if you have one)
4. **Run tests**: `pytest`
5. **Build**: `python -m build`
6. **Upload**: `twine upload dist/*`
7. **Tag release**: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
8. **Push tag**: `git push origin vX.Y.Z`
9. **Create GitHub Release**

### Semantic Versioning

- **MAJOR** (X.0.0): Breaking changes
- **MINOR** (2.X.0): New features, backward compatible
- **PATCH** (2.0.X): Bug fixes, backward compatible

## ⚠️ Important Notes

### Before Publishing

- [ ] Update email in `pyproject.toml` (currently placeholder)
- [ ] Verify all dependencies are correct in `pyproject.toml`
- [ ] Test package installation in clean environment
- [ ] Check README renders correctly on PyPI
- [ ] Verify LICENSE file is included
- [ ] Run all tests successfully
- [ ] Update version number if needed

### Package Name

- **PyPI Package**: `drudge-cli`
- **Import Name**: `worklog`
- **Command**: `drudge` or `worklog`

This is intentional - users install `pip install drudge-cli` but import as `from worklog import ...`

### Common Issues

**Issue**: Package name already taken
**Solution**: PyPI names are first-come-first-served. Choose a unique name.

**Issue**: Twine upload fails with 403
**Solution**: Check your API token is correct and has the right scope.

**Issue**: README doesn't render on PyPI
**Solution**: Ensure README.md is in Markdown format and referenced in pyproject.toml

**Issue**: Missing files in package
**Solution**: Check MANIFEST.in includes all necessary files

## 📊 Post-Publication

### Update README

Add installation section:
```markdown
## Installation

```bash
pip install drudge-cli
```

Add PyPI badge:
```markdown
[![PyPI version](https://img.shields.io/pypi/v/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
```

### Monitor

- PyPI download stats: https://pypistats.org/packages/drudge-cli
- GitHub stars and issues
- User feedback and bug reports

## 🎯 Quick Reference

```bash
# One-time setup
pip install build twine

# Build and publish workflow
rm -rf dist/ build/ *.egg-info
python -m build
twine check dist/*
twine upload dist/*

# Test in clean environment
python -m venv test_env && source test_env/bin/activate
pip install drudge-cli
drudge --help
deactivate && rm -rf test_env
```

## 🔗 Useful Links

- PyPI Project Page: https://pypi.org/project/drudge-cli/
- PyPI User Guide: https://packaging.python.org/tutorials/packaging-projects/
- Twine Documentation: https://twine.readthedocs.io/
- PyPI Classifiers: https://pypi.org/classifiers/
