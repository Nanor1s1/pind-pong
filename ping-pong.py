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
move_up2=False
move_down2=False

score=0
score1=0

font.init()
font1=font.Font(None,40)
font2=font.Font(None,100)

window=display.set_mode((900,700))
display.set_caption('pp')

background=image.load('fon.png')
background=transform.scale(background,(900,700))

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
        if e.type==KEYDOWN:
            if e.key==K_UP:
                move_up2=True
            if e.key==K_DOWN:
                move_down2=True
        elif e.type==KEYUP:
            if e.key==K_UP:
                move_up2=False  
            if e.key==K_DOWN:
                move_down2=False
        if e.type==KEYDOWN:
            if e.key==K_r:
                score=0
                score1=0
                platform=pictures(25,275,75,150,0,0,0,'xiao1.png')
                platform2=pictures(800,275,75,150,0,0,0,'xiao1.png')
                ball=pictures(400,300,50,50,0,0,0,'ball.png')
                window.blit(background,(0,0))
                finish=False
    if finish==False:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        
        window.blit(background,(0,0))
        if ball.colliderect(platform.rect) or ball.colliderect(platform2.rect):
            speed_x *=-1
        if ball.rect.y>700 or ball.rect.y<0:
            speed_y *=-1
        if ball.rect.x>900 or ball.rect.x<0:
            speed_x *=-1
        if ball.rect.x==0:
            score+=0.5
        if ball.rect.x==900:
            score1+=0.5
                
        if move_down:
            platform.rect.y +=3
        if move_up:
            platform.rect.y -=3
        if move_down2:
            platform2.rect.y +=3
        if move_up2:
            platform2.rect.y -=3

        window.blit(background,(0,0))
        text_score=font1.render('Очко1:'+str(int(score)),4,(0,0,0))
        window.blit(text_score,(0,30))

        
        text_score1=font1.render('Очко2:'+str(int(score1)),4,(0,0,0))
        window.blit(text_score1,(0,60))
    
        if score>=10:
            GAME_OVER=font2.render('Первый проиграл',1,(255,0,0))
            window.blit(GAME_OVER,(150,350))
            finish=True
        if score1 >=10:
            GAME_OVER=font2.render('Второй проиграл',1,(255,0,0))
            window.blit(GAME_OVER,(150,350))
            finish=True
        platform.draw()
        platform2.draw()
        
        ball.draw()
    clock.tick(360)
    display.update()

    




