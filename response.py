class ResponseAgent:
    def generate_response(self, city, weather_info):
        if "error" in weather_info:
            return weather_info["error"]
        return (f"The current weather in {city} is {weather_info['condition']} with "
                f"a temperature of {weather_info['temperature']}°C and humidity of "
                f"{weather_info['humidity']}%.")
