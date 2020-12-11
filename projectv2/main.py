import pygame as pg
import numpy as np
from random import randint
import cv2
import game1
import game2
import game4
import experiment

'''
набор констант 
'''
SCREEN_SIZE = (1200, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (255, 250, 205)
RED = (255, 0, 0)
YELLOW = (128, 0, 0)
BROWN = (160, 82, 45)
TOMATO = (255, 200, 181)
SKYBLUE = (100, 149, 237)



screen = pg.display.set_mode(SCREEN_SIZE)
pg.init()
pg.font.init()
font_1 = pg.font.SysFont("serif", 60)
k = 0
seq = 30 * 60 * 10

pg.mixer.music.load('adventure_music.mp3')
pg.mixer.music.set_volume(0.1)

pg.mixer.music.play()


class Timer():
    '''
    отвечает за время и его отрисовку
    '''
    global A

    def __init__(self, time=seq):
        self.time = time

    def draw(self):
        '''
        рисует полоску времени, как только она заполняется игрок проигрывает и срабатывает функция bad_end
        '''
        a = (seq - self.time)/seq
        a = int(a * 1200)
        pg.draw.rect(screen, RED, (0, 10, a, 10))
        f1 = pg.font.Font(None, 36)
        text1 = f1.render('TIME YOU HAVE', 1, RED)
        screen.blit(text1, (500, 20))

    def change(self):
        '''
        уменьшает время
        '''
        self.time -= 1

    def bad_end(self):
        '''
        в случает проигрыша игрока вызывает черный экран с надписью ты проиграл
        '''
        if self.time <= 0:
            screen.fill(BLACK)
            f1 = pg.font.Font(None, 36)
            text1 = f1.render('You lose', 1, RED)
            screen.blit(text1, (520, 300))

    def good_end(self):
        '''
        считает количество минигр, которые прошел игрок
        если игрок прошел все, то вызывает зороший конец
        экран становится черным с надписью ты победил
        '''
        f1 = pg.font.Font(None, 36)
        text1 = f1.render('You done' + ' ' + str(A) + '/4', 1, RED)
        screen.blit(text1, (1000, 40))
        if A == 4:
            screen.fill(BLACK)
            f1 = pg.font.Font(None, 36)
            text1 = f1.render('You win', 1, RED)
            screen.blit(text1, (520, 300))


class Map():
    '''
    рисует карту
    '''
    def __init__(self, screen):
        self.screen = screen
        self.coord_points = [[50, 350], [450, 350], [450, 150], [850, 150], [1050, 350]]

    def draw(self):
        '''
        рисует лабиринт
        '''
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
        pg.draw.rect(self.screen, BROWN, (100, 0, 100, 100))
        pg.draw.circle(self.screen, YELLOW, (1050, 350), 20)
        pg.draw.rect(self.screen, BROWN, (0, 0, 4, 600))
        pg.draw.rect(self.screen, BROWN, (0, 596, 1200, 4))
        pg.draw.rect(self.screen, BROWN, (1196, 0, 4, 600))
        pg.draw.rect(self.screen, GRAY, (100, 10, 100, 100))
        pg.draw.rect(self.screen, GRAY, (700, 100, 100, 100))
        pg.draw.rect(self.screen, GRAY, (900, 200, 80, 100))
        pg.draw.rect(self.screen, GRAY, (1100, 100, 96, 200))
        pg.draw.rect(self.screen, GRAY, (1000, 100, 100, 100))


'''
анимация движений героя
'''
hero1 = pg.image.load('jump1.png')
hero2 = pg.image.load('jump2.png')
hero3 = pg.image.load('jump3.png')
hero4 = pg.image.load('jump3.png')


class Hero():
    def __init__(self, coord=[150, 550]):
        self.coord = coord

    def draw(self, screen):
        '''
        рисует героя с центром в его координатах
        '''
        global k
        k += 1
        if (k//10+1) % 5 == 0:
            screen.blit(hero1, (self.coord[0]-35, self.coord[1]-35))
        if (k//10+1) % 5 == 1 or (k//10+1) % 5 == 2:            
            screen.blit(hero2, (self.coord[0]-35, self.coord[1]-35))
        if (k//10+1) % 5 == 3:            
            screen.blit(hero3, (self.coord[0]-35, self.coord[1]-35))
        if (k//10+1) % 5 == 4:      
            screen.blit(hero4, (self.coord[0]-35, self.coord[1]-35))

    def night(self):
        '''
        оставляет для игрока видимой щону лишь вокруг героя
        '''
        pg.draw.polygon(screen, BLACK, [[0, 0], [self.coord[0] - 40, self.coord[1] - 40],
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
        '''
        процесс игры
        '''
        done = self.handle_events(events)
        self.map.draw()
        self.hero.draw(screen)
        self.time.change()
        self.teleportation()
        self.hero.night()
        self.time.draw()
        self.time.bad_end()
        self.time.good_end()
        return [done, self.where_are_you()]

    def handle_events(self, events):
        '''
        считывает зажатия и нажатия клавиш
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
    
    def where_are_you(self):
        '''
        возвращает координаты героя
        '''
        for i in range(5):
            if (self.hero.coord[0] - self.map.coord_points[i][0]) ** 2 + (self.hero.coord[1] -
                                                                        self.map.coord_points[i][1]) ** 2 < 250:
                return i

    def teleportation(self):
        '''
        в случае если зажата одна из клавиш перемещения меняет положение героя
        '''
        if self.up_key_pressed:
            if screen.get_at((self.hero.coord[0], self.hero.coord[1] - 37)) == GRAY or \
                    screen.get_at((self.hero.coord[0], self.hero.coord[1] - 37)) == YELLOW:
                if screen.get_at((self.hero.coord[0] - 23, self.hero.coord[1] - 37)) == GRAY or \
                        screen.get_at((self.hero.coord[0] - 23, self.hero.coord[1] - 37)) == YELLOW:
                    if screen.get_at((self.hero.coord[0] + 23, self.hero.coord[1] - 37)) == GRAY or \
                            screen.get_at((self.hero.coord[0] + 23, self.hero.coord[1] - 37)) == YELLOW:
                        self.hero.coord[1] -= 2
        if self.down_key_pressed:
            if screen.get_at((self.hero.coord[0], self.hero.coord[1] + 37)) == GRAY or\
                    screen.get_at((self.hero.coord[0], self.hero.coord[1] + 37)) == YELLOW:
                if screen.get_at((self.hero.coord[0] + 23, self.hero.coord[1] + 25)) == GRAY or \
                        screen.get_at((self.hero.coord[0] + 23, self.hero.coord[1] + 25)) == YELLOW:
                    if screen.get_at((self.hero.coord[0] - 23, self.hero.coord[1] + 25)) == GRAY or \
                            screen.get_at((self.hero.coord[0] - 23, self.hero.coord[1] + 25)) == YELLOW:
                        self.hero.coord[1] += 2
        if self.left_key_pressed:
            if screen.get_at((self.hero.coord[0] - 25, self.hero.coord[1])) == GRAY or \
                    screen.get_at((self.hero.coord[0] - 25, self.hero.coord[1])) == YELLOW:
                if screen.get_at((self.hero.coord[0] - 25, self.hero.coord[1] + 32)) == GRAY or \
                        screen.get_at((self.hero.coord[0] - 25, self.hero.coord[1] + 32)) == YELLOW:
                    if screen.get_at((self.hero.coord[0] - 25, self.hero.coord[1] - 27)) == GRAY or \
                            screen.get_at((self.hero.coord[0] - 25, self.hero.coord[1] - 27)) == YELLOW:
                        self.hero.coord[0] -= 2
        if self.right_key_pressed:
            if screen.get_at((self.hero.coord[0] + 25, self.hero.coord[1])) == GRAY or\
                    screen.get_at((self.hero.coord[0] + 25, self.hero.coord[1])) == YELLOW:
                if screen.get_at((self.hero.coord[0] + 25, self.hero.coord[1] + 32)) == GRAY or \
                        screen.get_at((self.hero.coord[0] + 25, self.hero.coord[1] + 32)) == YELLOW:
                    if screen.get_at((self.hero.coord[0] + 25, self.hero.coord[1] - 27)) == GRAY or \
                            screen.get_at((self.hero.coord[0] + 25, self.hero.coord[1] - 27)) == YELLOW:
                        self.hero.coord[0] += 2


pg.display.set_caption("TRY TO ESCAPE")
clock = pg.time.Clock()

A = 0


dots_figure = [[[180, 588], [255, 513], [330, 588]],
              [[100, 569], [25, 519], [25, 569]],
              [[13, 392], [63, 517], [163, 392]],
              [[243, 371], [293, 496], [243, 496]],
              [[120, 496], [220, 496], [220, 371]],
              [[117, 512], [167, 512], [167, 562], [117, 562]],
              [[304, 556], [379, 506], [379, 456], [304, 506]],
              [[275, 402], [350, 402], [350, 452]],
              [[371, 118], [471, 118], [471, 18]],

              [[670, 162], [570, 162], [570, 62]],
              [[567, 177], [667, 177], [667, 277]],
              [[785, 176], [685, 176], [685, 276]],
              [[432, 197], [482, 222], [532, 172], [482, 122]],
              [[488, 19], [488, 94], [538, 44]],
              [[502, 112], [552, 162], [552, 62]],
              [[675, 86], [725, 36], [675, 36]],
              [[677, 107], [677, 157], [727, 157], [727, 57]],
              [[745, 111], [745, 11], [795, 86], [795, 161]],
                           
              [[1050, 465], [1150, 465], [1050, 565]],
              [[766, 577], [816, 527], [941, 527], [891, 577]],
              [[1049, 337], [1174, 337], [1174, 437], [1049, 437]],
              [[1169, 481], [1119, 531], [1119, 581], [1169, 581]],
              [[918, 418], [918, 393], [968, 343], [1043, 418]],
              [[1048, 225], [1048, 325], [1173, 325]],
              [[822, 321], [822, 396], [897, 346], [897, 321]],
              [[834, 420], [909, 370], [909, 495]],
              [[922, 464], [922, 439], [1022, 439], [1022, 589]]]


centers_match = [[[199, 99], [249, 280], [191, 164], [140, 205], [241, 206],
                 [197, 273],  [136, 297], [277, 318]],

                 [[564, 317], [632, 315], [565, 380], [633, 379], [548, 453], 
                  [516, 506], [581, 498], [614, 517], [622, 462], [674, 481]],
                 
                 [[882, 82], [986, 74], [961, 150], [871, 160], [1067, 99],
                  [1065, 190], [887, 223], [899, 281], [974, 244]]]

'''
набор сокращений 
в случае минигр создает массив из двух элементов 
первый отвечает за то, что игра идет 
второй отвечает за то, прошел ли игрок игру
'''
done = False
mgr = Manager()

done1 = [False, False]
mgr1 = game1.Manager(50, screen)
phrase1_1 = pg.image.load("phrase/1.png")
phrase1_2 = pg.image.load('phrase/2.1.png')
phrase1_3 = pg.image.load("phrase/3.1.png")

mgr2 = game2.Manager(dots_figure, screen)
done2 = [False, False]
phrase2_1 = pg.image.load("phrase/1.4.png")
phrase2_2 = pg.image.load('phrase/2.4.png')
phrase2_3 = pg.image.load("phrase/3.4.png")

mgr4 = game4.Manager(screen)
done4 = [False, 0]
phrase4_1 = pg.image.load("phrase/1.3.png")
phrase4_2 = pg.image.load('phrase/2.3.png')
phrase4_3 = pg.image.load("phrase/3.3.png")

mgr3 = experiment.Manager(screen)
done3 = [False, 0]
phrase3_1 = pg.image.load("phrase/1.2.png")
phrase3_2 = pg.image.load('phrase/2.2.png')
phrase3_3 = pg.image.load("phrase/3.1.png")

while not done:
    '''
    в зависимости от положения игрока на карте запускает минигру
    если игрок прошел миниигру то увеличивает счетчик миниигр на 1
    '''
    clock.tick(150)
    done = mgr.process(pg.event.get(), screen)[0]
    if 0 == mgr.process(pg.event.get(), screen)[1] and not done1[0]:
        pg.mixer.music.stop() 
        pg.mixer.music.load('fake_id.mp3')
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.1)
        while not done1[0]:
            clock.tick(20)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        done1[0] = True  
                if event.type == pg.QUIT:
                    done1[0] = True
            screen.fill(TOMATO)
            screen.blit(phrase1_1,(50,100))
            screen.blit(phrase1_2,(500,300))
            screen.blit(phrase1_3,(300,500))
            pg.display.update()
            mgr.time.change()
        done1[0] = False
        while not done1[0]:
            clock.tick(120)
            done1 = mgr1.process(pg.event.get(), screen)
            pg.display.update()
            mgr.time.change()
        if done1[1] == True:
            A += 1
    if 4 == mgr.process(pg.event.get(), screen)[1] and not done2[0]:
        pg.mixer.music.stop() 
        pg.mixer.music.load('felicia.mp3')
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.1)
        while not done2[0]:
            clock.tick(20)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        done2[0] = True  
                if event.type == pg.QUIT:
                    done2[0] = True
            screen.fill((216, 191, 216))
            screen.blit(phrase2_1,(50,100))
            screen.blit(phrase2_2,(500,300))
            screen.blit(phrase2_3,(300,500))
            pg.display.update()
            mgr.time.change()
        done2[0] = False

        while not done2[0]:
            clock.tick(10000)
            mgr2.draw(screen, centers_match)
            done2 = mgr2.handle_events(pg.event.get())
            mgr.time.change()
            pg.display.update()
        if done2[1] == True:
            A += 1
    if 1 == mgr.process(pg.event.get(), screen)[1] and not done4[0]:
        pg.mixer.music.stop() 
        pg.mixer.music.load('new_rules.mp3')
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.1)
        while not done4[0]:
            clock.tick(20)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        done4[0] = True  
                if event.type == pg.QUIT:
                    done4[0] = True
            screen.fill((152, 251, 152))
            screen.blit(phrase4_1,(50,100))
            screen.blit(phrase4_2,(500,300))
            screen.blit(phrase4_3,(300,500))
            pg.display.update()
            mgr.time.change()
        done4[0] = False
        while not done4[0]:
            clock.tick(30)
            done4 = mgr4.process(pg.event.get())
            pg.display.update() 
            mgr.time.change()
        if done4[1] == 1:
            A += 1
    if 2 == mgr.process(pg.event.get(), screen)[1] and not done3[0]:
        pg.mixer.music.stop() 
        pg.mixer.music.load('psy.mp3')
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.1)
        while not done3[0]:
            clock.tick(20)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        done3[0] = True  
                if event.type == pg.QUIT:
                    done3[0] = True
            screen.fill(SKYBLUE)
            screen.blit(phrase3_1,(600,100))
            screen.blit(phrase3_2,(100,300))
            screen.blit(phrase1_3,(400,500))
            pg.display.update()
            mgr.time.change()
        done3[0] = False
        while not done3[0]:
            clock.tick(30)
            done3 = mgr3.process(pg.event.get())
            pg.display.update() 
            mgr.time.change()
        if done3[1] == 1:
            A += 1

    pg.display.update()

pg.quit()
