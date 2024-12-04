import requests
from is_weather_bad import is_weather_bad

with open('/Users/skomorohovaleks/PycharmProjects/Web-service-with-weather-forecast-for-a-given-route/.venv/API_KEY.txt', "r") as file:
    API_KEY = file.read().strip()
def main(city_name = "Moscow"):
    # URL и параметры
    location_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": API_KEY,
        "q": city_name,
        "language": "en-us",
        "details": "false"
    }

    # Выполнение запроса

    response = requests.get(location_url, params=params)

    match response.status_code:
        case 200:
            data = response.json()
            if data:
                location_key = data[0].get("Key")
                print(f"Location Key for {city_name}: {location_key}")

            else:
                return f"No results found for city: {city_name}"
        case 304:
            return 'Нету интернета(((('
        case 401:
            return 'Ошибка подключения к серверу (не удаётся авторизоваться по данному api ключу)'
        case 503:
            return 'Сервис временно недоступен.'
        case 504:
            return 'Сервер долго отвечает(((('
        case _:
            return f"Error: {response.status_code}, {response.text}"

    weather_url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}'
    params = {
        'apikey': API_KEY,
        'details': 'true'
    }

    response2 = requests.get(weather_url, params=params)
    if response2.status_code == 200:
        fc_data = response2.json()
        print(f'Данные получены')
    else:
        return f"Ошибка получения Weather Data: {response2.status_code}, {response2.text}"

    rain_probability = fc_data[0]['RainProbability']  # %
    temperature = fc_data[0]['Temperature']['Value']  # Unit: F
    wind_speed = fc_data[0]['WindGust']['Speed']['Value']  # Unit: mi/h
    humidity = fc_data[0]['RelativeHumidity']  # %

    needed_data = {
        'rain_probability': rain_probability,
        'temperature': temperature,
        'wind_speed': wind_speed,
        'humidity': humidity
    }

    if is_weather_bad(needed_data['temperature'], needed_data['wind_speed'], needed_data['rain_probability']):
        return 0   # Погодные условия плохие
    else:
        return 1   # 'Погодные условия хорошие'
