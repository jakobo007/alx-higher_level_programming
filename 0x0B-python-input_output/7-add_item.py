#!/usr/bin/python3
"""Imported Modules"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__
('6-load_from_json_file').load_from_json_file

"""Script that add all the arguments to a python list and saves them to a file"""
  

# Load the existing list or initialize an empty list
my_list = load_from_json_file("add_item.json") if load_from_json_file("add_item.json") else []

# Append the arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, "add_item.json")
