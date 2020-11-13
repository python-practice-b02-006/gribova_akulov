# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:59:30 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint


BLACK = (0, 0, 0)
LSALMON = (255, 160, 122)
PEACH = (255, 218, 185)
LEMONE = (255, 250, 205)
SKYBLUE = (100, 149, 237)
TOMATO = (255, 99, 71)

pg.init()

class Button():
    def __init__(self, coord, rect, caption, color=None):
        self.coord = coord
        self.rect = rect
        self.caption = caption
        if color == None:
            color = TOMATO
            
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                pass
    def draw():
        pass

