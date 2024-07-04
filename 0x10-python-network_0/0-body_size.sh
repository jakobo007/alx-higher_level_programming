#!/bin/bash
# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL and display the size of the body of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
