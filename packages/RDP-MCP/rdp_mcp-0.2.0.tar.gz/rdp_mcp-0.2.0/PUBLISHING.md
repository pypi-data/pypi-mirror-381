# Publishing rdp-mcp to PyPI

This guide walks you through publishing the RiboSeq MCP server to PyPI so anyone can install it with `pip install rdp-mcp` or `uvx rdp-mcp`.

## Prerequisites

### 1. Create PyPI Accounts

You need accounts on both TestPyPI (for testing) and PyPI (for production).

**TestPyPI** (for testing):
1. Go to https://test.pypi.org/account/register/
2. Create an account
3. Verify your email
4. Go to https://test.pypi.org/manage/account/token/
5. Create an API token with scope: "Entire account"
6. Save the token somewhere safe (starts with `pypi-`)

**PyPI** (production):
1. Go to https://pypi.org/account/register/
2. Create an account
3. Verify your email
4. Go to https://pypi.org/manage/account/token/
5. Create an API token with scope: "Entire account"
6. Save the token somewhere safe

### 2. Install Publishing Tools

```bash
python3 -m pip install --upgrade build twine
```

## Publishing Process

### Step 1: Prepare the Package

Make sure everything is ready:
- ✅ `pyproject.toml` has correct version number
- ✅ `README.md` is up to date
- ✅ `CHANGELOG.md` is updated
- ✅ `LICENSE` file exists
- ✅ All code changes are committed

### Step 2: Build the Package

Run the publish script:

```bash
cd rdp-mcp-server
./publish.sh
```

This will:
- Clean previous builds
- Install build tools
- Build the package
- Check the package for errors

You should see files in `dist/`:
- `riboseq_mcp-0.2.0-py3-none-any.whl` (wheel)
- `riboseq_mcp-0.2.0.tar.gz` (source)

### Step 3: Test on TestPyPI (IMPORTANT!)

Always test on TestPyPI first before publishing to real PyPI:

```bash
python3 -m twine upload --repository testpypi dist/*
```

When prompted:
- **Username:** `__token__`
- **Password:** Your TestPyPI API token (paste the full token including `pypi-`)

### Step 4: Test Install from TestPyPI

In a new terminal or virtual environment:

```bash
# Test with pip
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ rdp-mcp

# Or test with uvx
uvx --from https://test.pypi.org/simple/ rdp-mcp
```

**Verify it works:**
```bash
# Should show version 0.2.0
python3 -c "import riboseq_mcp; print(riboseq_mcp.__version__)"
```

### Step 5: Upload to Production PyPI

Once you've verified everything works on TestPyPI:

```bash
python3 -m twine upload dist/*
```

When prompted:
- **Username:** `__token__`
- **Password:** Your PyPI API token

### Step 6: Verify on PyPI

1. Go to https://pypi.org/project/rdp-mcp/
2. Check that the page looks correct
3. Test installation:

```bash
pip install rdp-mcp
# or
uvx rdp-mcp
```

## After Publishing

### Update Documentation

Update the README to show the simple installation:

```markdown
## Installation

```bash
# Using uvx (recommended)
uvx rdp-mcp

# Or using pip
pip install rdp-mcp
```
```

### Configure Claude Desktop

Users can now use:

```json
{
  "mcpServers": {
    "riboseq": {
      "command": "uvx",
      "args": ["rdp-mcp"]
    }
  }
}
```

No local path needed!

## Updating to a New Version

When you want to release a new version:

1. **Update version number** in:
   - `pyproject.toml` → `version = "0.3.0"`
   - `src/riboseq_mcp/__init__.py` → `__version__ = "0.3.0"`

2. **Update CHANGELOG.md** with new features/fixes

3. **Commit changes:**
   ```bash
   git add .
   git commit -m "Release v0.3.0"
   git tag v0.3.0
   ```

4. **Rebuild and publish:**
   ```bash
   ./publish.sh
   # Test on TestPyPI first
   python3 -m twine upload --repository testpypi dist/*
   # Then production
   python3 -m twine upload dist/*
   ```

## Troubleshooting

### "File already exists"
You can't overwrite a version on PyPI. You need to increment the version number.

### "Invalid distribution filename"
Make sure your package name in `pyproject.toml` matches the filename pattern.

### "Authentication failed"
- Check you're using `__token__` as username (with two underscores)
- Make sure you copied the entire API token including the `pypi-` prefix
- Verify you're using the right token (TestPyPI vs PyPI)

### "Package dependencies not found"
When installing from TestPyPI, use both indexes:
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ rdp-mcp
```

## Security Notes

- ✅ **Never commit your API tokens to git**
- ✅ Store tokens in a password manager
- ✅ Use scoped tokens (project-specific) when possible
- ✅ Rotate tokens periodically
- ✅ Keep `dist/` in `.gitignore`

## Quick Reference

```bash
# Build
./publish.sh

# Test on TestPyPI
python3 -m twine upload --repository testpypi dist/*

# Production PyPI
python3 -m twine upload dist/*

# Test install
uvx --from https://test.pypi.org/simple/ rdp-mcp  # TestPyPI
uvx rdp-mcp  # Production PyPI
```

## Resources

- PyPI: https://pypi.org/
- TestPyPI: https://test.pypi.org/
- Packaging Guide: https://packaging.python.org/
- Twine Docs: https://twine.readthedocs.io/
