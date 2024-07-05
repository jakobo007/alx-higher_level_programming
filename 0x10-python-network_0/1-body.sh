#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -s -w "%{http_code}" "$1")
[ "${response: -3}" == "200" ] && echo "${response::-3}"

