#!/bin/bash
# Send a DELETE request 
response=$(curl -s -X DELETE "$1")
echo $"response"

