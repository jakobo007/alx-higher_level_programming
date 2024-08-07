#!/usr/bin/python3
"""Script that fetches a URL"""
import urllib.request


def fetch_url(url):
    """fetch url"""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_url("https://alx-intranet.hbtn.io/status")
