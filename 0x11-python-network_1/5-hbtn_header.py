#!/usr/bin/python3
"""Imported modules"""
import sys
import requests


def fetch(url):
    """takes url, sends rquest and displays the value"""
    request = requests.get(url)
    value = request.headers.get('X-Request-Id')
    print(value)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch(url)
