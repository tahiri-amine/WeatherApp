import requests
import argparse
import datetime

try:
    parser= argparse.ArgumentParser()
    parser.add_argument("-n",help="a city name",required=True)
    args = parser.parse_args()
   
    # handle the number ginving errour a buil in problem
    url = f"https://wttr.in/{args.n}?format=j1"
    r = requests.get(url) 
    if r.status_code == 200:
        data = r.json()
        temp = data['current_condition'][0]['temp_C']
        humidity = data['current_condition'][0]["humidity"]
        windSpeed = data['current_condition'][0]["windspeedKmph"]
        precip = data['current_condition'][0]["precipMM"]
        weatherdesc = data['current_condition'][0]["weatherDesc"][0]["value"]
        winddir = data['current_condition'][0]["winddir16Point"]
        print(f"""[--===--{args.n.capitalize()}--===-- ]""")
        print(f"Day:{datetime.date.today()} | Time:{datetime.datetime.now().strftime("%H:%M")}")
        print(f"Temperature:{temp}°C")
        print(f"Humidity:{humidity}%")
        print(f"Precipitation:{precip}MM")
        print(f"WindSpeed:{windSpeed}Kmph | Direction:{winddir}")
        print(f"WeatherDescription:{weatherdesc}")
    else:
        print(f"NameError: there is no city with the name '{args.n}'")

except (NameError,requests.exceptions.JSONDecodeError):
    print(f"NameError: there is no city with the name '{args.n}'") # question in try/except should i print or raise the error?

