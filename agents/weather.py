import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAgent:
    def run(self, launch_info):
        lat = launch_info["location"]["latitude"]
        lon = launch_info["location"]["longitude"]
        api_key = os.getenv("OPENWEATHER_API_KEY")

        res = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        )
        return res.json()
