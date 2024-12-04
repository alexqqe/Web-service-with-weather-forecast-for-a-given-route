def is_weather_bad(temperature, wind_speed, rain_probability):
    if temperature < 32 or temperature > 95: # температура в фаренгейтах
        return True
    if wind_speed > 31: # скорость в милях
        return True
    if rain_probability > 70:
        return True
    return False
# print(is_weather_bad(40, 10, 2))
# print(is_weather_bad(-444440, 10, 2))
# print(is_weather_bad(40, 1000, 2))