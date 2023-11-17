import requests

API_KEY = 'AIzaSyDmnCXO5w0f_24v0Uf8WWyeFZ9PBdSlcHw'

def getGeoCoord(address):
    params = {
        'key': API_KEY,
        'address': address.replace(' ', '+')
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        result = data['results'][0]
        location = result['geometry']['location']
        return location['lat'], location['lng']
    else:
        return
print(getGeoCoord("dhaka bangladesh"))
