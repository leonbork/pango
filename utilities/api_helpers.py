import requests
from configparser import ConfigParser
import os

class ApiHelper:
    def __init__(self):
        config = ConfigParser()
        config.read(os.path.join("config", "config.ini"))
        self.api_key = config["API"]["API_KEY"]
        print(f"Using API key: {self.api_key}")# temporary
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_current_weather(self, city: str) -> tuple:
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["main"]["temp"], data["main"]["feels_like"]
