#!/bin/bash
#takes URL and displays HTTP methods
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
