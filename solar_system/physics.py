# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:59:30 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint
import io_

G=6.67430*10**(-11)
alpha=10**11

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
COLORS = [LSALMON, PEACH, LEMONE, SKYBLUE, TOMATO, CADET, BROWN]

pg.init()



class Balls():
    def __init__(self):
        A = io_.take_info()
        self.A = A
        self.n = len(A)           
        self.colors = list([COLORS[randint(0, len(COLORS)-1)] for i in range(self.n)])
        self.mass = list([float((A[i][1])[0:len(A[i][1])-4]) for i in range(self.n)])
        self.rads = list([A[i][6] for i in range(self.n)])
        self.coordx = list([A[i][2] for i in range(self.n)])
        self.coordy = list([A[i][3] for i in range(self.n)])       
        self.velsx = list([A[i][4] for i in range(self.n)])
        self.velsy = list([A[i][5] for i in range(self.n)])
        self.vels=[]
        self.coords=[]
        for i in range(self.n):
            self.vels.append([float(self.velsx[i]), float(self.velsy[i])])
            self.coords.append([(float(self.coordx[i])), (float(self.coordy[i]))])
       
    def draw(self, screen):
        for i in range(self.n):
            pg.draw.circle(screen, self.colors[i], [int(np.around(self.coords[i][0])),int(np.around(self.coords[i][1]))], self.rads[i])

    def iterate(self, t):
        for i, ball in enumerate(self.coords):
            a=[0,0]
            for j in range(self.n):
                if j != i:
                    arctg = np.arctan((self.coords[j][0]-self.coords[i][0])/(self.coords[j][1]-self.coords[i][1]))
                    if self.coords[i][0]>self.coords[j][0]:
                        a[0] -= G*self.mass[j]*alpha*abs(np.sin(arctg))/((self.coords[i][0]-self.coords[j][0])**2+(self.coords[i][1]-self.coords[j][1])**2)
                    else:a[0] += G*self.mass[j]*alpha*abs(np.sin(arctg))/((self.coords[i][0]-self.coords[j][0])**2+(self.coords[i][1]-self.coords[j][1])**2)
                    if self.coords[i][1] > self.coords[j][1]:
                        a[1] -= G*self.mass[j]*alpha*abs(np.cos(arctg))/((self.coords[i][0]-self.coords[j][0])**2+(self.coords[i][1]-self.coords[j][1])**2)
                    else:a[1] += G*self.mass[j]*alpha*abs(np.cos(arctg))/((self.coords[i][0]-self.coords[j][0])**2+(self.coords[i][1]-self.coords[j][1])**2)
                    
                        
            self.rads[i] = int(self.rads[i])
            for k in range(2):
                self.coords[i][k] += self.vels[i][k]*t + 0.5*a[k]*t**2
                self.vels[i][k] += a[k]*t  
                self.A[i][4+k] = self.vels[i][k]
                self.A[i][2+k] = self.coords[i][k]
        A = self.A
        io_.save_info()
                
                
                 
        

pg.quit()