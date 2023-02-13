from turtle import*
def polygon(side,dis):
    for i in range(side):
        fd(dis)
        lt(360/side)
for i in range(3,10):
    polygon(3,i*10)
    bk(5)
# polygon(3,100)
# polygon(4,100)
# polygon(5,100)
# polygon(6,100)
# polygon(7,100)

hideturtle()
mainloop()