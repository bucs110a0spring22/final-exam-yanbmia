import requests

def main():
  r = requests.get("http://api.weather.gov/points/40.7,-73.9")
  trivia = r.json()
  #print(type(trivia), trivia)
  
  r2 = requests.get("https://api.weather.gov/gridpoints/OKX/36,34/forecast")
  temp = r2.json()
  #print(type(temp),temp)
  #for key in temp.keys():
    #print(key)
  info = temp['properties']
  #print(info)

  corn = temp['properties']['periods']
  print(corn)
  
  
main()