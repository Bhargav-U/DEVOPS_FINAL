import requests
from flask import Flask, render_template
app = Flask(__name__)

API_KEY = "900444decf24eb9242327d4a0b4f8a80"
CITY = "Chennai"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data():
    # Send request to OpenWeatherMap API
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"  # To get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        # Extract relevant data
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"]
        }
        return weather_info
    else:
        return {"error": "Failed to get weather data"}

@app.route('/')
def index():
    weather_data = get_weather_data()
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9095)

