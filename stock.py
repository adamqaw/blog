import requests

API_KEY = 'x5ZqKu9C1wmcAktc92_Jp_8EMQNUD2wQ'


class Stock:
    # def __init__(self, stocksTicker, multiplier, timespan, _from, _to, sort, limit, date):
    def __init__(self, stocksTicker, date, adjusted):
        self.stocksTicker = stocksTicker
        # self.multiplier = multiplier
        # self.timespan = timespan
        # self._from = _from
        # self._to = _to
        # self.sort = sort
        # self.limit = limit
        self.date = date
        self.adjusted = adjusted
        # self.get_stock()

    def get_stock(self):
        polygon_endpoint = f'https://api.polygon.io/v1/open-close/{self.stocksTicker}/{self.date}'
        headers = {
            'apiKey': f'{API_KEY}',
            'stocksTicker': f'{self.stocksTicker}',
            # 'multiplier': f'{self.multiplier}',
            # 'timespan': f'{self.timespan}',
            # 'from': f'{self._from}',
            # 'to': f'{self._to}',
            # 'sort': f'{self.sort}',
            # 'limit': f'{self.limit}',
            'adjusted': {self.adjusted},
            'date': f'{self.date}',
        }
        response = requests.get(f'{polygon_endpoint}', params=headers)

        return response.json()
