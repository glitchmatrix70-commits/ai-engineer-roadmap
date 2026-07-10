import requests

print("Welcome to the Weather App!")
city = input("Please enter a city name: ")

response = requests.get(f'https://wttr.in/{city}?format=j1')
data = response.json()

print(f"Weather information for {city}:")
print(f"Temperature: {data['current_condition'][0]['FeelsLikeC']}°C")
print(f"Humidity: {data['current_condition'][0]['humidity']}%")
print(f"Weather Description: {data['current_condition'][0]['weatherDesc'][0]['value']}")