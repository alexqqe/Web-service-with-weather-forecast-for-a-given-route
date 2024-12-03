import requests

# получаем апи-ключ
with open('/Users/skomorohovaleks/PycharmProjects/Web-service-with-weather-forecast-for-a-given-route/.venv/API_KEY.txt', "r") as file:
    API_KEY = file.read().strip()

# Широта и долгота
latitude = 55.7558
longitude = 37.6173

# Шаг 1: Получение Location Key для заданных координат
location_url = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
params = {
    "apikey": API_KEY,
    "q": f"{latitude},{longitude}"
}

response = requests.get(location_url, params=params)
if response.status_code == 200:
    location_data = response.json()
    location_key = location_data.get("Key")
    print(f"Location Key: {location_key}")
else:
    print(f"Ошибка получения Location Key: {response.status_code}, {response.text}")
    exit()

weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}'
params={
    'apikey': API_KEY,
    'details': 'true'
}

response2 = requests.get(weather_url, params=params)
if response2.status_code == 200:
    weather_data = response2.json()
    print(f'Weather Data: {weather_data}')
else:
    print(f"Ошибка получения Weather Data: {response2.status_code}, {response2.text}")