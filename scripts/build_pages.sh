#!/usr/bin/env bash

# build_pages.sh - Initialize Jupyter Book and modify myst.yml

set -e  # Exit on error

# Delete myst.yml if it exists
if [ -f "myst.yml" ]; then
    echo "Removing existing myst.yml..."
    rm myst.yml
fi

echo "Initializing Jupyter Book..."
jupyter book init --write-toc

echo "Modifying myst.yml..."

# Check if myst.yml exists
if [ ! -f "myst.yml" ]; then
    echo "Error: myst.yml not found!"
    exit 1
fi

# Add extends and id to myst.yml
awk '
/^version:/ {print; print "extends:"; print "  - ./site.yml"; next}
{print} 
' myst.yml > myst.yml.tmp && mv myst.yml.tmp myst.yml

echo "✓ Jupyter Book initialization complete!"
echo "✓ myst.yml modified with extends and project ID"