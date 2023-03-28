import pgzrun
WIDTH =1200
HEIGHT =800

box =Rect((50,250),(150,100))
box1 =Rect((600,250),(100,100))
box2 =Rect((350,50),(100,100))
box3 =Rect((350,500),(100,100))
bvx = 2
b1vx = -2
b2vx = -2
b3vx = -2

def draw():
    screen.fill('blue')
    screen.draw.filled_rect(box,'yellow')
    screen.draw.filled_rect(box1,'red')
    screen.draw.filled_rect(box2,'green')
    screen.draw.filled_rect(box3,'green')
    

def update():
    global bvx, b1vx,b2vx,b3vx
    box.x += bvx
    box1.x += b1vx 
    # box2.y -= b2vx
    # box3.y += b3vx
    if box.colliderect(box1):
        bvx = -bvx
        b1vx = -b1vx
        sounds.cling.play()
    if box2.colliderect(box3):
        b2vx = +b2vx
        b3vx = -b3vx
    if box2.bottom < 50:
        b2vx = -b2vx
    if box3.top < 500:
        b3vx = +b3vx
        
    if box.left < 0:
         bvx = -bvx
           
    if box1.right >800:
         b1vx = -b1vx
        #  sounds.exploring.play()
        
    # box.x += 2 # move box to the right every frame
    # box1.x -= 2 # move box to the left every frame
    # box2.y += 2 # move box to the down every frame

pgzrun.go()