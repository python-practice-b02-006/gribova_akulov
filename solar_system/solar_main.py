# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:59:30 2020

@author: Nika
"""
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


clock = pg.time.Clock()
balls = physics.Balls()
screen = pg.display.set_mode((1020, 640))

FPS = 5
finished = False
while not finished:
    clock.tick(1000)
    for event in pg.event.get():   
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                finished = True
    screen.fill((125,125,125))
    balls.iterate(0.01)#Артём, чтобы формулы работали корректно, нужен очень маленький интервал времени. и они вполне работают при таком
    balls.draw(screen)
    pg.display.update()
    
    
pg.quit()