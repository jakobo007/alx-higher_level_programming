#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a POST request to the URL with the variables email and subject
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

