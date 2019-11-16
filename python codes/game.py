import pygame
pygame.init()
win=pygame.display.set_mode((400,700)) 
pygame.display.set_caption("EGG JUMP!!")
x1=100;x2=x1-60;x3=x1-80;x4=x1+160;x5=x1+180;x6=x1-100
y1=650;y2=y1-500;y3=y1-400;y4=y1-300;y5=y1-200;y6=y1-100
x=x1+25
y=y1-20
w=10
h=10
width=50
height=10
vel=6
vels2=6;vels3=6;vels4=6;vels5=6;vels6=6;vels1=6
isjump=False
jumpcount=10
path=[0,350]
hitbox1 = (x1 -5,y1 - 5, width+10, height+5);hitbox2 = (x2-5,y2 - 5, width+10, height+5);hitbox3 = (x3 -5,y3 - 5, width+10, height+5);hitbox4 = (x4 -5,y4 - 5, width+10, height+5);hitbox5 = (x5-5,y5 - 5, width+10, height+5);hitbox6 = (x6 -5,y6 - 5, width+10, height+5)
direction = 'Right';direction2 = 'Right';direction3 = 'Right';direction4 = 'Right';direction5 = 'Right';direction6 = 'Right';direction1 = 'Right'
def hit(a,b):
    x=a+25
    y=b-20
    return(x,y)
def animate(x, y, height, width, direction,vel):
    if x < 0:
        direction = 'Right'

    elif x > 350:
        direction = 'Left'

    if direction == 'Right':
        x += vel

    elif direction == 'Left':
        x -= vel

    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(x, y, width, height))

    return x, direction

# main loop
run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if not (isjump):
        if keys[pygame.K_SPACE]:
            isjump=True
    else:
        if jumpcount>=-10:
            neg=1
            if jumpcount<0:
                neg=-1
            y=y-(jumpcount**2)*0.39*neg
            jumpcount=jumpcount-1
        else:
            isjump=False
            jumpcount=10   
    if( x>=x6 and x<=(x6+width) and y>=y6 and y<=(y6+height) ):
        x,y=hit(x5,y5)
    elif( x>=x5 and x<=(x5+width) and y>=y5 and y<=(y5+height) ):
        x,y=hit(x4,y4)
    elif( x>=x4 and x<=(x4+width) and y>=y4 and y<=(y4+height) ):
        x,y=hit(x3,y3)
    elif( x>=x3 and x<=(x3+width) and y>=y3 and y<=(y3+height) ):
        x,y=hit(x2,y2)
    elif( x>=x2 and x<=(x2+width) and y>=y2 and y<=(y2+height) ):
        x,y=hit(x1,y1)
        print("final stage")
    elif( x>=x1 and x<=(x1+width) and y>=y1 and y<=(y1+height) ):
        pygame.quit
    win.fill((0, 0, 0))

    x1, direction1 = animate(x1, y1, height, width, direction1,vels1)
    x2, direction2 = animate(x2, y2, height, width, direction2,vels2)
    x3, direction3 = animate(x3, y3, height, width, direction3,vels3)
    x4, direction4 = animate(x4, y4, height, width, direction4,vels4)
    x5, direction5 = animate(x5, y5, height, width, direction5,vels5)
    x6, direction6 = animate(x6, y6, height, width, direction6,vels6)
    x, direction = animate(x, y, height, width, direction,vel)

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x6,y6,width,height))#6
    pygame.draw.rect(win,(255,0,0),(x5,y5,width,height))#5
    pygame.draw.rect(win,(255,0,0),(x4,y4,width,height))#4
    pygame.draw.rect(win,(255,0,0),(x3,y3,width,height))#3
    pygame.draw.rect(win,(255,0,0),(x2,y2,width,height))#2
    pygame.draw.rect(win,(255,0,0),(x1,y1,width,height))#1
    pygame.draw.rect(win,(255,255,255),(x,y,w,h))
    #pygame.draw.rect(win,(0,255,0),(x2-5,y2 - 5, width+10, height+5),2);pygame.draw.rect(win,(0,255,0),(x3 -5,y3 - 5, width+10, height+5),2);pygame.draw.rect(win,(0,255,0),(x4 -5,y4 - 5, width+10, height+5),2);pygame.draw.rect(win,(0,255,0),(x5 -5,y5 - 5, width+10, height+5),2);pygame.draw.rect(win,(0,255,0),(x6 -5,y6 - 5, width+10, height+5),2);pygame.draw.rect(win,(0,255,0),(x1 -5,y1 - 5, width+10, height+5),2)
    pygame.display.update()
pygame.quits
