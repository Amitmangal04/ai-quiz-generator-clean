import requests

city = input("Enter City Name: ")

api_key = "7dd1dc100d229299ac81a02fb27a6ffe"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

print("\nWeather Report")

print("City:", data["name"])

print("Temperature:", data["main"]["temp"], "°C")

print("Feels Like:", data["main"]["feels_like"], "°C")

print("Humidity:", data["main"]["humidity"], "%")

print("Wind Speed:", data["wind"]["speed"], "m/s")

print("Weather:", data["weather"][0]["description"])
