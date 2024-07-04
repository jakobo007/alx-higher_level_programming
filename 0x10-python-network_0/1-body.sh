#!/bin/bash
# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL and display the body of the response if status code is 200
response=$(curl -s -w "%{http_code}" "$1")
body="${response%???}"
status="${response: -3}"

if [ "$status" -eq 200 ]; then
    echo "$body"
fi
