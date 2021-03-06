# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:50:11 2020

@author: Nika
"""
import pygame as pg
import numpy as np
from random import randint

SIZE = (1200, 600)
A = []
presents = [[100, 0], [550, 100], [1050, 150]]
s = len(presents)
B = []
l = True
number_pr = [0, 0, 0, 0]

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
        score_surf.append(self.font.render("Перемещайтесь вверх/вниз кнопками LEFT и RIGHT", True, TOMATO))
        score_surf.append(self.font.render("Получили дополнительные секунды {}".format(self.score()), True, PEACH))
        for i in range(2):
            screen.blit(score_surf[i], [10, 10 + 30*i])


class Ball():
    def __init__(self, coord, vel, rad=15, color=None):
        if color == None:
            color = COLORS[randint(0, len(COLORS)-1)]
        self.alive = True
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad

    def move(self, t_step=1, g=1):
        global k, A, s
        if self.coord[1] - A[1] < 25 or self.coord[0] - A[0] < 25:
            angle = [1, 1]
        else: 
            arctg = np.arctan((self.coord[0] - A[0])/(self.coord[1] - A[1]))        
            angle = [np.sin(arctg), np.cos(arctg)]
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
        vel_perp = vel.dot(n) * n
        #скалярное произведение массиввов
        vel_par = vel - vel_perp
        ans = -0.9*vel_perp + 0.93*vel_par
        self.vel = ans.astype(np.int).tolist()    
        if vel_perp.any() < 0.001:
            self.alive = False
    
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)


class Gun():
    def __init__(self, coord=[SIZE[0]//2, SIZE[1]-150], minp=50):
        global A
        self.coord = coord
        self.angle = 0
        self.min_pow = minp
        self.power = minp
        self.active = False
        A = self.coord

    
    def draw(self, screen):
        gun_ = pg.image.load("gun.png").convert_alpha()
        gun = pg.transform.rotate(gun_, -180/np.pi*self.angle-90)
        screen.blit(gun, (self.coord[0]-29, self.coord[1]-26.5))
    
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])

    def spit(self):
        vel = [int(self.power * np.cos(self.angle)), 
               int(self.power * np.sin(self.angle))]
        return Ball(list(self.coord), vel)


class Target():
    def __init__(self, screen, coord=None, color=None, r=50):
        if coord == None:
            coord = [randint(r//50, (SIZE[0] - r)//50), randint(r//50, (SIZE[1] - 10*r)//50)]
        self.coord = coord
        self.r = r
        if color == None:
            color =SKYBLUE
            self.color = color
        else: self.color = TOMATO
        self.screen = screen
        self.vidno = 0

    def draw(self, screen):
        global l
        self.vidno += 1
        pg.draw.rect(screen, self.color, (self.coord[0]*50, 50*self.coord[1], 50, 50))
        pg.draw.lines(screen, CADET, False, [(self.coord[0]*50, self.coord[1]*50), 
                                               (self.coord[0]*50+50, self.coord[1]*50),
                                               (self.coord[0]*50+50, self.coord[1]*50+50), 
                                               (self.coord[0]*50, self.coord[1]*50+50),
                                               (self.coord[0]*50, self.coord[1]*50)], 6)
    
    def check_collision(self, ball):
        dist = (sum([(50*(self.coord[i]+0.5) - ball.coord[i])**2 for i in range(2)]))**0.5
        min_dist = ball.rad+25
        return dist <= min_dist
    
    def move_present(self, t_step=0.002):
        speed = 1
        global B, l
        money = pg.image.load("timeismoney.png").convert_alpha()
        for i in range(len(B)):
            if 50*B[i][1] < 400:
                self.screen.blit(money, (50*B[i][0], 50*B[i][1]))
            B[i][1] += speed*t_step
            

class Manager():
    def __init__(self, n_targets, screen):
        self.gun = Gun()
        self.score_t = Table()
        self.targets = []
        self.n_targets = n_targets
        self.balls = []   
        self.missions(screen)    
        self.screen = screen
        
    def move(self):
        global B
        for i in self.balls:
            i.move()
        dead_balls = []
        for i, target in enumerate(self.targets):
            target.move_present()
        for i, ball in enumerate(self.balls):
            ball.move(g=3)
            if not ball.alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        
    def process(self, events, screen):
        done1 = self.handle_events(events)
        done2= False
        self.draw(screen)
        self.move()
        self.collide()
        self.check_alive()
        if len(self.targets) == 0 and len(self.balls) == 0:
            done1 = True
            #self.missions(screen)
        if len(self.targets) == 0:
            done2 = True
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        return done1, done2
        
    def draw(self, screen):
        screen.blit(SC_IMG, (0, 0))
        screen.blit(SC_IMG, (0, 0))
        pg.draw.line(screen, TOMATO, (200, 450), (300, 450), 4)
        pg.draw.line(screen, TOMATO, (1000, 450), (900, 450), 4)
        pg.draw.lines(screen, TOMATO, False, [[220, 430], [200, 450], [220, 470]], 4)
        pg.draw.lines(screen, TOMATO, False, [[980, 430], [1000, 450], [980, 470]], 4)
        
        for i in self.balls:
            i.draw(screen)
        for target in self.targets:
            target.draw(screen)
        self.score_t.draw(screen)
        self.gun.draw(screen)
        
    def handle_events(self, events):
        done1 = False
        for event in events:
            if event.type == pg.QUIT:
                done1 = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.gun.coord[0] -= 40
                elif event.key == pg.K_RIGHT:
                    self.gun.coord[0] += 40
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
        return done1
    
    def check_alive(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)
   
    def missions(self, screen):
        global presents
        for i in range(self.n_targets):
            self.targets.append(Target(screen, r=randint(max(1, abs(30 - 2*max(0, self.score_t.score()))), 
                abs(30 - max(0, self.score_t.score())))))
        for i in range(len(presents)):
            self.targets.append(Target(screen, coord=[presents[i][0]//50, presents[i][1]//50], color=TOMATO))
    
    def collide(self):
        collisions = []
        targets_c = []
        global s, B, number_pr
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
                    ball.flip_vel([1, 0])
                    ball.flip_vel([0, 1]) 
        targets_c.sort()
        for j in reversed(targets_c):   
            l = True
            if j >= len(self.targets) - s: 
                if number_pr[3-s] == 24: 
                    s -= 1
                    B.append(self.targets[j].coord)
                    self.score_t.t_destr += 15
                    self.targets.pop(j)
                l = False
                number_pr[3-s] += 1
            if l == True or number_pr[3-s] == 25:
                self.targets.pop(j)
                self.score_t.t_destr += 1
        
'''
#screen = pg.display.set_mode(SIZE)
#pg.display.set_caption("game1")
#clock = pg.time.Clock()

#mgr = Manager(30)
'''
done1 = False

SC_IMG = pg.image.load("space_forgame1.jpg")

'''
while not done:
    clock.tick(120)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
    '''
