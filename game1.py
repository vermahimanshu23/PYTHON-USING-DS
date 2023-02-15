import pgzrun

box =Rect((50,50),(150,100))
box1 =Rect((600,50),(100,100))
# box2 =Rect((350,50),(100,100))
bvx = 10
b2vx = -10

def draw():
    screen.fill('blue')
    screen.draw.filled_rect(box,'yellow')
    screen.draw.filled_rect(box1,'red')
    # screen.draw.filled_rect(box2,'green')
    

def update():
    global bvx, b2vx
    box.x += bvx
    box1.x += b2vx 
    if box.colliderect(box1):
        bvx = -bvx
        b2vx = -b2vx
        sounds.dj.play()
        
    if box.left < 0:
         bvx = -bvx
        
        
    if box1.right >800:
         b2vx = -b2vx
        
        
    # box.x += 2 # move box to the right every frame
    # box1.x -= 2 # move box to the left every frame
    # box2.y += 2 # move box to the down every frame

pgzrun.go()