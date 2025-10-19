""" import requests
try:
    requests.get("https://www.python.org")
except requests.ConnectionError:
    print('\033[31mO site www.python.org NÃO está acessível.')
else:
    print('\033[33mO site www.python.org está acessível!')"""

import urllib.request
try:
    site = urllib.request.urlopen('http://www.python.org')
except:
    print('\033[31mO site www.python.org NÃO está acessível.')
else:
    print('\033[33mO site www.python.org está acessível!')
    print(site.read())

