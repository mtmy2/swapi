import os

import requests


class APIRequester:
    base_url = 'https://swapi.dev/api/'
    session = requests.session()

    def __init__(self):
        pass

class Response(APIRequester):


    def __init__(self):
       pass    

    def get(self):
        try:
            self.response = self.session.get(self.base_url)
            self.response.raise_for_status()
            #print(self.response)
            return self.response
        except requests.ConnectionError:
            return '<ошибка на сервере>'
        except Exception as e:
            return str(e)
        
class SWRequester(APIRequester):

    def __init__(self):
       super().__init__()

    def get_sw_categories(self):
        self.categories = list(self.session.get(self.base_url).json().keys())
        #self.categories_dict = dict(self.categories.text)
        #print(f'категории {self.categories}')
        return self.categories
    
    def get_sw_info(self, sw_type):
        self.info = self.session.get(f'{self.base_url}{sw_type}/')
        #print(self.info.text)
        return self.info.text
    
    def save_sw_info(self):
        for category in self.get_sw_categories():
            self.info = self.get_sw_info(category)
            os.makedirs('data', exist_ok=True)
            with open(f'data/{category}.txt', 'w', encoding="utf-8") as f:
                f.write(self.info)

url_response = Response()
url_response.get()
sw_info = SWRequester()
categories_list = SWRequester().get_sw_categories()
SWRequester().get_sw_info(categories_list[0])
SWRequester().save_sw_info()
        
        



