#!/bin/bash
# Send a DELETE request
url = "$1"
response=$(curl -s -X DELETE "$url")
echo $"response"

