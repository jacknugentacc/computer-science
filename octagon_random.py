import turtle
import random
colors = ["red","green","blue","cyan","black","magenta","yellow","olive"]
def octagon():
    for i in range(8):
        chosencolor = random.choice(colors)
        colors.remove(chosencolor)
        turtle.color(chosencolor)
        turtle.forward(100)
        turtle.right(45)
turtle.speed(0)
octagon()
turtle.exitonclick()