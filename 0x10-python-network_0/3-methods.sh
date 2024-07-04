#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send an OPTIONS request to the URL and display the allowed HTTP methods
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-

