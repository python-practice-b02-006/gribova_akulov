
import numpy as np
import pygame as pg
from random import randint
import io_
import physics
import gui

SIZE = (1020, 640)
A=[]

BLACK = (0, 0, 0)
LSALMON = (255, 160, 122)
PEACH = (255, 218, 185)
LEMONE = (255, 250, 205)
SKYBLUE = (100, 149, 237)
TOMATO = (255, 99, 71)
CADET = (176, 196, 222)
SLATE = (106, 90, 205)
DARK = (72, 61, 109)
BROWN = (139, 69, 19)
GREY = (130, 130, 130)
COLORS = [LSALMON, PEACH, LEMONE, SKYBLUE, TOMATO, GREY, CADET, BROWN]

pg.init()

pg.mixer.init()
pg.mixer.music.load('pups.mp3')
pg.mixer.music.play()

clock = pg.time.Clock()
balls = physics.Balls()
button = gui.Button()
screen = pg.display.set_mode((1020, 640))

FPS = 30
finished = False

while not finished:

    for event in pg.event.get():

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                finished = True
    screen.fill((125, 125, 125))
    k = button.time_()
    if k == 0:
        clock.tick(10000)
        balls.iterate(0)
    else:
        balls.iterate(0.01)
        clock.tick(1000 * k)


    balls.draw(screen)
    button.handle_events(pg.event.get())
    button.draw(screen)
    pg.display.update()
    
pg.quit()