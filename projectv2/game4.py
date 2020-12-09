import pygame as pg
import numpy as np
from random import randint


SCREEN_SIZE = (1200, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pg.init()



class Ball():

    def __init__(self, coord=None):
        if coord==None:
            coord = (randint(0, 1200), randint(0, 600))
        self.coord = coord


    def draw(self, screen):
        fire_img = pg.image.load("fire.png")
        screen.blit(fire_img, (self.coord[0], self.coord[1]))

    def check(self, mouse_pos):
        if (self.coord[0]-mouse_pos[0])**2+(self.coord[1]-mouse_pos[1])**2 < 50*50:
            return 1

q=30*60*2
class Manager():
    def __init__(self, time=q):
        self.balls = []
        self.time = time

    def up_time(self):
        self.time -= 1
        if self.time % 30 == 0 and self.time > 60:
            self.new_aim()

    def print_time(self):
        a = (q - self.time) / q
        a = int(a * 1200)
        pg.draw.rect(screen, WHITE, (0, 10, a, 10))
        f1 = pg.font.Font(None, 36)
        text1 = f1.render('TIME YOU HAVE', 1, WHITE)
        screen.blit(text1, (500, 20))

    def new_aim(self):
       self.balls.append(Ball())

    def final_check(self):
        done = False
        if self.time == 0:
            if len(self.balls) == 0:
                print('afasdf')
            done = True
        return done


    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        self.up_time()
        self.print_time()
        if self.final_check() == True:
            done = True
        return done

    def draw(self, screen):
        SC = pg.image.load("menu.jpg")
        screen.blit(SC, (0,0))
        for ball in self.balls:
            ball.draw(screen)




    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pg.mouse.get_focused():
                        mouse_pos = pg.mouse.get_pos()
                        self.check_collide(mouse_pos)

        return done

    def check_collide(self, mouse_pos):
        for i, ball in enumerate(self.balls):
            if Ball.check(ball, mouse_pos) == 1:
                self.balls.pop(i)






screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Abacaba")
clock = pg.time.Clock()

mgr = Manager()

done = False

score = 0
'''
основное тело
'''
while not done:
    clock.tick(30)

    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()

pg.quit()
