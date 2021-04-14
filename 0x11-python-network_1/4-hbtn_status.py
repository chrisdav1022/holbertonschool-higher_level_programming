#!/usr/bin/python3
"""status url"""
import requests

if __name__ == '__main__':
    status = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(status.text), status.text))
