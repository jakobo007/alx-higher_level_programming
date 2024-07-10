#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
        return func
    except Exception as err:
        print(f"Exception: {err}", file=sys.stderr)
        return None
