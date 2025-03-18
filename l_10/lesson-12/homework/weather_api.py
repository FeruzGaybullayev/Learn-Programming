import requests

# Replace with your OpenWeatherMap API key
api_key = "YOUR_API_KEY"

# City for weather data (Tashkent in this case)
city = "Tashkent"

# OpenWeatherMap API endpoint for current weather
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Sending GET request to the OpenWeatherMap API
response = requests.get(url)

# If the request is successful (status code 200)
if response.status_code == 200:
    data = response.json()
    
    # Extracting relevant information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    
    # Printing the weather details
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error fetching weather data.")