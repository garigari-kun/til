import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    print(path)


if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    geocode(address)
