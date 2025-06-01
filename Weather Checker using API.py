import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
