#!/usr/bin/python3
"""Imported modules"""
import sys
import urllib.request


def fetch_url(url, email):
    """takes url and email, sends post request to url"""
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url) as response:
            result = response.read().decode('utf-8')
            print(result)
    
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    fetch_url(url, email)