#!/usr/bin/python3
"""Imported module"""
import sys
import requests


def fetch(url, email):
    """takes url and email, sends post to url"""
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    fetch(url, email)
