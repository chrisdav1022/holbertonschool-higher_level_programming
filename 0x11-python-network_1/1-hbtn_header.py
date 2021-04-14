#!/usr/bin/python3
"""X-Request-Id variable"""
import urllib.request

if __name__=="__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))