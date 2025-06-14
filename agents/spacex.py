import requests

class SpaceXAgent:
    def run(self, _):
        res = requests.get("https://api.spacexdata.com/v4/launches/next")
        data = res.json()
        return {
            "name": data["name"],
            "launch_time": data["date_utc"],
            "location": {
                "name": data["launchpad"],
                "latitude": 28.5618571,
                "longitude": -80.577366
            }
        }
