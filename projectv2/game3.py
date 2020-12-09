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

class Spaceship():
    def __init__(self, coords=[550, 600], crash=False):
        self.coords = coords
        self.crash = crash

    def draw(self):
        pg.draw.circle(screen, BLACK, (self.coords), 10)

class Srtike():
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def draw(self):
        pg.draw.circle(screen, BLACK, (self.coord_x, self.coord_y), 3)

    def movement(self):
        self.coord_y -= 7

class Meteors():
    def __init__(self, coord):
        self.coord = coord

    def movement(self):
        self.coord[1] += 5

    def draw(self):
        pg.draw.circle(screen, GREY, (self.coord[0], self.coord[1]), self.coord[2])

    def check_collide(self, strikes):
        dist = (self.coord[0] - strikes.coord[0]) ** 2 + (self.coord[1] - strikes.coord[1]) ** 2
        mindist = (self.coord[2] + 3) ** 2
        if dist < mindist:
            return 1


class Manager():
    def __init__(self):
        self.up_key_pressed = False
        self.down_key_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.strike_active = False
        self.game_win = True

        self.spaceship = Spaceship()
        self.strikes = []
        self.meteors = []

    def draw(self):
        self.spaceship.draw()
        for meteors in self.meteors:
            Meteors.draw(meteors)
        for strikes in self.strikes:
            Srtike.draw(strikes)


    def create_meteors(self):
        for i in range(50):
            coord = [randint(0, 1200), randint(-500, 0), randint(20, 40)]
            self.meteors.append(coord)

    def movement(self):
        for meteors in self.meteors:
            Meteors.movement(meteors)
        for strikes in self.strikes:
            Srtike.movement(strikes)

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
                elif event.key == pg.K_SPACE:
                    self.strike_active  = True
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
                    self.strike_active = False


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

    def collide(self):
        for i in range(len(self.strikes)):
            for j in range (len(self.meteors)):
                if Meteors.check_collide(self.meteors[j], self.strikes[i]) == 1:
                    self.meteors.pop(j)
                    self.strikes.pop(i)


    def strike(self):
        if self.strike_active == True:
            self.strikes.append((self.spaceship.coords[0], self.spaceship.coords[1]))

    def back_bad(self):
        for i in range(len(self.meteors)):
            if self.meteors[1] > 600:
                done = True
                self.game_win = False
        return done, self.game_win

    def back_good(self):
        if len(self.meteors) == 0:
            done = True
            self.game_win=True
        return done, self.game_win

    def process(self, events):
        done = self.handle_events(events)
        screen.fill(WHITE)
        self.movement()
        self.draw()
        self.teleportation()
        self.collide()
        self.back_bad()
        self.back_good()
        return done

done = False
clock = pg.time.Clock()

mgr = Manager()
mgr.create_meteors()
while not done:
    clock.tick(60)
    screen.fill(BLACK)

    done = mgr.process(pg.event.get())

    pg.display.update()


pg.quit()