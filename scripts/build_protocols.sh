#!/usr/bin/env bash

# Process and build PDFs for all process files in docs/
# Usage: ./build_protocols.sh

set -e  # Exit on error

echo "Processing and building PDFs for all process files in docs/..."
echo ""

# Counters
total=0
parse_success=0
parse_failed=0
build_success=0
build_failed=0

# Find all files matching pattern process-*.md in docs/ and subdirectories
find docs -type f -name "process-*.md" | while read -r file; do
    ((total++))
    
    echo "[$total] Processing: $file"
    
    # Run parse_protocol.py
    if python scripts/parse_protocol.py "$file"; then
        echo "  ✓ Parsing successful"
        ((parse_success++))
        
        # Determine the protocol filename that was created
        dir=$(dirname "$file")
        basename=$(basename "$file")
        protocol_file="$dir/${basename/process-/protocol-}"
        
        echo "  Building PDF: $protocol_file"
        
        # Run myst build
        if myst build "$protocol_file" --pdf; then
            echo "  ✓ PDF build successful"
            ((build_success++))
        else
            echo "  ✗ PDF build failed"
            ((build_failed++))
        fi
    else
        echo "  ✗ Parsing failed"
        ((parse_failed++))
    fi
    echo ""
done

# Check if any files