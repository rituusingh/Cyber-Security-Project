# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N1mf_-MKJlBzZ_WBPR2s7ibFxw-xKCsi
"""

import requests
from datetime import datetime
api_key = 'be8ddfb82d1bb075237092fc8402c5d8'
location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link= requests.get(complete_api_link)
api_data=api_link.json()
temp_city  = ((api_data['main']['temp'])-273.15)
weather_desc= api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']


print("----------------------------------------------------------------------------------")

print("----------------------------------------------------------------------------------")
r=print("Current temperature is : {:.2f} deg C".format(temp_city))
s=print("Current Weather desc :", weather_desc)
t=print("Current Humidity :",hmdt,'%')
u=print("Current wind speed :",wind_spd, 'kmph')
with open ('weather.txt', 'w') as f :
  f.writelines("r")
  f.writelines("s")
  f.writelines("t")
  f.writelines("u")