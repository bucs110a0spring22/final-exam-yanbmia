import requests

class Weather:
  def tempWeek():
    r = requests.get("http://api.weather.gov/points/40.7,-73.9")
    
    req = requests.get("https://api.weather.gov/gridpoints/OKX/36,34/forecast")
    info = req.json()

    properties = info['properties']
    periods = properties['periods']

    today = periods[0]

    temp = today['temperature']
    wind = today['windSpeed']

    windNum = wind[0:1]
    
    return([temp,windNum])
    #return(windNum)

    
    
  tempWeek()
    
    