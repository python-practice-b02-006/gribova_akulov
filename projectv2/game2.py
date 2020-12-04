# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:06:37 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint

def mediana(a, b, c):
    m_a = int(np.sqrt(2*(b**2+c**2)-a**2)/3)
    m_b = int(np.sqrt(2*(a**2+c**2)-b**2)/3)
    m_c = int(np.sqrt(2*(b**2+a**2)-c**2)/3)
    return min(m_a+1, m_b+1, m_c+1)

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

class Figure():
    def __init__(self, dots, color=None):
        self.norm_dots = dots
        self.coord=[0, 0]
        self.dots = [0]*len(dots)
        for i in range(len(dots)):
            self.coord[0] += int(dots[i][0]/len(dots))
            self.coord[1] += int(dots[i][1]/len(dots))
            self.dots[i] = (dots[i][0], dots[i][1])
        self.color = COLORS[randint(0,len(COLORS)-1)]
        self.active = 0
        if len(dots)==3:
            self.rad = mediana(np.sqrt((dots[0][0]-dots[1][0])**2+(dots[0][1]-dots[1][1])**2),
                               np.sqrt((dots[0][0]-dots[2][0])**2+(dots[0][1]-dots[2][1])**2),
                               np.sqrt((dots[2][0]-dots[1][0])**2+(dots[2][1]-dots[1][1])**2))
        if len(dots) == 4:
            self.rad = int(min(np.sqrt((dots[3][0]-dots[1][0])**2+(dots[1][1]-dots[3][1])**2),
                           np.sqrt((dots[0][0]-dots[2][0])**2+(dots[0][1]-dots[2][1])**2)))
        print(self.coord, self.rad)
        self.time = 1

    def convert_dots(self):
        for i in range(len(self.dots)):
            self.dots[i] = (self.norm_dots[i][0], self.norm_dots[i][1])
        return self.dots
    
    def draw(self, screen):
        pg.draw.polygon(screen, self.color,  figure.convert_dots())

    def movement(self, mouse_pos):
        if ((mouse_pos[0] - self.coord[0]) ** 2 + (mouse_pos[1] - self.coord[1]) ** 2) < self.rad ** 2:      
            for i in range(len(self.dots)):
                self.norm_dots[i][0] += - self.coord[0] + mouse_pos[0]
                self.norm_dots[i][1] += - self.coord[1] + mouse_pos[1]
            self.coord = mouse_pos

    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    

            elif event.type == pg.MOUSEBUTTONUP:
                pass
        pressed = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        if pressed[0]:
            Figure.movement(self, mouse_pos)
        return done





class Match():
    pass


rocket1 = Schedule(1)
rocket2 = Schedule(2)
rocket3 = Schedule(3)
figure = Figure(dots=[[75, 75], [150, 0], [225, 75]])

while not done:
    clock.tick(30)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    rocket1.draw(screen,1)
    rocket2.draw(screen,2)
    rocket3.draw(screen,3)
    figure.handle_events(pg.event.get())
    figure.draw(screen)
    
    
pg.quit()