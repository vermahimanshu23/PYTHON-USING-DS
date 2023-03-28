import colorsys
from turtle import*

pensize(2)
h=0.5
speed(0)

for i in range(42):
    c =colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(90)
        rt(100)
        fd(120)
        circle(150,45)
done()