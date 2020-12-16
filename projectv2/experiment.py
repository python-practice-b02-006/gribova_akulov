import pygame as pg
import numpy as np
from random import randint

'''
набор констант 
'''

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


pg.init()
'''
дале идут 3 функции, каждая из которых создает объект определенного типа и возвращает его координаты
new_ball - выстрелы
new_meteor - метеориты
new_spaceship - корабль
'''

def new_ball(x, y):
    return {
        'x': x,
        'y': y,
    }


def new_meteor():
    return {
        'x': 1240,
        'y': randint(40, 640),
    }


def new_spaceship():
    return {
        'x': 40,
        'y': 300,
    }


a = new_spaceship()
q = 30 * 60 * 3


class Manager():
    def __init__(self, screen):
        self.meteors = []
        self.strikes = []
        self.up_key_pressed = False
        self.down_key_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.time = q
        self.crash = False
        self.calculate = 0
        self.win = 0
        self.lost = 0
        self.screen = screen

    def draw(self):
        '''
        функция отрисовки, сначала отрисовывает корабль, затем отрисовывает пули и метеориты, проходя циклом
        по каждому элементу
        '''
        SC = pg.image.load("space_forgame3.jpg")
        self.screen.blit(SC, (0, 0))
        for unit in self.meteors:
            unit['x'] -= 12
            SC1 = pg.image.load("qquop.png")
            self.screen.blit(SC1, (unit['x'], unit['y']))
        for unit in self.strikes:
            pg.draw.circle(self.screen, WHITE, (unit['x'], unit['y']), 3)
            unit['x'] += 15
        SC1 = pg.image.load("spaceship.png")
        self.screen.blit(SC1, (a['x'], a['y']))

    def handle_events(self, events):
        '''
        считывает нажатия и зажатия клавиш, передает это программе
        '''
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
        '''
        если какая-то из клавиш движения зажата, то корабль начинает перемещаться в данном направлении
        '''
        if self.up_key_pressed == True:
            a['y'] -= 8
            if a['y'] < 30:
                a['y'] = 30

        if self.down_key_pressed == True:
            a['y'] += 8
            if a['y'] > 570:
                a['y'] = 570

        if self.left_key_pressed == True:
            a['x'] -= 8
            if a['x'] < 30:
                a['x'] = 30

        if self.right_key_pressed == True:
            a['x'] += 8
            if a['x'] > 1170:
                a['x'] = 1170

    def strike(self):
        '''
        в случае если нажат пробел созлает объект типа пуля в точке с кординатами корабля
        '''
        self.strikes.append(new_ball(a['x'], a['y']+15))

    def lose(self):
        '''
        проверяет количество метеоритов которые пролетели за игрока, проходя каджый по циклу
        если их больше определенного числа, то игрок проигрывает
        '''
        for unit in self.meteors:
            if unit['x'] > 0 and unit['x'] < 10:
                self.lost += 1

    def timer(self):
        '''
        функция времени + функция отрисовки счета
        по остатку от времени создает метеорит и выводит на экран количество метеоритов, что сбил человек
        и количество пропущенных метеоритов
        '''
        self.time -= 1
        if self.time % 7 == 0:
            self.meteors.append(new_meteor())
        f1 = pg.font.Font(None, 36)
        text1 = f1.render('you done'+'' + str(self.calculate) + '/' + '50', 1, TOMATO)
        self.screen.blit(text1, (500, 20))
        f1 = pg.font.Font(None, 36)
        text1 = f1.render('you lost' + '' + str(self.lost) + '/' + '10', 1, TOMATO)
        self.screen.blit(text1, (500, 50))
        if self.calculate == 50:
            self.win = 1
        if self.lost > 9:
            self.crash = True

    def kill(self):
        '''
        проходя циклом по всем парам выстрел метеор сравнивает расстояние между ними через функцию check
        если оно меньше фиксированной константы удаляет метеорит и выстрел
        '''
        for i, ball in enumerate(self.strikes):
            for j, meteor in enumerate(self.meteors):
                if self.check(ball, meteor) == 1:
                    self.strikes.pop(i)
                    self.meteors.pop(j)
                    self.calculate += 1

    def check(self, ball, meteor):
        '''
        считает расстояние между данный метеоритом и данной пулей
        '''
        if (ball['x'] - meteor['x'])**2 + (ball['y'] - meteor['y'])**2 < (40+3)**2:
            return 1

    def zepopa(self):
        '''
        проходя циклом по всем метеоритам считает расстояние между каждым из них и кораблем
        если расстояние меньше фиксированного, то происходит столкновение
        т.е параметр столкновения становится равен правде
        '''
        for meteor in self.meteors:
            if (meteor['x']-a['x'])**2+(meteor['y']-a['y'] - 15) ** 2 < (20+30) ** 2:
                self.crash = True

    def end(self):
        '''
        проверяет закончилась ли игра т.е смотрит уничтожил ли игрок нужное количество метеоритов
        столкнулся с каким-нибудь из них, или пропустил их слишком много
        '''
        if self.win == True or self.crash == True:
            return 1

    def process(self, events):
        '''
        отвечает за процесс игры
        '''
        done = self.handle_events(events)
        self.draw()
        self.teleportation()
        self.timer()
        self.kill()
        self.zepopa()
        self.lose()
        if self.end() == 1:
            done = True
        return done, self.win
    
pg.quit()