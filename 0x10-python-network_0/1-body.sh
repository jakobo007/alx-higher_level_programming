#!/usr/bin/bash
#sends get request to url
[ -z "$1" ] && { echo "Usage: $0 <url>"; exit 1; }
curl -sL -w "%{http_code}" "$1" -o /tmp/response_body | grep -q 200 && cat /tmp/response_body

