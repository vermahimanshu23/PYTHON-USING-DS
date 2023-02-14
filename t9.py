from turtle import*
speed(0)
fillcolor('red')
def polygon(side,dis):
    for i in range(side):
        fd(dis)
        lt(360/side)
for i in range(3,30):
    polygon(3,i*10)
    lt(20)
end_fill()
hideturtle()
mainloop()