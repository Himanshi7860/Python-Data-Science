
import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 400

music.play('dreamland')

p = Actor('ironman', pos=(WIDTH//2, HEIGHT//2))

c = Rect ((100,100),(20,20))
speed = 5

def move():
    if keyboard.W:
        p.y -= speed
    elif keyboard.S:
        p.x += speed
    elif keyboard.A:
        p.x-= speed
        p.angle = 10
    if keyboard.D:
        p.y += speed
        p.angle -=10
    else:
        p.angle = 0

def check_for_boundary():
    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x += WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y< 0:
        p.y = HEIGHT

def on_coin_collect():
    global speed
    if p.colliderect(c):
        c.x = randint(50, WIDTH-50)
        c.y = randint(50, HEIGHT-50)
        sounds.arrow.play()
        speed +=1

def draw():
    screen.clear()
    p.draw()
    screen.draw.filled_rect(c, '#00ffAA')
    screen.draw.text(f"Speed : {speed}", (10,10), color="#00ffAA")

def update():
    move()
    check_for_boundary()
    on_coin_collect()
pgzrun.go()
