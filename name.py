import requests

class Name:
  def music():
    number = "120-200-30"
    website = "https://x-colors.herokuapp.com/api/rbg2hex?value="+ number
    print(website)
    request = requests.get(website)
    mus = request.json()
    
    
    print(mus)
  
  music()
  