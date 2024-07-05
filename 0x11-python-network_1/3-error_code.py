#!/usr/bin/python3
"""Imported modules"""
import sys
import urllib.error
import urllib.request


def fetch_url(url):
    """takes url, sends request and displays body"""
    try:
        with urllib.request.urlopen(url) as response:
            result = response.read().decode('utf-8')
            print(result)
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
        
if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)