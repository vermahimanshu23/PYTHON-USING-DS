import turtle
t=turtle.Turtle()
t.speed(0)
t.screen.bgcolor('black')
t.pensize(2)
t.color('brown')
t.left(90)
t.backward(120)
t.speed(0)
t.shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(2)
        t.color('brown')
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()