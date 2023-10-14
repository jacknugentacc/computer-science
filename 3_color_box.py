import turtle
import random 
fillcolorlist = ["red","green","blue","cyan","black","magenta","yellow"]
def square():
    for i in range(4):
        turtle.color()
        turtle.pendown()
        turtle.forward(100)
        turtle.right(90)
        turtle.penup()
for i in range(3):
    chosencolor = random.choice(fillcolorlist)
    fillcolorlist.remove(chosencolor)
    turtle.fillcolor(chosencolor)
    turtle.begin_fill()
    square()
    turtle.end_fill()
    turtle.hideturtle()
    turtle.forward(110)
    turtle.showturtle()
turtle.exitonclick()
#is random :P