import time
import requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '648f71380344c14f8d30afd84d40cf00'
CITY = "Prnjavor"


def kelvin_to_c(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_c(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_c(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = time.localtime(response['sys']['sunrise'])
sunset_time = time.localtime(response['sys']['sunset'])

izlazak_sunca = time.strftime("%H:%M", sunrise_time)
zalazak_sunca = time.strftime("%H:%M", sunset_time)


print(f"Temperatura u {CITY}-u: {round(temp_celsius)}C ili {temp_fahrenheit:.2f}F")
print(f"Temperatura u {CITY}-u feels like: {round(feels_like_celsius)}C ili {feels_like_fahrenheit:.0f}F")
print(f"Vlaznost vazduha: {humidity}%")
print(f"Brzina vetra: {wind_speed}m/s")
print(f"Opsti utisak vremena: {description}")
print(f"Sunce izlazi u {izlazak_sunca}")
print(f"Sunce zalazi u {zalazak_sunca}")
