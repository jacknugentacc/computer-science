import turtle
def star():
    for i in range(5):
        turtle.forward(1000)
        turtle.right(144)
turtle.penup()
turtle.goto(-500,125)
turtle.pendown()
star()
turtle.exitonclick()