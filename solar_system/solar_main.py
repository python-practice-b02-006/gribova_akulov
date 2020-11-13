# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:59:30 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint
import body
import io
import physics
import gui

SIZE = (728, 410)
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

class Manager():
    def __init__(self):      
        """
        конструктор
        """
        pass

    def file_before(self, file_from):
        A = io.take_info()       
        """
        съедает и обрабатывает информацию из файла
        """

    def process(self):
        """
        итерируемый код: перемещение, обновление, цифер, рис, тык на кнопки
        """
        pass

    def move_obj(self):
        """
        метод перемещения всех планет и обновления их параметров
        """
        body.Body.move()

    def handle_events(self, events):
        gui.Button.handle_events()
                    
    
    def draw(self, screen):
        
        """
        отрисовка всех объектов на screen
        """
        body.Body.draw()
        gui.Button.draw()


screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Now it's my work")
clock = pg.time.Clock()

mgr = Manager()

done = False
FPS=20

while not done:
    screen.fill(BLACK)
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True 
    clock.tick(30)
    done = mgr.process(pg.event.get(), screen)
    io.save_info()
    pg.display.update()
    
    
pg.quit()