# GitHub Badges Reference for Drudge CLI

## 📌 Current Badges in README

The README now includes these badges:

```markdown
[![GitHub](https://img.shields.io/badge/GitHub-Trik16%2Fdrudge-blue?logo=github)](https://github.com/Trik16/drudge)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Typer](https://img.shields.io/badge/CLI-Typer-green.svg)](https://typer.tiangolo.com/)
```

## 🎯 Additional Badges (Add After PyPI Publishing)

### PyPI Badges

Once you publish to PyPI, add these:

```markdown
[![PyPI version](https://img.shields.io/pypi/v/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
[![PyPI downloads](https://img.shields.io/pypi/dm/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
[![PyPI status](https://img.shields.io/pypi/status/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
```

### GitHub Dynamic Badges

These show real-time GitHub stats:

```markdown
[![GitHub stars](https://img.shields.io/github/stars/Trik16/drudge?style=social)](https://github.com/Trik16/drudge/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Trik16/drudge?style=social)](https://github.com/Trik16/drudge/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Trik16/drudge)](https://github.com/Trik16/drudge/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Trik16/drudge)](https://github.com/Trik16/drudge/pulls)
[![GitHub last commit](https://img.shields.io/github/last-commit/Trik16/drudge)](https://github.com/Trik16/drudge/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Trik16/drudge)](https://github.com/Trik16/drudge)
```

### CI/CD Badges (Add After Setting Up GitHub Actions)

```markdown
[![Tests](https://github.com/Trik16/drudge/actions/workflows/tests.yml/badge.svg)](https://github.com/Trik16/drudge/actions/workflows/tests.yml)
[![Build](https://github.com/Trik16/drudge/actions/workflows/build.yml/badge.svg)](https://github.com/Trik16/drudge/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/Trik16/drudge/branch/main/graph/badge.svg)](https://codecov.io/gh/Trik16/drudge)
```

### Quality & Security Badges

```markdown
[![Code Quality](https://img.shields.io/codefactor/grade/github/Trik16/drudge)](https://www.codefactor.io/repository/github/Trik16/drudge)
[![Maintainability](https://api.codeclimate.com/v1/badges/YOUR_TOKEN/maintainability)](https://codeclimate.com/github/Trik16/drudge/maintainability)
```

## 🎨 Badge Styles

Shields.io supports different styles:

- **Flat** (default): `?style=flat`
- **Flat Square**: `?style=flat-square`
- **Plastic**: `?style=plastic`
- **For the Badge**: `?style=for-the-badge`
- **Social**: `?style=social` (for stars/forks)

Example:
```markdown
[![GitHub stars](https://img.shields.io/github/stars/Trik16/drudge?style=for-the-badge)](https://github.com/Trik16/drudge/stargazers)
```

## 🔧 Customizing Badges

### Custom Colors

Use color names or hex codes:
```markdown
![Custom](https://img.shields.io/badge/custom-badge-ff69b4)
![Custom Hex](https://img.shields.io/badge/custom-badge-ff69b4?logo=python)
```

### With Logos

Add logos from [Simple Icons](https://simpleicons.org/):
```markdown
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)
```

## 📋 Recommended Badge Order

1. **Project Status/Build** - CI/CD badges
2. **Version** - PyPI version badge
3. **Platform/Language** - Python version
4. **Quality** - Code coverage, quality scores
5. **Downloads** - PyPI downloads
6. **License** - License type
7. **Tools/Frameworks** - Typer, Rich, etc.
8. **Social** - Stars, forks (at the bottom or side)

## 🚀 Full Example for After PyPI Publishing

```markdown
# Drudge CLI Tool

[![PyPI version](https://img.shields.io/pypi/v/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI downloads](https://img.shields.io/pypi/dm/drudge-cli.svg)](https://pypi.org/project/drudge-cli/)
[![Tests](https://github.com/Trik16/drudge/actions/workflows/tests.yml/badge.svg)](https://github.com/Trik16/drudge/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Typer](https://img.shields.io/badge/CLI-Typer-green.svg)](https://typer.tiangolo.com/)
[![GitHub stars](https://img.shields.io/github/stars/Trik16/drudge?style=social)](https://github.com/Trik16/drudge/stargazers)
```

## 🔗 Useful Resources

- **Shields.io**: https://shields.io/ - Main badge service
- **Simple Icons**: https://simpleicons.org/ - Logo collection
- **Badge Generator**: https://badgen.net/ - Alternative badge service
- **GitHub Badge Guide**: https://github.com/badges/shields

## 💡 Tips

1. **Don't overdo it**: 5-8 badges is usually enough
2. **Keep them updated**: Remove badges for discontinued services
3. **Use meaningful badges**: Show actual project stats, not vanity metrics
4. **Align properly**: Use HTML tables if you need specific alignment
5. **Test the links**: Make sure all badges link to the correct pages

## 📝 Note

The current badges are static placeholders. Once you:
- Publish to PyPI → Add PyPI badges
- Set up GitHub Actions → Add CI/CD badges
- Set up code coverage → Add Codecov badge
- Get community engagement → Add social badges (stars, forks)
