from pygame import*

window = display.set_mode((700,500))
display.set_caption("                                                                                                    ")
background=transform.scale(image.load("Background.png"), (700,500))
window.blit(background,(0,0))
clock=time.Clock()
FPS=60
p1=transform.scale(image.load("sprite1.png"),(100,100))
x1,y1=100,150
p2=transform.scale(image.load("sprite2.png"),(100,100))
x2,y2=400,150
speed=5
game=True
while game:
    window.blit(background,(0,0))
    window.blit(p1,(x1,y1))
    window.blit(p2,(x2,y2))
    keys_pressed=key.get_pressed()
    for ev in event.get():
        if ev.type==KEYDOWN:
            if ev.key==K_LEFT and x1>5:
                x1-=10
            if ev.key==K_RIGHT and x1<595:
                x1+=10
            if ev.key==K_UP and y1>10:
                y1-=10
            if ev.key==K_DOWN and y1<395:
                y1+=10
            if ev.key==K_a and x2>5:
                x2-=10
            if ev.key==K_d and x2<595:
                x2+=10
            if ev.key==K_w and y2>10:
                y2-=10
            if ev.key==K_s and y2<395:
                y2+=10
            
        if ev.type==QUIT:
            game=False
    # if keys_pressed[K_LEFT] and x1>5:
    #     x1-=speed
    # if keys_pressed[K_RIGHT] and x1<595:
    #     x1+=speed
    # if keys_pressed[K_UP] and y1>5:
    #     x1-=speed
    # if keys_pressed[K_DOWN] and y1>395:
    #     x1-=speed
    
    
    
    
    
    
    
    
    
    
    
    
    

    clock.tick(FPS)
    display.update()