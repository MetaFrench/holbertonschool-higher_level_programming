#!/usr/bin/python3
""" Takes in URL and email, sends POST request to passed URL
with email as parameter, displays body of response
(decoded in utf-8) """
import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
