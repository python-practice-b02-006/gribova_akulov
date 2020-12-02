# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:50:11 2020

@author: Nika
"""
import pygame as pg
import numpy as np
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


class Table():
    def __init__(self, t_destr=0, b_used=0):
        self.t_destr = t_destr
        self.b_used = b_used
        self.font = pg.font.SysFont("dejavusansmono", 25)

    def score(self):
        return self.t_destr - self.b_used
    
    def draw(self, screen):
        score_surf = []
        '''score_surf.append(self.font.render("Destroyed: {}".format(self.t_destr), True, TOMATO))
        score_surf.append(self.font.render("Balls used: {}".format(self.b_used), True, PEACH))
        score_surf.append(self.font.render("Total: {}".format(self.score()), True, PEACH))
        for i in range(3):
            screen.blit(score_surf[i], [10, 10 + 30*i])'''

class Ball():
    def __init__(self, coord, vel, rad=15, color=None):
        if color == None:
            color = COLORS[randint(0,len(COLORS)-1)]
        self.alive=True
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad

    def move(self, t_step=1, g=1):
        self.vel[1] += int(g * t_step)
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.wall()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SIZE[1] - 2*self.rad:
               self.alive = False

    def wall(self):
        n = [[1, 0], [0, 1]]
       
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i])
            elif self.coord[i] > SIZE[i] - self.rad:
                self.coord[i] = SIZE[i] - self.rad
                self.flip_vel(n[i])
       
    
    def flip_vel(self, axis, coef_perp=1, coef_par=1):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n #скалярное произведение массиввов
        vel_par = vel - vel_perp
        ans = -0.9*vel_perp + 0.93*vel_par
        self.vel = ans.astype(np.int).tolist()    
        if vel_perp.any()<0.001: self.alive=False
    
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)


class Gun():
    def __init__(self, coord=[SIZE[0]//2, SIZE[1]-50], minp=40):
        self.coord = coord
        self.angle = 0
        self.min_pow = minp
        self.power = minp
        self.active = False
    
    def draw(self, screen):
        gun_ = pg.image.load("gun.png").convert_alpha()
        gun = pg.transform.rotate(gun_, -180/np.pi*self.angle-90)
        screen.blit(gun,(self.coord[0]-29, self.coord[1]-26.5))
    
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])

    def spit(self):
        vel = [int(self.power * np.cos(self.angle)), 
               int(self.power * np.sin(self.angle))]
        return Ball(list(self.coord), vel)
    


class Target():
    def __init__(self, coord=None, color=None, r=80):
        if coord == None:
            coord = [randint(r//80, (SIZE[0] - r)//80), randint(r//80, (SIZE[1] - r)//80)]
        self.coord = coord
        self.r = r
        if color == None:
            color =SKYBLUE
            self.color = color

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.coord[0]*80, 80*self.coord[1], 80, 80))
        pg.draw.lines(screen, CADET, False, [(self.coord[0]*80, self.coord[1]*80), 
                                               (self.coord[0]*80+80, self.coord[1]*80),
                                               (self.coord[0]*80+80, self.coord[1]*80+80), 
                                               (self.coord[0]*80, self.coord[1]*80+80),
                                               (self.coord[0]*80, self.coord[1]*80)], 6)
    
    def check_collision(self, ball):
        dist = (sum([(80*(self.coord[i]+0.5) - ball.coord[i])**2 for i in range(2)]))**0.5
        min_dist = ball.rad+40
        return dist <= min_dist
        

class Manager():
    def __init__(self, n_targets):
        self.gun = Gun()
        self.score_t = Table()
        self.targets = []
        self.n_targets = n_targets
        self.balls = []   
        self.missions()    
        
    def move(self):
        for i in self.balls:
            i.move()
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move(g=3)
            if not ball.alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        
    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        self.move()
        self.collide()
        self.check_alive()
        if len(self.targets) == 0 and len(self.balls) == 0:
            self.missions()        
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        return done
        
    def draw(self, screen):
        screen.blit(SC_IMG, (0, 0))
        
        for i in self.balls:
            i.draw(screen)
        for target in self.targets:
            target.draw(screen)
        self.score_t.draw(screen)
        self.gun.draw(screen)
        
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 20
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 20
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.spit())
                    self.score_t.b_used += 1
                    
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        return done
    
    def check_alive(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)
   
    def missions(self):
        for i in range(self.n_targets):
            self.targets.append(Target(r=randint(max(1, 30 - 2*max(0, self.score_t.score())), 
                30 - max(0, self.score_t.score()))))
    
    def collide(self):
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
                    ball.flip_vel([1,0])
                    ball.flip_vel([0,1])                    
        targets_c.sort()
        for j in reversed(targets_c):
            self.score_t.t_destr += 1
            self.targets.pop(j)
        

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("game1")
clock = pg.time.Clock()

mgr = Manager(30)

done = False


SC_IMG = pg.image.load("space_forgame1.jpg")
screen.blit(SC_IMG, (0, 0))

while not done:
    clock.tick(100)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
    
    
pg.quit()