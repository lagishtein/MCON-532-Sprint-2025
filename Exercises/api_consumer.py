import os
import requests
from dotenv import load_dotenv
load_dotenv()

def get_weather_data(city, api_key):
    """Fetch weather data for a city from OpenWeather API."""
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Request Exception:", err)
    return None

def display_weather(data):
    """Extract and display relevant weather information."""
    if data is None:
        print("No data received from API.")
        return
    if data.get('cod') != 200:
        print("Error:", data.get('message', 'Unknown error'))
        return
    main = data['main']
    wind = data['wind']
    weather_desc = data['weather'][0]['description']
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Pressure: {main['pressure']} hPa")
    print(f"Wind Speed: {wind['speed']} m/s")
    print(f"Weather: {weather_desc.capitalize()}")


if __name__ == "__main__":
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = input("Enter a city name: ")
    data = get_weather_data(city, api_key)
    display_weather(data)
