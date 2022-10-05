import api

city_name = input('Input city name: ')
weather = api.get_weather(city_name)
weather_data = weather['data'][0]

print(f"Temperature in city: {weather_data['temp']} °C \nDescription: {weather_data['weather']['description']}")
