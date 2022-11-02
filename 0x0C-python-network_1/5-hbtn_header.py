#!/usr/bin/python3
""" takes URL, sends request to URL
and displays the value of variable X-Request-Id in the response header """
import requests
import sys


if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get('X-Request-Id'))
