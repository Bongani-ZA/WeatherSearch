import requests
import json


def get_weather(longitude, latitude):
    access_token = '4d7b59699fd915c21ea1ccc1de5749b5'
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={access_token}&units=metric'
    response = requests.get(url)
    response_text = response.text
    data = json.loads(response_text)
    json.dump(data, open('result/data.json', 'w'), indent=4)
    return round(data['current']['temp'])
