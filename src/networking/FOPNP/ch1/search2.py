import requests

def geocode(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    geocode(address)
