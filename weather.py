import requests
import geocoder
import json

API_KEY = '3b9bfe4f6b8e0deb472d15f72fc1a692'


class Weather:
    def __init__(self):
        self.g = geocoder.ip('me').latlng
        self.headers = {
            'appid': API_KEY,
            'lat': str(self.g[0]),
            'lon': str(self.g[1]),
            'units': 'metric'
        }

        weather_endpoint = f'https://api.openweathermap.org/data/2.5/weather'
        response = requests.get(url=weather_endpoint, params=self.headers)

        self.report = response.json()

