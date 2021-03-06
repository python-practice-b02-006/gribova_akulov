# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:39:57 2020

@author: Nika
"""
import numpy as np
import os
import pygame as pg
from random import randint
import cv2

pg.init()
SIZE = (1020, 600)
A=[]




pg.mixer.music.load('start_music.mp3')
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play()

stream = 'start2.avi'

# open stream
cap = cv2.VideoCapture(stream)
ret, img = cap.read()


img = cv2.transpose(img)

print('shape:', img.shape)

pg.init()

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

pg.mixer.music.load('adventure_music.mp3')
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play()

class Walls(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image("amongus2.jpg", -1)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pg.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = 563


class Touch(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = load_image("button.jpg", -1)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self,events):
        # если ещё в небе
        global running
        if not pg.sprite.collide_mask(self, wall):
            for event in events:
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.rect = self.rect.move(0, -8)
                    elif event.key == pg.K_DOWN:
                        self.rect = self.rect.move(0, 8)
                    elif event.key == pg.K_RIGHT:
                        self.rect = self.rect.move(8, 0)
                    elif event.key == pg.K_LEFT:
                        self.rect = self.rect.move(-8, 0)
            


def main():
    pg.init()
    screen = pg.display.set_mode(SIZE)
    SC_IMG = pg.image.load("amongus.jpg")
    screen.blit(SC_IMG, (0, 0))

    global all_sprites, wall
    all_sprites = pg.sprite.Group()
    wall = Walls()

    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pg.MOUSEBUTTONDOWN:
                Touch(event.pos)

        SC_IMG = pg.image.load("amongus.jpg")
        screen.blit(SC_IMG, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update(pg.event.get())

        pg.display.flip()
        clock.tick(20)

    pg.quit()


def load_image(name, colorkey=None):
    fullname = os.path.join(os.path.dirname(__file__), name)
    image = pg.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    main()

pg.quit()