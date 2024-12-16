from flask import Flask, render_template, request
import requests
import os
import openai
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
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
    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Describe the municipality {city}."}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
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
