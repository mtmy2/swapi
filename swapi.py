from pathlib import Path

import requests


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url_add):
        try:
            self.response = requests.get(f'{self.base_url}{url_add}')
            self.response.raise_for_status()
            return self.response
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):

    def get_sw_categories(self):
        self.categories = self.get('/').json().keys()
        return self.categories

    def get_sw_info(self, sw_type):
        return self.get(f'/{sw_type}/').text


def save_sw_data():
    for category in list(SWRequester(
            'https://swapi.dev/api').get_sw_categories()):
        info = SWRequester('https://swapi.dev/api').get_sw_info(category)
        Path('data').mkdir(exist_ok=True)
        with open(f'data/{category}.txt', 'w', encoding="utf-8") as f:
            f.write(info)


url_response = APIRequester('https://swapi.dev/api').get('')
sw_info = SWRequester('https://swapi.dev/api')
categories_list = list(SWRequester(
    'https://swapi.dev/api').get_sw_categories())
SWRequester('https://swapi.dev/api').get_sw_info(categories_list[0])
save_sw_data()
