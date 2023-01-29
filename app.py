from flask import Flask
import pandas as pd
import requests
from datetime import datetime
app = Flask(__name__)
# {'coord': {'lon': 121.4581, 'lat': 31.2222}, 
# 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
# 'base': 'stations', 'main': {'temp': 275.19, 'feels_like': 272.1, 'temp_min': 274.07, 
# 'temp_max': 275.89, 'pressure': 1020, 'humidity': 46}, 'visibility': 10000, 
# 'wind': {'speed': 3, 'deg': 240}, 'clouds': {'all': 0}, 'dt': 1674952817, 
# 'sys': {'type': 2, 'id': 2002757, 'country': 'CN', 'sunrise': 1674946116, 'sunset': 1674984330}, 
# 'timezone': 28800, 'id': 1796236, 'name': 'Shanghai', 'cod': 200}


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/city/<city>")
def getCity(city):
    api_key = "eb7c178f50772e2ac375adff2a06fdea"
 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
     
    url = base_url + "appid=" + api_key + "&q=" + city
    res = requests.get(url)
    data = res.json()
    
    name = data['name']
    time = datetime.fromtimestamp(data['dt']).strftime("%A, %B %d, %Y %I:%M:%S")
    lon = data['coord']['lon']
    lat = data['coord']['lat']
    country = data['sys']['country']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = "{:.2f}".format(data['main']['temp'] - 273.15)

    return (name + " is located at (latitude, longitude) " + str(lon) + ", " + str(lat)
      + ". It is in " + country + ". " + "Current local time is " + str(time) + "." + "\n" 
      + 'Current weather info: Temperature: ' + str(temp) + '°C' + ', Wind: ' + str(wind) + 
      ', Pressure: ' + str(pressure) + ', Humidity: ' + str(humidity) + ', Sky: ' + description)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)
