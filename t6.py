from turtle import*
import turtle
bgcolor('yellow')
pensize(3)
pencolor('red')

def curve():
    for i in range(200):
        rt(1)
        fd(1)

def leaf():
    fillcolor('red')
    begin_fill()
    left(140)
    fd(120)
    curve()
    lt(120)
    curve()
    fd(115)
    dot(20)
    lt(50)
    fd(100)
leaf()
turtle.done()


