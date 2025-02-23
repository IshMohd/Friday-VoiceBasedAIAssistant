import requests

API_KEY = "9ca2f8baf48d4e338df54345252302"  
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {"key": API_KEY, "q": city}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "error" in data:
        return "Sorry, I couldn't fetch the weather for that location."

    return f"The current temperature in {data['location']['name']} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."
