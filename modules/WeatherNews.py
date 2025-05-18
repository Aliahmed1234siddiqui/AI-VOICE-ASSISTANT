import requests

def get_weather(city):
    """Fetch weather details from OpenWeatherMap API."""
    API_KEY = "8b2cce6c84994726b74150626251605"  # Replace with your API key
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if there's an error in the response
        if "error" in data:
            return "City not found or invalid request."

        temp = data["current"]["temp_c"]
        desc = data["current"]["condition"]["text"]
        return f"The weather in {city} is {desc} with a temperature of {temp}°C."

    except Exception as e:
        return f"An error occurred: {e}"