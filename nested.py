from turtle import*
speed(0)
pencolor("blue")
fillcolor('red')
side=6
for i in range(side):
    fd(100)
    begin_fill()
    for i in range(side):
        fd(50)
        for i in range(side):
            fd(25)
            lt(360/side)
        rt(360/side)
    end_fill()
    lt(360/side)
hideturtle()
mainloop()