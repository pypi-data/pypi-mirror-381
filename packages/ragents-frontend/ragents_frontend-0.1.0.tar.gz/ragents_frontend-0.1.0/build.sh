#!/bin/bash
set -e

echo "Building RAGents Frontend Package..."

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist/
rm -rf src/ragents_frontend/frontend_build

# Check if Next.js build exists
if [ ! -d "../.next" ]; then
    echo "Error: Next.js build not found at ../.next"
    echo "Please run 'npm run build' in the project root first"
    exit 1
fi

# Copy Next.js production build
echo "Copying Next.js production build..."
mkdir -p src/ragents_frontend/frontend_build
cp -r ../.next src/ragents_frontend/frontend_build/.next

# Copy public assets if they exist
if [ -d "../public" ]; then
    echo "Copying public assets..."
    cp -r ../public src/ragents_frontend/frontend_build/public
fi

# Build the package
echo "Building package..."
uv build

echo "✓ Package built successfully!"
echo "  Files: dist/ragents_frontend-0.1.0-py3-none-any.whl"
echo "         dist/ragents_frontend-0.1.0.tar.gz"
echo ""
echo "To install: uv pip install dist/ragents_frontend-0.1.0-py3-none-any.whl"
echo "To publish to PyPI: uv publish"
