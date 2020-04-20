from dotenv import load_dotenv
import requests
import json
import time
import pprint
import os
from geopy.geocoders import Nominatim
#https://github.com/geopy/geopy/blob/master/README.rst

load_dotenv()
API_ID = os.getenv('API_ID')

class Weather:
     def __init__(self,address):
          self.addressDefinition(address)

     def addressDefinition(self, address):
          geolocator = Nominatim(user_agent="my_app", timeout=7)
          location = geolocator.geocode(address)

          self.latitude = str(location.latitude)
          self.longitude = str(location.longitude)

          self.climateForward()

     def climateForward(self):
          latitude = self.latitude
          longitude = self.longitude
          require = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' + latitude + '&lon=' + longitude + '&appid=' + API_ID)

          climate = json.loads(require.text)

          print('')
          print('Data de Hoje: ', time.ctime(climate['current']['dt']))
          print('Nascer do Sol: ', time.ctime(climate['current']['sunrise']))
          print('Põr do Sol: ', time.ctime(climate['current']['sunset']))
          print('Temperatura Média: ', '{:.5}'.format(float(climate['current']['temp'])-273))
          print('Descrição do tempo: ', climate['current']['weather'][0]['description'])
          print('')

          for i in range(0,6):
               print(time.ctime(climate['daily'][i]['dt']))
               print('Nascer do Sol: ', time.ctime(climate['daily'][i]['sunrise']))
               print('Põr do Sol: ', time.ctime(climate['daily'][i]['sunset']))
               print('Temperatura Máxima: ', '{:.5}'.format(float(climate['daily'][i]['temp']['max'])-273))
               print('Temperatura Mínima: ', '{:.5}'.format(float(climate['daily'][i]['temp']['min'])-273))
               print('Descrição do tempo: ', climate['daily'][i]['weather'][0]['description'])
               print('')