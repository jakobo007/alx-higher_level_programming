#!/usr/bin/python3
"""Imported modules"""
import requests


def fetch(url):
    """fetch url using request package"""
    r = requests.get(url)
    body = r.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch(url)
