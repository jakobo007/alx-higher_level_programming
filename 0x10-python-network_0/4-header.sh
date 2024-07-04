#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL with the header variable X-School-User-Id set to 98
curl -s -H "X-School-User-Id: 98" "$1"


