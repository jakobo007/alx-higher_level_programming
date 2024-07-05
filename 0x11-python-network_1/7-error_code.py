#!/usr/bin/python3
"""imported modules"""
import sys
import requests


def fetch(url):
    """takes url, sends request and displays body"""
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.RequestException as error:
        print("Error:", error)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch(url)