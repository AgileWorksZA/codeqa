#!/bin/bash
# Script to run codeqa on the TypeScript project and copy the results

# Set paths
TS_PROJECT_PATH="/Users/hjonck/Development/gitprojects/AgileWorksZA/mw-core"
CURRENT_DIR=$(pwd)

# Change to the TypeScript project directory
cd "$TS_PROJECT_PATH" || exit 1

# Run codeqa snapshot with verbose output
echo "Running codeqa snapshot in $TS_PROJECT_PATH..."
codeqa snapshot --verbose

# Return to original directory
cd "$CURRENT_DIR" || exit 1

echo "Done!"