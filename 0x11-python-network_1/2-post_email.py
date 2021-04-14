#!/usr/bin/python3
"""Sends a POST request."""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
        email = urllib.parse.urlencode({"email": sys.argv[2]}).encode()
            with urllib.request.urlopen(sys.argv[1], email) as response:
                        print(response.read().decode('utf-8'))
