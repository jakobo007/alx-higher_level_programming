#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these charachters: .. ? and : 
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    new_text = ""
    for char in text:
        new_text += char
        
        if char in ('.', '?', ':'):
            new_text += "\n\n"
    print(new_text.strip())