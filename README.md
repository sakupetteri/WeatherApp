# WeatherApp

Weather and Municipality Info
A web application that retrieves weather and municipality information for a given city. The application fetches the current weather and a description of a specified city using the OpenWeatherMap and OpenAI APIs. It provides users with an interactive web interface to get weather forecasts and municipality descriptions.

Features
Fetches the current weather and next day's forecast of a city using OpenWeatherMap's API.
Retrieves a description of the specified city from OpenAI's GPT-3.5-turbo model.
Displays the weather and city description on the main page.

Requirements
Python 3.x
Flask - Web framework
requests - HTTP library to interact with OpenWeatherMap API
openai - Python client for OpenAI API
python-dotenv - For managing environment variables

Usage
Clone the Repository: git clone https://github.com/your-username/weather-and-municipality-info.git
Install Dependencies: pip install -r requirements.txt
Set Environment Variables:
WEATHER_API_KEY: set to your OpenWeatherMap API key
OPENAI_API_KEY: set to your OpenAI API key
Open a Web Browser: navigate to http://localhost:5000 to access the application

API Documentation
GET /: renders the main page with form input and submit button
POST /: retrieves weather and municipality information for the given city and displays the results
Endpoints
/weather: retrieves weather forecast for a given city
/municipality: retrieves municipality description for a given city
Data Sources
OpenWeatherMap API: used to fetch weather data
OpenAI API: used to fetch description of the specified municipality using OpenAI's GPT-3.5-turbo model.

Contributing
Contributions are welcome! Please submit a pull request with your changes.

License
This project is licensed under the MIT License. See LICENSE.md for details.

Acknowledgments
This project utilizes the OpenAI GPT-3.5-turbo model to provide descriptions of cities. The API is powered by OpenAI, and we appreciate the access to their models for this purpose. For more information about OpenAI and its technologies, visit https://openai.com.

The weather data is powered by the OpenWeatherMap API. Check out their website for more information at https://openweathermap.org.