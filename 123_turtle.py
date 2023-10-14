import turtle
def one():
    turtle.setpos(0,100)
    turtle.right(90)
    turtle.forward(200)
    turtle.penup()
def two():
    turtle.setpos(100,100)
    turtle.pendown()
    turtle.left(90)
    for i in range(2):
        turtle.forward(100)
        turtle.right(90)
    for i in range(2):
        turtle.forward(100)
        turtle.left(90)
    turtle.forward(100)
    turtle.penup()
def three():
    turtle.setpos(300,100)
    turtle.pendown()
    for i in range(2):
        turtle.forward(100)
        turtle.right(90)
    turtle.forward(75)
    turtle.setpos(400,0)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
one()
two()
three()
turtle.exitonclick()