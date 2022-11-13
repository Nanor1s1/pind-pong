#Создай собственный Шутер!

from pygame import *
from random import randint
import time as t 

num_fire=0

class GameSprite(sprite.Sprite):
    def __init__(self,x,y,size_x,size_y, img):
        super().__init__()
        self.image=image.load(img)
        self.image=transform.scale(self.image,(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
        
class Player(GameSprite):
    def update(self):
        for i in event.get():
            if i.type==KEYDOWN:
                if i.key==K_d:
                    self.rect.x+=5
                if i.key==K_a:
                    self.rect.x-=5
    def update2(self):
        keys=key.get_pressed()
        if keys[K_d]:
            self.rect.x+=5
        if keys[K_a]:
            self.rect.x-=5
        if self.rect.x>750:
            self.rect.x=0
        if self.rect.x<0:
            self.rect.x=700
    def fire(self):
        bullet1=Bullet(self.rect.x,self.rect.y,50,50,"bullet.png")
        bullet.add(bullet1)


class Enemy(GameSprite):
    def update(self):
        global lose
        self.rect.y+=randint(1,5)
        if self.rect.y>700:
            self.rect.y=0
            self.rect.x=randint(50,600)
            lose+=1

class Bullet(GameSprite):
    def update(self):
        self.rect.y-=3
        if self.rect.y <0:
            self.kill()

bullet=sprite.Group()

font.init()
font1=font.Font(None,30)
font2=font.Font(None,100)

lose=0
score=0
live=5

win=display.set_mode((700,700))
display.set_caption('Шутер')

background=image.load('galaxy.jpg')
background=transform.scale(background,(700,700))

player=Player(300,600,100,100,"rocket.png")
enemis=sprite.Group()
for i in range(5):
    enemy=Enemy(randint(0,600),0,100,75,'ufo.png')
    enemis.add(enemy)

asteroids=sprite.Group()
for o in range(6):
    asteroid=Enemy(randint(0,600),0,100,75,'asteroid.png')
    asteroids.add(asteroid)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

run=True 
finish=False
clock=time.Clock()
rel_fire=False
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        if e.type == KEYDOWN:
            if e.key==K_SPACE:
                if num_fire<5 and rel_fire==False:
                    player.fire()
                    num_fire+=1
                else:
                    rel_fire=True
                    start_time=t.time()
    if rel_fire:
        end_time=t.time()
        if end_time-start_time>1:
            rel_fire=False
            num_fire=0
    if finish==False:
        win.blit(background,(0,0))
        player.draw()
        player.update2()
        bullet.draw(win)
        bullet.update()
        enemis.draw(win)
        enemis.update()
        asteroids.draw(win)
        asteroids.update()
        if sprite.spritecollide(player,asteroids,True):
            live-=1
        text_lose=font1.render('Пропущено:'+str(lose),1,(255,255,255))
        win.blit(text_lose,(0,0))

        text_score=font1.render('Очко:'+str(score),1,(255,255,255))
        win.blit(text_score,(0,30))

        enemy_list=sprite.groupcollide(enemis,bullet,True,True)
        text_live=font1.render('Жизнь:'+str(live),1,(255,255,255))
        win.blit(text_live,(600,0))
        
        if enemy_list:
            enemy=Enemy(randint(0,600),0,100,75,'ufo.png')
            enemis.add(enemy)
            score+=1
        if lose>100:
            GAME_OVER=font2.render('Ты ЛОХ',1,(255,0,0))
            win.blit(GAME_OVER,(250,350))
            finish=True
        if score>100:
            GAME_OVER=font2.render('ПОБЕДА',1,(2,125,22))
            win.blit(GAME_OVER,(250,350))
            finish=True
        if live==0:
            GAME_OVER=font2.render('Ты ЛОХ',1,(255,0,0))
            win.blit(GAME_OVER,(250,350))
            finish=True
        win.blit(text_score,(0,30))
        #enemy.update()
        clock.tick(360)
        display.update()