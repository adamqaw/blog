import requests
import datetime
import os

API_KEY = os.eviron.get('polygon_api_key')


class Stock:
    def __init__(self, stocksTicker, date):
        self.stocksTicker = stocksTicker
        self.date = date
        self.polygon_endpoint = f'https://api.polygon.io/v1/open-close/{self.stocksTicker}/{self.date}?apiKey={API_KEY}'
        self.response = requests.get(self.polygon_endpoint).json()
