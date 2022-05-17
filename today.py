import turtle
from weather import *
from poetry import *

class Today:
  def create():
    wn = turtle.Screen()
    tempTurt = turtle.Turtle()
    poemTurt = turtle.Turtle()
    
    listWeather = Weather.tempWeek()
    temperature = listWeather[0]
    windSpeed = listWeather[1]

    listPoem = Poetry.poem()
    title = listPoem[0]
    line = listPoem[1]
    
    
    if temperature > 70:
      tempTurt.color("red")
    
    if temperature > 40 and temperature < 70:
      tempTurt.color("green")
    
    if temperature < 40:
      tempTurt.color("blue")

    style_1 = ('Courier', 30)
    style_2 = ('Courier', 15)
    style_3 = ('Courier', 10,'italic')

    writeTemp = str(temperature)+"°F"
    tempTurt.write(writeTemp,font=style_1,align='center')
    poemTurt.pu()
    poemTurt.goto(0,-30)
    poemTurt.pd()
    poemTurt.write(title,font=style_2,align='center')
    poemTurt.pu()

    poemTurt.goto(0,-50)
    poemTurt.pd()
    poemTurt.write(line +" ["+windSpeed+"]",font=style_3,align="center")
    
    tempTurt.hideturtle()
    poemTurt.hideturtle()
    
    wn.exitonclick()

  create()