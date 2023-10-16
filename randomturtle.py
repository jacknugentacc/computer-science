import turtle
import random
def rand():
    for i in range(random.randint(1,100)):
        turtle.forward(random.randint(1,50))
        rightorleft = random.randint(1,2)
        if rightorleft == 1:
            turtle.right(random.randint(0,360))
        if rightorleft == 2:
            turtle.left(random.randint(0,360))
turtle.speed(0)
rand()
turtle.exitonclick()