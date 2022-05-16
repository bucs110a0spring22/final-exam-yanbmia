import requests
from weather import *
import random

class Poetry:
  def poem():
    list = Weather.tempWeek()
    
    number = list[0]
    website = "https://poetrydb.org/linecount/"+str(number)
    
    request = requests.get(website)
    listofPoems = request.json()
    num = len(listofPoems)
    chooseOne = random.randrange(num+1)

    thePoem =listofPoems[chooseOne]
    
    title = thePoem['title']
    line = thePoem['lines']

    numLine = int(list[1])
    windLine = line[numLine]
    
    return([title,windLine])
    
  
  poem()


    
  
  