#!/bin/bash
# sends request to url and display status code
curl -s -o /dev/null -w "%{http_code}" "$1"
