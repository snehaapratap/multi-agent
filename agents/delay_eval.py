class DelayEvalAgent:
    def run(self, weather_data):
        main = weather_data['weather'][0]['main']
        wind_speed = weather_data['wind']['speed']

        if main in ['Thunderstorm', 'Rain'] or wind_speed > 10:
            return f"Launch may be delayed due to {main} and wind speed of {wind_speed} m/s."
        else:
            return "Launch conditions look good. No major delays expected."
