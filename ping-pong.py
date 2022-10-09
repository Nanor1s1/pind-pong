from pygame import *
import time as t 

class GameSprite(sprite.Sprite):
    def __init__(self,x,y,size_x,size_y,r,g,b):
        self.x=x
        self.y=y
        self.size_x=size_x
        self.size_y=size_y
        self.color=(r,g,b)
        self.rect=Rect(x,y,size_x,size_y)
    def draw_rect(self):
        draw.rect(window,self.color,self.rect)
    def set_color(self,r,g,b):
        self.color=(r,g,b)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
class Player(GameSprite):
    pass
class pictures(GameSprite):
    def __init__(self,x,y,size_x,size_y,r,g,b,image1=None):
        GameSprite.__init__(self,x,y,size_x,size_y,r,g,b)
        self.image=transform.scale(image.load(image1),(size_x,size_y))
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

move_up=False
move_down=False
window=display.set_mode((900,700))
window.fill((117,187,253))

#создание платформы
platform=pictures(25,275,75,150,0,0,0,'xiao1.png')
platform2=pictures(800,275,75,150,0,0,0,'xiao1.png')
ball=pictures(400,300,50,50,0,0,0,'ball.png')


run=True 
finish=False
clock=time.Clock()
rel_fire=False
speed_x=1
speed_y=1
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        if e.type==KEYDOWN:
            if e.key==K_w:
                move_up=True
            if e.key==K_s:
                move_down=True
        elif e.type==KEYUP:
            if e.key==K_w:
                move_up=False  
            if e.key==K_s:
                move_down=False
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.colliderect(platform.rect) or ball.colliderect(platform2.rect):
        speed_y *=-1
    if ball.rect.y>700 or ball.rect.y<0:
        speed_y *=-1
    if ball.rect.x>900 or ball.rect.x<0:
        speed_x *=-1
     
              
    if move_down:
        platform.rect.y -=3
    if move_up:
        platform.rect.y +=3
    if move_down:
        platform2.rect.y -=3
    if move_up:
        platform2.rect.y +=3

    window.fill((117,187,253))
    platform.draw()
    platform2.draw()
    ball.draw()
    clock.tick(600)
    display.update()
    




