import pygame as pg
import numpy as np
from random import randint
import cv2

SCREEN_SIZE = (1200, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
RED = (255, 0, 0)
YELLOW = (128, 0, 0)
BROWN = (160, 82, 45) #150, 75, 0


screen = pg.display.set_mode(SCREEN_SIZE)
pg.init()
seq = 120 * 60 * 10

'''
pg.mixer.music.load('start_music.mp3')
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play()
stream = 'start2.avi'
# open stream
cap = cv2.VideoCapture(stream)
ret, img = cap.read()
img = cv2.transpose(img)
print('shape:', img.shape)
# create window with the same size as frame
screen = pg.display.set_mode((img.shape[0], img.shape[1]))
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # read one frame and check if there was no problem
    ret, img = cap.read()
    if not ret:
        running = False
        break
    else:
        img = cv2.transpose(img)
        pg.surfarray.blit_array(screen, img)
    pg.display.flip()
'''



pg.mixer.music.load('adventure_music.mp3')
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play()


class Timer():
    def __init__(self, time=seq):
        self.time = time

    def draw(self):
        a = (seq - self.time)/seq
        a = int(a * 1200)
        pg.draw.rect(screen, RED, (0, 10, a, 10))
        f1 = pg.font.Font(None, 36)
        text1 = f1.render('TIME YOU HAVE', 1, RED)
        screen.blit(text1, (500, 20))

    def change(self):
        self.time -= 1

    def end(self):
        if self.time <= 0:
            screen.fill(BLACK)


class Map():
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pg.draw.rect(self.screen, BROWN, (-100, -100, 1500, 800))

        pg.draw.rect(self.screen, GRAY, (100, 500, 1100, 100))
        pg.draw.rect(self.screen, GRAY, (300, 300, 200, 100))
        pg.draw.rect(self.screen, GRAY, (600, 100, 100, 500))
        pg.draw.rect(self.screen, GRAY, (800, 100, 100, 500))
        pg.draw.rect(self.screen, GRAY, (0, 100, 100, 300))
        pg.draw.rect(self.screen, GRAY, (100, 100, 200, 100))
        pg.draw.rect(self.screen, GRAY, (200, 200, 100, 300))
        pg.draw.rect(self.screen, GRAY, (400, 100, 200, 100))
        pg.draw.rect(self.screen, GRAY, (1100, 300, 100, 200))
        pg.draw.rect(self.screen, GRAY, (1000, 300, 100, 100))
        pg.draw.circle(self.screen, YELLOW, (50, 350), 20)
        pg.draw.circle(self.screen, YELLOW, (450, 350), 20)
        pg.draw.circle(self.screen, YELLOW, (450, 150), 20)
        pg.draw.circle(self.screen, YELLOW, (850, 150), 20)
        pg.draw.circle(self.screen, YELLOW, (1050, 350), 20)
        pg.draw.rect(self.screen, BROWN, (0, 0, 4, 600))
        pg.draw.rect(self.screen, BROWN, (0, 596, 1200, 4))
        pg.draw.rect(self.screen, BROWN, (1196, 0, 4, 600))

class Hero():
    def __init__(self, coord=[150, 550]):
        self.coord = coord

    def draw(self, screen):
        pg.draw.circle(screen, BLACK, (self.coord[0], self.coord[1]), 10)

    def night(self):
        pg.draw.polygon(screen, BLACK, [[0 , 0], [self.coord[0] - 40, self.coord[1] - 40],
                                        [self.coord[0] - 40, self.coord[1] + 40], [0, 600]])
        pg.draw.polygon(screen, BLACK, [[0, 600], [self.coord[0] - 40, self.coord[1] + 40],
                                        [self.coord[0] + 40, self.coord[1] + 40], [1200, 600]])
        pg.draw.polygon(screen, BLACK, [[1200, 600], [self.coord[0] + 40, self.coord[1] + 40],
                                        [self.coord[0] + 40, self.coord[1] - 40], [1200, 0]])
        pg.draw.polygon(screen, BLACK, [[1200, 0], [self.coord[0] + 40, self.coord[1] - 40],
                                        [self.coord[0] - 40, self.coord[1] - 40], [0, 0]])

class Manager():
    def __init__(self):
        self.hero = Hero()
        self.time = Timer()
        self.map = Map(screen)
        self.up_key_pressed = False
        self.down_key_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False

    def process(self, events, screen):
        done = self.handle_events(events)
        self.map.draw()
        self.hero.draw(screen)
        self.time.change()
        self.teleportation()
        self.hero.night()
        self.time.draw()
        self.time.end()
        return done

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


    def teleportation(self):
        if self.up_key_pressed:
            if screen.get_at((self.hero.coord[0], self.hero.coord[1] - 11)) == GRAY or \
                    screen.get_at((self.hero.coord[0], self.hero.coord[1] - 11)) == YELLOW:
                self.hero.coord[1] -= 1
        if self.down_key_pressed:
            if screen.get_at((self.hero.coord[0], self.hero.coord[1] + 11)) == GRAY or\
                    screen.get_at((self.hero.coord[0], self.hero.coord[1] + 11)) == YELLOW:
                self.hero.coord[1] += 1
        if self.left_key_pressed:
            if screen.get_at((self.hero.coord[0] - 11, self.hero.coord[1])) == GRAY or \
                    screen.get_at((self.hero.coord[0] - 11, self.hero.coord[1])) == YELLOW:
                self.hero.coord[0] -= 1
        if self.right_key_pressed:
            if screen.get_at((self.hero.coord[0] + 11, self.hero.coord[1])) == GRAY or\
                    screen.get_at((self.hero.coord[0] + 11, self.hero.coord[1])) == YELLOW:
                self.hero.coord[0] += 1




pg.display.set_caption("The gun of Abacaba")
clock = pg.time.Clock()

done = False
mgr = Manager()

while not done:
    clock.tick(120)
    done = mgr.process(pg.event.get(), screen)
    pg.display.update()

pg.quit()