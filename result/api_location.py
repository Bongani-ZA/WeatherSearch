import requests
import json
from decouple import config


def get_location(address):
    
    access_token = config('LOCATION_TOKEN')
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?limit=1&proximity=ip&types=place%2Cpostcode%2Caddress&access_token={access_token}'
    response = requests.get(url)

    response_text = response.text
    data = json.loads(response_text)
    json.dump(data, open('result/data.json', 'w'), indent=4)

    if data['features']:
        full_address = data['features'][0]['place_name']
        longitude = data['features'][0]['center'][0]
        latitude = data['features'][0]['center'][1]

        #Extract country codes from JSON data
        country_codes = []
        for i in data['features'][0]['context']:
            dict(i)
            print(i)
        for j in i.keys():
            if j == 'short_code':
                country_codes.append((i[j]))

        return [full_address, longitude, latitude, country_codes]
    else:
        return "Error"
    

