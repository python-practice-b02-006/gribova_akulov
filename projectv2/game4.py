import pygame as pg
import numpy as np
from random import randint


SCREEN_SIZE = (1200, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pg.init()


class Ball():
    '''
    класс огоньков, отвечает за их отрисовку, проверяет попал ли игрок в них
    '''
    def __init__(self, coord=None):
        '''
        в случае если у точки нет кординаты, она генерируется случайно за исклбчением зоны,
        где нет приборной панели
        '''
        if coord == None:
            coord1 = [randint(50, 1150), randint(50, 550)]
            
            if 300 < coord1[1] < 450:
                coord1[1] += 130
            if 220 < coord1[1] <= 300:
                coord1[1] -= 150   
            coord = (coord1[0], coord1[1])
        self.coord = coord

    def draw(self, screen):
        '''
        вставляет картинку огня в точку с кординатами данного объекта
        '''
        fire_img = pg.image.load("fire.png").convert_alpha()
        screen.blit(fire_img, (self.coord[0], self.coord[1]))

    def check(self, mouse_pos):
        '''
        получает на вход координаты мыши
        сравнивает расстояние между положением мыши и центром данного огонька
        если они меньше фиксированного числа возращает, что огонь потушен
        '''
        if (self.coord[0]+15-mouse_pos[0])**2+(self.coord[1]+15-mouse_pos[1])**2 < 50*60:
            return 1


q = 15 * 60


class Manager():
    def __init__(self, screen, time=30*60):
        self.balls = []
        self.time = time
        self.screen = screen
        self.done = 0

    def up_time(self):
        '''
        отвечает за генерацию огонька в зависимотсти от остатка числа при делении на 20
        за 5 секунд до конца игры перестает генерировать огни
        '''
        self.time -= 1
        if self.time % 20 == 0 and self.time > 60:
            self.new_aim()

    def print_time(self):
        '''
        отвечате за отрисовку времени
        '''
        a = (30*60 - self.time) / q
        a = int(a * 600)
        pg.draw.rect(self.screen, WHITE, (0, 10, a, 10))
        f1 = pg.font.Font(None, 36)
        text1 = f1.render('TIME YOU HAVE', 1, WHITE)
        self.screen.blit(text1, (500, 20))

    def new_aim(self):
        '''
        добавляет в массив шаров новый элемент
        '''
        self.balls.append(Ball())

    def final_check(self):
        '''
        проверят в момент конца игры, что игрок потушил все пожары
        '''
        done = False
        if self.time == 0:
            if len(self.balls) == 0:
                self.done = 1
            done = True
        return done

    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        self.up_time()
        self.print_time()
        self.final_check()
        if self.final_check() == True:
           done = True
        return done, self.done

    def draw(self, screen):
        '''
        проходя по массиву с огоньков отрисовывает их
        '''
        SC = pg.image.load("menu.jpg")
        screen.blit(SC, (0, 0))
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
        '''
        получает кординаты мыщи
        если при проверке оказывается, что пожар потушен, то удаляет из массива огоньков данный огонек
        '''
        for i, ball in enumerate(self.balls):
            if Ball.check(ball, mouse_pos) == 1:
                self.balls.pop(i)


done = False

score = 0
