import pygame as pg
import numpy as np
from random import randint
WHITE = (255, 255, 255)
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
SCREEN_SIZE = (1200, 600)
screen = pg.display.set_mode(SCREEN_SIZE)
pg.init()

class Ball():
    def __init__(self, coords=None):
        if coords == None:
            coords = (randint(1200, 1700), randint(0, 600))
        self.coords = coords

    def draw(self):
        pg.draw.circle(screen, BLACK, (self.coords), 5)

    def move(self):
        self.coords[0] += 7

class Meteors():
    def __init__(self, coords=None):
        if coords==None:
            coords = (1240, randint(0, 600))
        self.ball_coords = coords

    def draw(self):
        pg.draw.circle(screen, BLACK, (self.ball_coords), 40)

    def move(self):
        self.ball_coords[0] -= 5

class Spaceship():
    def __init__(self, coords=[50, 300]):
        self.coords = coords
        self.crash = False

    def draw(self):
        pg.draw.circle(screen, BLACK, (self.coords), 10)
q=30*60*3
class Manager():
    def __init__(self):
        self.spaceship = Spaceship()
        self.meteors = []
        self.strikes = []
        self.up_key_pressed = False
        self.down_key_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.time = q
        self.crash = False

    def draw(self):
        SC = pg.image.load("space_forgame1.jpg")
        screen.blit(SC, (0, 0))
        self.spaceship.draw()
        for meteor in self.meteors:
            meteor.draw()
            meteor.move()
        for strike in self.strikes:
            strike.draw()
            strike.move()
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
                return done
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True
                    return done
                if event.key == pg.K_UP:
                    self.up_key_pressed = True
                elif event.key == pg.K_DOWN:
                    self.down_key_pressed = True
                elif event.key == pg.K_RIGHT:
                    self.right_key_pressed = True
                elif event.key == pg.K_LEFT:
                    self.left_key_pressed = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.up_key_pressed = False
                elif event.key == pg.K_DOWN:
                    self.down_key_pressed = False
                elif event.key == pg.K_RIGHT:
                    self.right_key_pressed = False
                elif event.key == pg.K_LEFT:
                    self.left_key_pressed = False
                elif event.key == pg.K_SPACE:
                    self.strike()

    def teleportation(self):
        if self.up_key_pressed == True:
            self.spaceship.coords[1] -= 3
            if self.spaceship.coords[1] < 10:
                self.spaceship.coords[1] = 10

        if self.down_key_pressed == True:
            self.spaceship.coords[1] += 3
            if self.spaceship.coords[1] > 590:
                self.spaceship.coords[1] = 590

        if self.left_key_pressed == True:
            self.spaceship.coords[0] -= 3
            if self.spaceship.coords[0] < 10:
                self.spaceship.coords[0] = 10

        if self.right_key_pressed == True:
            self.spaceship.coords[0] += 3
            if self.spaceship.coords[0] > 1190:
                self.spaceship.coords[0] = 1190

    def strike(self):
        self.strikes.append(Ball((self.spaceship.coords[0], self.spaceship.coords[1])))

    def timer(self):
        self.time -= 1
        if self.time % 10 == 0:
            self.meteors.append(Meteors())

    def kill(self):
        for i, ball in enumerate(self.strikes):
            for j, meteor in enumerate(self.meteors):
                if self.check(ball, meteor) == 1:
                    self.strikes.pop(i)
                    self.meteors.pop(j)
    def check(self, ball, meteor):
        if (ball.coord[0]-meteor.coord[0])**2 + (ball.coord[1]-meteor.coord[1])**2 < (40+3)**2:
            return 1

    def zepopa(self):
        for meteor in self.meteors:
            if (meteor.coord[0]-self.spaceship.coords[0])**2+(meteor.coord[1]-self.spaceship[1])**2<(40+30)**2:
                self.crash = True+


    def end(self):
        if self.time == 0 or self.crash==True:
            return 1

    def process(self, events):
        done = self.handle_events(events)
        self.draw()
        self.teleportation()
        self.timer()
        self.kill()
        self.zepopa()
        if self.end() == 1:
            done = True
        return done












done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(30)
    screen.fill(BLACK)

    done = mgr.process(pg.event.get())

    pg.display.update()
