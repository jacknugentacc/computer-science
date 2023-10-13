import turtle as t

def octagon():
    for i in range (8):
        t.forward(100)
        t.left(45)
def goober():
    for i in range (10):
        t.speed(0)
        octagon()
        t.left(36)
goober()
t.exitonclick()
