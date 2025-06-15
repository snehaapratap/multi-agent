class DelayEvalAgent:
    def run(self, weather_data):
        if 'current' not in weather_data:
            return "Weather data not available."

        condition = weather_data['current']['condition']['text']
        wind_kph = weather_data['current']['wind_kph']
        temp_c = weather_data['current']['temp_c']

        if 'Rain' in condition or wind_kph > 20:
            return f"Possible delay: {condition} with wind speed {wind_kph} kph and temp {temp_c}°C."
        else:
            return f"Conditions look fine: {condition}, wind {wind_kph} kph, temperature {temp_c}°C."
