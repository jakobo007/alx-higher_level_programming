#!/bin/bash
# Send a DELETE request to the URL and display the body of the response
response=$(curl -s -X DELETE "$1")
echo $"response"

