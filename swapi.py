import os

import requests


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.session()

    def get(self, url_add):
        try:
            self.response = self.session.get(f'{self.base_url}/{url_add}')
            self.response.raise_for_status()
            return self.response
        except requests.ConnectionError:
            return '<ошибка на сервере>'
        except requests.RequestException as e:
            return str(e)


class SWRequester(APIRequester):

    def __init__(self):
        super().__init__()

    def get_sw_categories(self):
        self.categories = list(self.get('').json().keys())
        return self.categories

    def get_sw_info(self, sw_type):
        self.info = self.get(f'{sw_type}')
        return self.info.text

    def save_sw_info(self):
        for category in self.get_sw_categories():
            self.info = self.get_sw_info(category)
            os.makedirs('data', exist_ok=True)
            with open(f'data/{category}.txt', 'w', encoding="utf-8") as f:
                f.write(self.info)


url_response = APIRequester('https://swapi.dev/api').get('')
sw_info = SWRequester()
categories_list = SWRequester().get_sw_categories()
SWRequester().get_sw_info(categories_list[0])
SWRequester().save_sw_info()
