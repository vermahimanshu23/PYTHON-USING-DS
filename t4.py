from turtle import*
side=8 
si =3
for i in range(side):
    rt(360/side)
    fd(100)
    for i in range(si):
        color("blue")
        rt(360/si)
        fd(100)
        dot(25)

mainloop()