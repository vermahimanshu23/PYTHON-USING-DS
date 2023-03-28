from turtle import*
side=8 
si =3
fillcolor("blue")
for i in range(side):
    fd(100)
    begin_fill()
    for i in range(si):
       
        rt(360/si)
        fd(100)
        dot(25)
    rt(360/side)
    end_fill()
mainloop()
# import turtle   
# ttl = turtle.Turtle()  
  
 
# ttl.color("red")  
  
 
# ttl.begin_fill()  
# ttl.circle(90)  
# ttl.end_fill()  
  
  
# ttl.hideturtle()  
# turtle.done()  