#!/bin/bash
# Send a request to the URL and display the size of the body of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
