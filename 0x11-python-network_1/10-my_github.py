#!/usr/bin/python3
"""Imported modules"""
import sys
import requests


def my_github(username, password):
    """used git credentials to display id"""
    url = "https://api.github.com/user"
    auth = (username, password)
    headers = {'Accept': 'application/vnd.github.v3+json'}

    response = requests.get(url, auth=auth, headers=headers)
    
    """handle request"""
    if response.status_code == 200:
        """if successful"""
        info = response.json()
        print(f"{info['id']}")
    else:
       print("None")
            

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    my_github(username, password)