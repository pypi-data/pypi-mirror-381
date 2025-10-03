# Publishing Guide for DSA Toolkit

## Prerequisites

1. **Install build tools**:
   ```bash
   pip install --upgrade pip
   pip install build twine
   ```

2. **Create PyPI Account**:
   - Main PyPI: https://pypi.org/account/register/
   - Test PyPI (for testing): https://test.pypi.org/account/register/

## Step-by-Step Publishing

### 1. Update Package Information

Before publishing, update these files with your information:

- **setup.py**: Replace `author`, `author_email`, and `url`
- **pyproject.toml**: Replace author name and email
- **LICENSE**: Replace "Your Name" with your actual name
- **README.md**: Update contact information and GitHub URLs

### 2. Clean Previous Builds

```bash
# Remove old build artifacts
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
```

### 3. Build the Package

```bash
# Build distribution packages
python -m build
```

This creates:
- `dist/dsa-toolkit-1.0.0.tar.gz` (source distribution)
- `dist/dsa_toolkit-1.0.0-py3-none-any.whl` (wheel distribution)

### 4. Test on Test PyPI (Recommended)

```bash
# Upload to Test PyPI first
python -m twine upload --repository testpypi dist/*

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ dsa-toolkit
```

### 5. Publish to PyPI

```bash
# Upload to PyPI
python -m twine upload dist/*
```

You'll be prompted for:
- Username: Your PyPI username
- Password: Your PyPI password or API token

### 6. Verify Installation

```bash
# Install your package
pip install dsa-toolkit

# Test it
python -c "from dsa import sorting; print('Success!')"
```

## Using API Tokens (Recommended)

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Use token for authentication:
   ```bash
   python -m twine upload dist/* -u __token__ -p pypi-YOUR-TOKEN-HERE
   ```

## Version Updates

When releasing new versions:

1. Update version in:
   - `setup.py` (line 12: `version="1.0.1"`)
   - `pyproject.toml` (line 6: `version = "1.0.1"`)
   - `dsa/__init__.py` (line 7: `__version__ = "1.0.1"`)

2. Clean, rebuild, and upload:
   ```bash
   Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
   python -m build
   python -m twine upload dist/*
   ```

## Quick Publish Script

Save this as `publish.ps1`:

```powershell
# Clean previous builds
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue

# Build package
Write-Host "Building package..." -ForegroundColor Green
python -m build

# Check distribution
Write-Host "Checking distribution..." -ForegroundColor Green
python -m twine check dist/*

# Upload to PyPI
Write-Host "Uploading to PyPI..." -ForegroundColor Green
python -m twine upload dist/*

Write-Host "Done! Package published successfully!" -ForegroundColor Green
```

Then run: `.\publish.ps1`

## Troubleshooting

### Issue: "Package already exists"
- You can't re-upload the same version. Increment the version number.

### Issue: "Invalid distribution"
- Run `python -m twine check dist/*` to validate
- Check for syntax errors in setup.py

### Issue: Authentication failed
- Use API token instead of password
- Check token permissions

## Best Practices

1. ✅ Always test on Test PyPI first
2. ✅ Use semantic versioning (MAJOR.MINOR.PATCH)
3. ✅ Update CHANGELOG for each release
4. ✅ Tag releases in Git: `git tag v1.0.0`
5. ✅ Use API tokens for automation
6. ✅ Never commit tokens to version control

## Resources

- PyPI Documentation: https://packaging.python.org/
- Twine Documentation: https://twine.readthedocs.io/
- Python Packaging Guide: https://packaging.python.org/tutorials/packaging-projects/
