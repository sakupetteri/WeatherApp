from flask import Flask, render_template, request
import requests
import os
import openai
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

def get_weather(city):
    """Fetches the current and next day's weather of the specified city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city for which the weather is to be fetched.

    Returns:
        dict: A dictionary with the current and next day's weather data. If an error occurs, returns a dictionary with an "error" key.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Weather API response:", data)
        current_weather = data['list'][0]
        next_day_weather = data['list'][1]
        return {
            "current": {
                "temp": current_weather["main"]["temp"],
                "description": current_weather["weather"][0]["description"]
            },
            "next_day": {
                "temp": next_day_weather["main"]["temp"],
                "description": next_day_weather["weather"][0]["description"]
            }
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_municipality_description(city):
    """
    Fetches a description of the specified municipality using OpenAI's GPT-3.5-turbo model.

    Args:
        city (str): The name of the city for which the description is to be fetched.

    Returns:
        str: A text description of the municipality. If an error occurs, returns an error message.
    """

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Describe the municipality {city}.",
            max_tokens=2048
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"Error: {str(e)}"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main page with weather and description of the given city.

    GET request: Render the page with empty variables.
    POST request: Get the city name from the form data and call the
    get_weather and get_municipality_description functions. If an error
    occurred in the weather API, render the error page. Otherwise, render
    the page with the weather and description data.
    """
    weather = description = city = None
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather(city)
        description = get_municipality_description(city)
        if 'error' in weather:
            # Handle the error case
            return render_template("error.html", error=weather['error'])
        else:
            # Render the template as usual
            return render_template("index.html", weather=weather, description=description, city=city)
    return render_template("index.html", weather=weather, description=description, city=city)

if __name__ == "__main__":
    app.run(debug=True)