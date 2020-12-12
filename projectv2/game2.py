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
b = ['ne_zanyato']

dots_figure = [[[180, 588], [255, 513], [330, 588]],
              [[100, 569], [25, 519], [25, 569]],
              [[13, 392], [63, 517], [163, 392]],
              [[243, 371], [293, 496], [243, 496]],
              [[120, 496], [220, 496], [220, 371]],
              [[117, 512], [167, 512], [167, 562], [117, 562]],
              [[304, 556], [379, 506], [379, 456], [304, 506]],
              [[275, 402], [350, 402], [350, 452]],
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
A = [[0, 0]]*len(dots_figure)

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
MICRO2 = (0, 128, 128)
MICRO1 = (20, 20, 112)
COLORS = [LSALMON, PEACH, LEMONE, SKYBLUE, TOMATO, GREY, CADET, BROWN]

pg.init()
pg.font.init()


font_1 = pg.font.SysFont("serif", 60)

clock = pg.time.Clock()

done2 = False


SC_IMG = pg.image.load("night_forest.jpg")


class Schedule():
    def __init__(self, number, left_side=50, ceiling=50, color=None):
        self.l = left_side
        if color == None:
            self.color = COLORS[randint(0, len(COLORS)-1)]
        self.c = ceiling
        self.coord = [[[self.l + 150, self.c], [self.l + 75, self.c + 75],
                       [self.l + 75, self.c + 200], [self.l + 125, self.c + 200],
                       [self.l + 50, self.c + 250], [self.l + 50, self.c + 300],
                       [self.l + 125, self.c + 250], [self.l + 175, self.c + 250],
                       [self.l + 250, self.c + 300], [self.l + 250, self.c + 250],
                       [self.l + 175, self.c + 200], [self.l + 225, self.c + 200],
                       [self.l + 225, self.c + 75], [self.l + 150, self.c]],
                      [[self.l + 400 + 150, self.c + 200], [self.l+400 + 50, self.c+200 + 100],
                       [self.l + 400 + 100, self.c + 200 + 150], [self.l + 400 + 50, self.c + 200 + 225],
                       [self.l + 400 + 50, self.c + 200 + 300], [self.l + 400 + 100, self.c + 200 + 250],
                       [self.l + 400 + 150, self.c + 200 + 300], [self.l + 400 + 200, self.c + 200 + 250],
                       [self.l + 400 + 250, self.c + 200 + 300], [self.l + 400 + 250, self.c + 200 + 225],
                       [self.l + 400 + 200, self.c + 200 + 150], [self.l + 400 + 250, self.c + 200 + 100],
                       [self.l + 400 + 150, self.c + 200]],
                      [[self.l + 800 + 225, self.c + 0], [self.l+800 + 0, self.c + 0],
                       [self.l + 800 + 0, self.c + 225], [self.l+800 + 75, self.c + 300],
                       [self.l + 800 + 75, self.c + 175], [self.l+800 + 175, self.c + 300],
                       [self.l + 800 + 175, self.c + 175], [self.l+800 + 300, self.c + 175],
                       [self.l + 800 + 175, self.c + 75], [self.l+800 + 300, self.c + 75],
                       [self.l + 800 + 225, self.c + 0]]]
    
    def draw(self, screen, n):
        pg.draw.lines(screen, self.color, False, self.coord[n-1], 5)


class Figure():
    def __init__(self, dots, color=None):
        self.norm_dots = dots
        self.coord = [0, 0]
        self.dots = [0]*len(dots)
        for i in range(len(dots)):
            self.coord[0] += int(dots[i][0]/len(dots))
            self.coord[1] += int(dots[i][1]/len(dots))
            self.dots[i] = (dots[i][0], dots[i][1])
        self.color = COLORS[randint(0, len(COLORS)-1)]
        self.active = 0
        if len(dots) == 3:
            self.rad = mediana(np.sqrt((dots[0][0]-dots[1][0])**2+(dots[0][1]-dots[1][1])**2),
                               np.sqrt((dots[0][0]-dots[2][0])**2+(dots[0][1]-dots[2][1])**2),
                               np.sqrt((dots[2][0]-dots[1][0])**2+(dots[2][1]-dots[1][1])**2))
        if len(dots) == 4:
            self.rad = int(min(np.sqrt((dots[3][0]-dots[1][0])**2+(dots[1][1]-dots[3][1])**2),
                           np.sqrt((dots[0][0]-dots[2][0])**2+(dots[0][1]-dots[2][1])**2)))
            self.rad //= 1.41
        self.time = 1

    def convert_dots(self):
        for i in range(len(self.dots)):
            self.dots[i] = (self.norm_dots[i][0], self.norm_dots[i][1])
        return self.dots
    
    def draw(self, screen, this_figure):
        pg.draw.polygon(screen, self.color,  this_figure.convert_dots())

    def movement(self, mouse_pos, k):
        global b, A
        if ((mouse_pos[0] - self.coord[0]) ** 2 + (mouse_pos[1] - self.coord[1]) ** 2) < self.rad ** 2:      
            if b == ['ne_zanyato']:
                b = [k]
            elif len(b) != 1:
                b.pop()
            elif b[0] != k: 
                b.append(k)
            if b[0] == k: 
                for i in range(len(self.dots)):
                    self.norm_dots[i][0] += - self.coord[0] + mouse_pos[0]
                    self.norm_dots[i][1] += - self.coord[1] + mouse_pos[1]
                self.coord = mouse_pos
                A[k] = self.coord

    def handle_events(self, events, k):
        global b
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                b = ['ne_zanyato']
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pg.mouse.get_pos()

        pressed = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        if pressed[0]:
            self.movement(mouse_pos, k)          


def match(centers_match, k):
    global A
    z = [0, 0, 0]
    for i in range(len(centers_match)):
        if len(centers_match) == 8:
            if (centers_match[i][0] - A[i][0])**2 + (centers_match[i][1] - A[i][1])**2 < 200:
                z[0] += 1
        if len(centers_match) == 10:
            if (centers_match[i][0] - A[8+i][0])**2 + (centers_match[i][1] - A[8+i][1])**2 < 200:
                z[1] += 1
        if len(centers_match) == 9:
            if (centers_match[i][0] - A[18+i][0])**2 + (centers_match[i][1] - A[18+i][1])**2 < 200:
                z[2] += 1
    if z[k] == len(centers_match):
        return True
    else:
        return False


class Manager():
    def __init__(self, figcoords, screen):
        self.figures = []
        self.l = 50
        self.c = 50
        self.done2 = False
        self.dots_figure = figcoords
        self.screen = screen
        for i in range(len(self.dots_figure)):
            self.figures.append(Figure(dots=self.dots_figure[i]))
        self.done3 = False
            
    def draw(self, screen, centers_match):
        screen.blit(SC_IMG, (0, 0))
        screen.blit(SC_IMG, (337, 0))
        screen.blit(SC_IMG, (674, 0))
        screen.blit(SC_IMG, (1011, 0))
        rocket1.draw(screen, 1)
        rocket2.draw(screen, 2)
        rocket3.draw(screen, 3)
        screen.blit(SC_IMG, (0, 0))
        screen.blit(SC_IMG, (337, 0))
        screen.blit(SC_IMG, (674, 0))
        screen.blit(SC_IMG, (1011, 0))
        rocket1.draw(screen, 1)
        rocket2.draw(screen, 2)
        rocket3.draw(screen, 3)
        for i in range(len(self.dots_figure)):
            self.figures[i].draw(screen, self.figures[i])
        exit_if_i_need_it = [0, 0, 0]
        for i in range(len(centers_match)):
            if match(centers_match[i], i):
                if i == 0:
                    surf1 = font_1.render("GREAT!", False, GREY)
                    screen.blit(surf1, (100, 450))
                    pg.draw.polygon(screen, MICRO1, [(self.l + 150, self.c), (self.l + 75, self.c + 75),
                       (self.l + 75, self.c + 200), (self.l + 125, self.c + 200),
                       (self.l + 50, self.c + 250), (self.l + 50, self.c + 300),
                       (self.l + 125, self.c + 250), (self.l + 175, self.c + 250),
                       (self.l + 250, self.c + 300), (self.l + 250, self.c + 250),
                       (self.l + 175, self.c + 200), (self.l + 225, self.c + 200),
                       (self.l + 225, self.c + 75), (self.l + 150, self.c)])
                    pg.draw.lines(screen, MICRO2, False, [[30, 155], [170, 155], [210, 190], [330, 190]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[30, 194], [185, 194], [185, 80], [330, 80]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[30, 235], [200, 235], [200, 155], [330, 155]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[30, 275], [200, 275], [200, 320], [330, 320]], 3)                    
                    exit_if_i_need_it[0] = 1
                    pg.draw.circle(screen, MICRO1, [330, 320], 5)
                    pg.draw.circle(screen, MICRO1, [30, 155], 5)
                    pg.draw.circle(screen, MICRO1, [30, 235], 5)
                    pg.draw.circle(screen, MICRO1, [30, 194], 5)
                    pg.draw.circle(screen, MICRO1, [30, 275], 5)
                    pg.draw.circle(screen, MICRO1, [330, 190], 5)
                    pg.draw.circle(screen, MICRO1, [330, 155], 5)
                    pg.draw.circle(screen, MICRO1, [330, 80], 5)
                if i == 1:
                    surf2 = font_1.render("AWESOME!!", False, GREY)              
                    screen.blit(surf2, (450, 140))
                    exit_if_i_need_it[1] = 1
                    pg.draw.polygon(screen, MICRO1, [(self.l + 400 + 150, self.c + 200), (self.l+400 + 50, self.c+200 + 100),
                       (self.l + 400 + 100, self.c + 200 + 150), (self.l + 400 + 50, self.c + 200 + 225),
                       (self.l + 400 + 50, self.c + 200 + 300), (self.l + 400 + 100, self.c + 200 + 250),
                       (self.l + 400 + 150, self.c + 200 + 300), (self.l + 400 + 200, self.c + 200 + 250),
                       (self.l + 400 + 250, self.c + 200 + 300), (self.l + 400 + 250, self.c + 200 + 225),
                       (self.l + 400 + 200, self.c + 200 + 150), (self.l + 400 + 250, self.c + 200 + 100),
                       (self.l + 400 + 150, self.c + 200)])
                    pg.draw.lines(screen, MICRO2, False, [[420, 350], [560, 350], [560, 425], [480, 545], [480, 580]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[450+136, 220], [450+136, 450], [522, 545], [522, 580]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[450+163, 220], [450+163, 450], [676, 545], [676, 580]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[780, 350], [640, 350], [640, 425], [720, 545], [720, 580]], 3)  
                    pg.draw.circle(screen, MICRO1, [420, 350], 5)
                    pg.draw.circle(screen, MICRO1, [450+136, 220], 5)
                    pg.draw.circle(screen, MICRO1, [450+163, 220], 5)
                    pg.draw.circle(screen, MICRO1, [480, 580], 5)
                    pg.draw.circle(screen, MICRO1, [780, 350], 5)
                    pg.draw.circle(screen, MICRO1, [522, 580], 5)
                    pg.draw.circle(screen, MICRO1, [676, 580], 5)
                    pg.draw.circle(screen, MICRO1, [720, 580], 5)
                if i == 2:
                    surf3 = font_1.render("EXCITING!", False, GREY)
                    screen.blit(surf3, (850, 450))
                    exit_if_i_need_it[2] = 1
                    pg.draw.polygon(screen, MICRO1, [(self.l + 800 + 225, self.c + 0), (self.l+800 + 0, self.c + 0),
                       (self.l + 800 + 0, self.c + 225), (self.l+800 + 75, self.c + 300),
                       (self.l + 800 + 75, self.c + 175), (self.l+800 + 175, self.c + 300),
                       (self.l + 800 + 175, self.c + 175), (self.l+800 + 300, self.c + 175),
                       (self.l + 800 + 175, self.c + 75), (self.l+800 + 300, self.c + 75),
                       (self.l + 800 + 225, self.c + 0)])
                    pg.draw.lines(screen, MICRO2, False, [[820, 150], [950, 150], [950, 20]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[820, 200], [1000, 200], [1000, 20]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[910, 380], [910, 110], [1180, 110]], 3)
                    pg.draw.lines(screen, MICRO2, False, [[960, 380], [960, 160], [1180, 160]], 3)  
                    pg.draw.circle(screen, MICRO1, [820, 150], 5)
                    pg.draw.circle(screen, MICRO1, [820, 200], 5)
                    pg.draw.circle(screen, MICRO1, [910, 380], 5)
                    pg.draw.circle(screen, MICRO1, [960, 380], 5)
                    pg.draw.circle(screen, MICRO1, [950, 20], 5)
                    pg.draw.circle(screen, MICRO1, [1000, 20], 5)
                    pg.draw.circle(screen, MICRO1, [1180, 110], 5)
                    pg.draw.circle(screen, MICRO1, [1180, 160], 5)
        if exit_if_i_need_it == [1, 1, 1]:
            self.done2 = True
            self.done3 = True
            
    def handle_events(self, events):
        done2 = False
        for event in events:
            if event.type == pg.QUIT:
                self.done2 = True
        for i in range(len(self.dots_figure)):
            self.figures[i].handle_events(events, i)
            
        return self.done2, self.done3


centers_match = [[[199, 99], [249, 280], [191, 164], [140, 205], [241, 206],
                 [197, 273],  [136, 297], [277, 318]],

                 [[564, 317], [632, 315], [565, 380], [633, 379], [548, 453], 
                  [516, 506], [581, 498], [614, 517], [622, 462], [674, 481]],
                 
                 [[882, 82], [986, 74], [961, 150], [871, 160], [1067, 99],
                  [1065, 190], [887, 223], [899, 281], [974, 244]]]


rocket1 = Schedule(1)
rocket2 = Schedule(2)
rocket3 = Schedule(3)
