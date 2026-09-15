import requests

class WeatherRetrievalAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        res = requests.get(self.base_url, params=params)
        if res.status_code == 200:
            data = res.json()
            return {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"]
            }
        return {"error": "City not found"}

