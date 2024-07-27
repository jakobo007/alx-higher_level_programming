#!/bin/bash
 # Send a POST request to the URL with the variables email and subject
curl -s -
X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

