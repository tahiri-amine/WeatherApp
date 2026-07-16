import requests
city = input("enter a city name:")
url = f"https://wttr.in/{city}?format=j1"
r = requests.get(url)
data = r.json()
print(f"the temperature in {city} is: {data['current_condition'][0]['temp_C']} deg")

