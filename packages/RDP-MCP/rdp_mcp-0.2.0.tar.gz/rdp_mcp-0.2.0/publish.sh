#!/bin/bash
# Script to publish rdp-mcp to PyPI

set -e  # Exit on error

echo "🚀 Publishing rdp-mcp to PyPI"
echo ""

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Run this from the rdp-mcp-server directory."
    exit 1
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info

# Create virtual environment for building if it doesn't exist
if [ ! -d ".build-venv" ]; then
    echo "📦 Creating build virtual environment..."
    python3 -m venv .build-venv
fi

# Activate virtual environment
echo "📦 Activating build environment..."
source .build-venv/bin/activate

# Install/upgrade build tools
echo "📦 Installing build tools..."
pip install --quiet --upgrade pip build twine

# Build the package
echo "🔨 Building package..."
python3 -m build

# Check the package
echo "✅ Checking package..."
python3 -m twine check dist/*

# Deactivate venv
deactivate

echo ""
echo "📋 Package built successfully!"
echo ""
echo "Contents of dist/:"
ls -lh dist/

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Next steps:"
echo ""
echo "1. TEST on TestPyPI first (RECOMMENDED):"
echo "   source .build-venv/bin/activate"
echo "   python3 -m twine upload --repository testpypi dist/*"
echo "   # You'll need your TestPyPI API token"
echo "   # Username: __token__"
echo "   # Password: [your TestPyPI token]"
echo ""
echo "   # Test install:"
echo "   uvx --from https://test.pypi.org/simple/ rdp-mcp"
echo ""
echo "2. Upload to REAL PyPI (when ready):"
echo "   source .build-venv/bin/activate"
echo "   python3 -m twine upload dist/*"
echo "   # You'll need your PyPI API token"
echo "   # Username: __token__"
echo "   # Password: [your PyPI token]"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
