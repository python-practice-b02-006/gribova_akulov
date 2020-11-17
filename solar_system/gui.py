import numpy as np
import pygame as pg
from random import randint

LEMONE = (255, 250, 205)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pg.init()

class Button():
    def __init__(self, coord=[510, 620], color=BLACK):
        self.coord = coord
        self.color = color
        self.active = 0
        self.rad = 15
        self.time = 1

    def draw(self, screen):
        pg.draw.rect(screen, WHITE, (310, 600, 400, 40))
        pg.draw.circle(screen, self.color,  self.coord, self.rad)
        pg.draw.rect(screen, WHITE, (940, 0, 80, 50))
        f1 = pg.font.Font(None, 36)
        if self.active == 1:
            text1 = f1.render('идет', 1, BLACK)
        else:
            text1 = f1.render('пауза', 1, BLACK)
        screen.blit(text1, (945, 10))

    def movement(self, mouse_pos):
        if ((mouse_pos[0] - self.coord[0]) ** 2 + (mouse_pos[1] - self.coord[1]) ** 2) < self.rad ** 2:
            if mouse_pos[0] > 710:
                self.coord[0] = 710
            elif mouse_pos[0] < 310:
                self.coord[0] = 310
            else:
                self.coord[0] = mouse_pos[0]

    def time(self):
        if self.active == 0:
            self.time = 0
        else:
            self.time = 10 ** ((self.coord[0] - 510) / 200)



    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pg.mouse.get_pos()

                    if mouse_pos[0] > 940 and mouse_pos[1] < 50:
                        self.active += 1
                        self.active = self.active % 2
                        return


            elif event.type == pg.MOUSEBUTTONUP:
                pass
        pressed = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        if pressed[0]:
            Button.movement(self, mouse_pos)

        return done



