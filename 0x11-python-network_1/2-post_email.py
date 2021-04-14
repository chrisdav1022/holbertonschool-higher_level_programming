#!/usr/bin/python3
"""Sends a POST request."""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
        mail = urllib.parse.urlencode({"email": sys.argv[2]}).encode()
        with urllib.request.urlopen(sys. argv[1], mail) as response:
                print(response.read().decode('utf-8'))
