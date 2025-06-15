import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAgent:
    def run(self, launch_info):
        lat = launch_info["location"]["latitude"]
        lon = launch_info["location"]["longitude"]
        api_key = os.getenv("WEATHER_API_KEY")

        location = f"{lat},{lon}"
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

        print(f"[WeatherAgent] Requesting: {url}")
        res = requests.get(url)
        data = res.json()
        print("[WeatherAgent] Response:", data)

        return data
