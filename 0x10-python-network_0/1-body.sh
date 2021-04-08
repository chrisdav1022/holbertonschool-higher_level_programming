#!/bin/bash
#script request to the URL, and displays the body of the response
curl -silent -L "$1" | wc -c
