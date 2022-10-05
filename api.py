import requests
import json

API_URL = "http://api.weatherbit.io/v2.0/current/"
API_KEY = ""
#input APIkey

def make_url(city_name: str) -> str:
    return f"{API_URL}?key={API_KEY}&city={city_name}"

def get_weather(city_name: str) -> dict:
    response = requests.get(make_url(city_name))
    return json.loads(response.content)
