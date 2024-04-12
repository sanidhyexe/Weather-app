import requests
import json
import pyttsx3

city = input("Enter the name of the city : \n")
try:
    url = f"https://api.weatherapi.com/v1/current.json?key=58ffba5cd69941feb0140412241204&q={city}"

    r = requests.get(url)
    #print(r.text)
    wdic = json.loads(r.text)
    w = wdic["current"]["temp_c"]
    print(f"The weather in {city} is {w} degrees")
    engine = pyttsx3.init()
    engine.say(f"The weather in {city} is {w} degrees")
    engine.runAndWait()
except:
    print("Invalid city name")
