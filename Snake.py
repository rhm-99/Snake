# Learnt from https://www.edureka.co/blog/snake-game-with-pygame/ (may be slightly edited)
import random
import pygame
import math
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 20
    w = 400

    def __init__(self, start, dirnx=1, dirny=0, color=(0,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = width / rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    surface.fill((0, 0, 0))
    drawGrid(surface)
    pygame.display.update()


def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 400
    height =400
    rows = 20

    win = pygame.display.set_mode((width, height))

    s = snake((255, 255, 255), (10, 10))

    clock = pygame.time.Clock()

    flag = True

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)


main()
