#!/usr/bin/python3
"""imported modules"""
import sys
import urllib.request


def fetch_url(url):
    """takes url, send request and displays value"""
    with urllib.request.urlopen(url) as response:
        value = response.getheader('X-Request-Id')
        print(value)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
