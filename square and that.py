import turtle as t

def square():
    for i in range(4):
        t.forward(100)
        t.right(90)
def triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)
def circle():
    for i in range(360):
        t.forward(1)
        t.right(1)
def star():
    for i in range(5):
        t.forward(100)
        t.right(144)
square()
t.clear()
triangle()
t.clear()
star()
t.clear()
circle()
t.exitonclick()

