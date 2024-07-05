#!/usr/bin/python3
"""Imported modules"""
import sys
import requests


def search_api(letter, url):
    """sends post request to url with letter as parameter"""
    data = {'q': letter}
    if not letter:
        data['q'] = ""
        
    response = requests.post(url, data=data)
    response_json = response.json()
    
    """check if json is valid"""
    if isinstance(response_json, list) and len(response_json) > 0:
        user = response_json[0]
        print(f"{user.get('id')}, {user.get('name')}")
    elif response_json == {}:
        print("No result")
    else:
        print("Not a valid JSON")

    
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1]
    search_api(letter, url)