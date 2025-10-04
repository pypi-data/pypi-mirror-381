# 🚀 PyPI Release Checklist for Drudge CLI

## ✅ Completed Steps (Automated)

- [x] **Created pyproject.toml** - Complete package metadata with dependencies
- [x] **Created setup.py** - Backward compatibility wrapper  
- [x] **Created MANIFEST.in** - Package data inclusion rules
- [x] **Created LICENSE** - MIT License
- [x] **Built package locally** - Successfully created dist files
- [x] **Created documentation** - Comprehensive PYPI_PUBLISHING.md guide

## 📦 Package Information

- **Package Name (PyPI)**: `drudge-cli`
- **Import Name**: `worklog`
- **Commands**: `drudge`, `worklog`
- **Version**: 2.0.0
- **License**: MIT
- **Python**: 3.8+

## 📁 Files Ready for Distribution

```
dist/
├── drudge-2.0.0-py3-none-any.whl    (30 KB) - Wheel distribution
└── drudge-2.0.0.tar.gz              (41 KB) - Source distribution
```

## 🎯 Manual Steps Required (YOU DO THESE)

### Step 1: Install Twine

```bash
pip install twine
```

### Step 2: Verify Package

```bash
# Check the package for errors
twine check dist/*
```

### Step 3: Create PyPI Account

1. Go to https://pypi.org/account/register/
2. Register and verify email
3. Login to your account

### Step 4: Create API Token

1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name: "drudge-cli"
4. Scope: "Entire account"
5. **Copy the token** (starts with `pypi-...`)
6. Save it securely!

### Step 5: Test on TestPyPI (RECOMMENDED)

```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# When prompted:
# Username: __token__
# Password: pypi-YOUR_TOKEN_HERE

# Test installation
pip install --index-url https://test.pypi.org/simple/ drudge-cli
drudge --help
```

### Step 6: Upload to PyPI (PRODUCTION)

```bash
# Upload to real PyPI
twine upload dist/*

# When prompted:
# Username: __token__
# Password: pypi-YOUR_PRODUCTION_TOKEN
```

### Step 7: Verify Publication

```bash
# Install from PyPI
pip install drudge-cli

# Test it works
drudge --help
drudge version
```

### Step 8: Create GitHub Release

```bash
# Tag the release
git tag -a v2.0.0 -m "🚀 Release v2.0.0 - First PyPI Publication"

# Push the tag
git push origin v2.0.0
```

Then on GitHub:
1. Go to https://github.com/Trik16/drudge/releases/new
2. Select tag: v2.0.0
3. Title: "🚀 Drudge CLI v2.0.0 - PyPI Release"
4. Add release notes
5. Publish release

### Step 9: Update README

Add installation instructions:
```markdown
## Installation

Install via pip:
```bash
pip install drudge-cli
```

Then use:
```bash
drudge start "My Task"
drudge status
```

## ⚠️ Before Publishing - IMPORTANT!

1. **Update your email** in `pyproject.toml` (currently placeholder)
2. **Test in clean environment** - Make sure package works
3. **Run tests** - All tests should pass
4. **Check README** - Make sure it looks good on PyPI

### Update Email

Edit `pyproject.toml` line 11:
```toml
authors = [
    { name = "Trik16", email = "your.actual@email.com" }  # ← Change this!
]
```

Then rebuild:
```bash
rm -rf dist/ build/ src/*.egg-info
python3 -m build
```

## 🔗 Quick Reference

```bash
# Full workflow:
pip install build twine
rm -rf dist/ build/ src/*.egg-info
python3 -m build
twine check dist/*
twine upload dist/*  # Enter token when prompted
pip install drudge-cli
drudge --help
git tag -a v2.0.0 -m "Release v2.0.0"
git push origin v2.0.0
```

## 📚 Documentation

- Full guide: `docs/PYPI_PUBLISHING.md`
- Badge reference: `docs/BADGES_REFERENCE.md`
- GitHub setup: `docs/GITHUB_SETUP.md`

## 🎉 After Publishing

Once published, add PyPI badges to README:

```markdown
[![PyPI version](https://img.shields.io/pypi/v/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
[![PyPI downloads](https://img.shields.io/pypi/dm/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
```

Your package will be available at:
- **PyPI**: https://pypi.org/project/drudge-cli/
- **Install**: `pip install drudge-cli`
- **Import**: `from worklog import ...`
- **Commands**: `drudge` or `worklog`

## 🆘 Need Help?

Check the comprehensive guide in `docs/PYPI_PUBLISHING.md` for:
- Detailed step-by-step instructions
- Troubleshooting common issues
- TestPyPI testing procedure
- Version update workflow
- And much more!

---

**You're ready to publish! 🚀**

Just follow the manual steps above and Drudge CLI will be live on PyPI!
