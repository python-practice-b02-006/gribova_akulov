# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:06:37 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint

SIZE = (1200, 600)

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

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Now it's my work")
clock = pg.time.Clock()


done = False
'''
pg.mixer.music.load('bisnesss.mp3')
pg.mixer.music.play()'''

SC_IMG = pg.image.load("night_forest.jpg")
screen.blit(SC_IMG, (0, 0))
screen.blit(SC_IMG, (337, 0))
screen.blit(SC_IMG, (674, 0))
screen.blit(SC_IMG, (1011, 0))

class Schedule():
    def __init__(self, number, left_side = 50, ceiling = 50, color=None):
        self.l = left_side
        if color == None:
            self.color = COLORS[randint(0,len(COLORS)-1)]
        self.c = ceiling
        self.coord = [[[self.l + 150, self.c], [self.l + 75, self.c + 75],
                       [self.l + 75, self.c + 200], [self.l + 125, self.c + 200],
                       [self.l + 50, self.c + 250], [self.l + 50, self.c +300],
                       [self.l + 125, self.c + 250], [self.l + 175, self.c + 250],
                       [self.l + 250, self.c + 300], [self.l + 250, self.c + 250],
                       [self.l + 175, self.c + 200], [self.l + 225, self.c + 200],
                       [self.l + 225, self.c + 75], [self.l + 150, self.c]],
                      [[self.l+400 + 150, self.c+200], [self.l+400 + 50, self.c+200 + 100],
                       [self.l+400 + 100, self.c+200 + 150], [self.l+400 + 50, self.c+200 +225],
                       [self.l+400 + 50, self.c+200 + 300], [self.l+400 + 100, self.c+200 + 225],
                       [self.l+400 + 150, self.c+200 +300], [self.l+400 + 200, self.c+200 +225],
                       [self.l+400 + 250, self.c+200 +300], [self.l+400 + 250, self.c+200 +225],
                       [self.l+400 + 200, self.c+200 +150], [self.l+400 + 250, self.c+200 +100],
                       [self.l+400 + 150, self.c+200]],
                      [[self.l+800 + 225,self.c +0],[self.l+800 + 0,self.c +0],
                       [self.l+800 + 0,self.c +225], [self.l+800 + 75,self.c + 300],
                       [self.l+800 + 75,self.c +175], [self.l+800 + 175,self.c +300],
                       [self.l+800 + 175,self.c +175], [self.l+800 + 300,self.c +175],
                       [self.l+800 + 175,self.c +75], [self.l+800 + 300,self.c +75],
                       [self.l+800 + 225,self.c +0]]]
    
    def draw(self, screen, n):
        pg.draw.lines(screen, self.color, False, self.coord[n-1], 5)

class Figures():
    pass

class Match():
    pass


rocket1 = Schedule(1)
rocket2 = Schedule(2)
rocket3 = Schedule(3)

while not done:
    clock.tick(30)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    rocket1.draw(screen,1)
    rocket2.draw(screen,2)
    rocket3.draw(screen,3)
    
pg.quit()