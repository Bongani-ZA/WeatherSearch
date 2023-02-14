from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Result
from . import api_weather, api_location
import json
import requests
import urllib.request


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def previous_results(request):
    results = Result.objects.all()
    return render(request, 'previous-results.html', {'results': results})


def search(request):

    address = request.GET.get('address')
    location = api_location.get_location(address)
    if location == "Error":
        message = "Invalid address entered."
        return render(request,'message.html', {'message': message})
    else:
        address = location[0]
        longitude = location[1]
        latitude = location[2]
        country_codes = location[3]

        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        time = now.strftime('%H:%M')

        temperature = api_weather.get_weather(longitude, latitude)
        final_data = {'address': address, 'longitude': longitude,
                    'latitude': latitude, 'date': date, 'time': time,
                    'temperature': temperature, 'country_codes': country_codes}

        with open('result/data.json', 'w') as file:
            json.dump(final_data, file)

        return render(request, 'search.html', final_data)


def save_result(request):
    file = open('result/data.json')
    data = json.load(file)

    result = Result()
    result.address = data['address']
    result.longitude = data['longitude']
    result.latitude = data['latitude']
    result.date = data['date']
    result.time = data['time']
    result.temperature = data['temperature']
    result.save()
    message = "Result successfully saved."

    return render(request, 'message.html', {'message': message})


def message(request):
    return render(request,'message.html')
