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
    return min(m_a+1, m_b+1, m_c+1)/1.5

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
                       [self.l+400 + 50, self.c+200 + 300], [self.l+400 + 100, self.c+200 + 250],
                       [self.l+400 + 150, self.c+200 +300], [self.l+400 + 200, self.c+200 +250],
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
            self.rad //= 1.5
        print(self.coord, self.rad)
        self.time = 1

    def convert_dots(self):
        for i in range(len(self.dots)):
            self.dots[i] = (self.norm_dots[i][0], self.norm_dots[i][1])
        return self.dots
    
    def draw(self, screen, this_figure):
        pg.draw.polygon(screen, self.color,  this_figure.convert_dots())

    def movement(self, mouse_pos):
        if ((mouse_pos[0] - self.coord[0]) ** 2 + (mouse_pos[1] - self.coord[1]) ** 2) < self.rad ** 2:      
            for i in range(len(self.dots)):
                self.norm_dots[i][0] += - self.coord[0] + mouse_pos[0]
                self.norm_dots[i][1] += - self.coord[1] + mouse_pos[1]
            self.coord = mouse_pos

    def handle_events(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    
            elif event.type == pg.MOUSEBUTTONUP:
                pass
        pressed = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        if pressed[0]:
            self.movement(mouse_pos)

class Match():
    def __init__():
        pass

class Manager():
    def __init__(self, figcoords):
        self.figures = []
        self.dots_figure = figcoords
        for i in range(len(self.dots_figure)):
            self.figures.append(Figure(dots=self.dots_figure[i]))
            
    def draw(self, screen):
        rocket1.draw(screen,1)
        rocket2.draw(screen,2)
        rocket3.draw(screen,3)
        screen.blit(SC_IMG, (0, 0))
        screen.blit(SC_IMG, (337, 0))
        screen.blit(SC_IMG, (674, 0))
        screen.blit(SC_IMG, (1011, 0))
        rocket1.draw(screen,1)
        rocket2.draw(screen,2)
        rocket3.draw(screen,3)
        for i in range(len(self.dots_figure)):
            self.figures[i].draw(screen, self.figures[i]) 
            
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        for i in range(len(self.dots_figure)):
            self.figures[i].handle_events(events)
        return done
        
dots_figure =[[[180, 588], [255, 513], [330, 588]],
              [[100, 569], [25, 519], [25, 569]],
              [[13, 392], [63, 517], [163, 392]],
              [[243, 371], [293, 496], [243, 496]],
              [[120, 496], [220, 496], [220, 371]],
              [[117, 512], [167, 512], [167, 562], [117, 562]],
              [[304, 556], [379, 506], [379, 456], [304, 506]],
              [[275, 402], (350, 402), (350, 452)],
              [[371, 118], [471, 118], [471, 18]],

              [[670, 162], [570, 162], [570, 62]],
              [[567, 177], [667, 177], [667, 277]],
              [[785, 176], [685, 176], [685, 276]],
              [[432, 197], [482, 222], [532, 172], [482, 122]],
              [[488, 19], [488, 94], [538, 44]],
              [[502, 112], [552, 162], [552, 62]],
              [[675, 86], [725, 36], [675, 36]],
              [[677, 107], [677, 157], [727, 157], [727, 57]],
              [[745, 111], [745, 11], [795, 86], [795, 161]],
                           
              [[1050, 465], [1150, 465], [1050, 565]],
              [[766, 577], [816, 527], [941, 527], [891, 577]],
              [[1049, 337], [1174, 337], [1174, 437], [1049, 437]],
              [[1169, 481], [1119, 531], [1119, 581], [1169, 581]],
              [[918, 418], [918, 393], [968, 343], [1043, 418]],
              [[1048, 225], [1048, 325], [1173, 325]],
              [[822, 321], [822, 396], [897, 346], [897, 321]],
              [[834, 420], [909, 370], [909, 495]],
              [[922, 464], [922, 439], [1022, 439], [1022, 589]]]
'''

[[[25, 465], [100, 390], [175, 465]], [[275, 485], [200, 435], [200, 485]],
               [[75, 75], [125, 200], [225,75]], [[75, 75], [125, 200], [75, 200]], 
               [[125, 200], [225, 200], [225,75]], [[125,200], [175,200], [175,250], [125, 250]],
               [[50, 300], [125, 250], [125,200], [50,250]],
               [[175, 250], [250, 250], [250,300]],
               
               [[450, 100], [550,100], [550,0]], [[650, 100], [550,100], [550,0]], 
               [[450, 100], [550,100], [550,200]], [[650, 100], [550,100], [550,200]],
               [[450, 225], [500, 250], [550, 200], [500, 150]],
               [[450,225], [450,300], [500, 250]], [[500,250], [550,300], [550, 200]],
               [[550, 300], [600,250], [550, 250]], [[550, 200], [550, 250], [600,250], [600,150]],
               [[600,250], [600,150], [650, 225], [650, 300]]] 
[[0 ,0], [100, 0], [0, 100]],
              [[50,50], [100, 0], [225, 0], [175, 50]],
              [[50,50], [175, 50], [175,150], [50, 150]],
              [[50, 50],[0, 100], [0,150], [50, 150]],
              [[175,75], [175, 50], [225, 0], [300, 75]],
              [[175, 75], [175, 175], [300, 175]],
              [[0, 150], [0, 225], [75, 175], [75, 150]],
              [[0, 225], [75, 175], [75,300]],
              [[75, 175], [75, 150], [175, 150], [175, 300]]]
'''





mgr = Manager(dots_figure)

rocket1 = Schedule(1)
rocket2 = Schedule(2)
rocket3 = Schedule(3)
#figure = Figure(dots=[[275, 485], [200, 435], [200, 485]])

while not done:
    clock.tick(30)
    mgr.draw(screen)
    done = mgr.handle_events(pg.event.get())
    pg.display.flip()
    
    
pg.quit()
