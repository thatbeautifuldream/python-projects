import requests
from pprint import pprint

API_Key = 'cb771e45ac79a4e8e2205c0ce66ff633'

city = input('Enter city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)