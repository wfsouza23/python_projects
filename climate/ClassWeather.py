from dotenv import load_dotenv
import requests
import json
import time
import pprint
import os
# from geopy.geocoders import Nominatim

# https://github.com/geopy/geopy/blob/master/README.rst

load_dotenv()
API_ID = os.getenv('API_ID')


class Weather:
    def __init__(self, address):
        # geo_locator = Nominatim(user_agent="my_app", timeout=7)
        # location = geo_locator.geocode(address)
        # self.longitude = str(location.longitude)
        # self.latitude = str(location.latitude)
        self.climate_forward(address)

    def climate_forward(self, address):
        # latitude = self.latitude
        # longitude = self.longitude
        # require = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&appid={2}'.format(latitude, longitude, API_ID))

        require = requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+address+'&appid='+API_ID)

        climate = json.loads(require.text)
        
        print('')
        print('Data de Hoje: ', time.ctime(climate['list'][0]['dt']))
        print('Nascer do Sol: ', time.ctime(climate['city']['sunrise']))
        print('Põr do Sol: ', time.ctime(climate['city']['sunset']))
        # print('Temperatura Média: ', '{:.5}'.format(float(climate['main']['temp']) - 273))
        # print('Descrição do tempo: ', climate['weather']['description'])
        print('')
        print('')
        
        
        for i in range(0, 6):
            print(time.ctime(climate['list'][i]['dt']))
            print('Temperatura Mínima: ', '{:.5}'.format(float(climate['list'][i]['main']['temp_min']) - 273))
            print('Temperatura Máxima: ', '{:.5}'.format(float(climate['list'][i]['main']['temp_max']) - 273))
            # print('Descrição do tempo principal: ', climate['list'][i]['weather']['main'])
            # print('Descrição do tempo: ', climate['list'][i]['weather']['description'])
            print('')
        

