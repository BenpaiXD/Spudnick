import pygame
from venv.Classes.Camera import *

class Hitbox:
    def __init__(self, x,y,width, height, screen):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._screen = screen

    def checkIntersect(self, hitbox2, depth):
        if(depth < 0):
            return False

        top = False
        bottom = False
        left = False
        right = False

        #check for left side intersection
        if(hitbox2.getX() <= self._x and self._x <= hitbox2.getEdgeR()):
            left = True

        #checks for right side intersection
        if (hitbox2.getX() <= self.getEdgeR() and self.getEdgeR() <= hitbox2.getEdgeR()):
            right = True

        #checks for top side intersection
        if (hitbox2.getY() <= self._y and self._y <= hitbox2.getEdgeB()):
            top = True

        #checks for bottom side intersection
        if (hitbox2.getY() <= self.getEdgeB() and self.getEdgeB() <= hitbox2.getEdgeB()):
            bottom = True

        return (left or right) and (top or bottom) or hitbox2.checkIntersect(self, depth-1)

    def setCoords(self, x, y):
        self._x = x
        self._y = y

    def changeCoords(self,x,y):
        self._x += x
        self._y += y

    def setDim(self, width, height):
        self._width = width
        self._height = height

    def display(self):
        pygame.draw.rect(self._screen.getScreen(), (255, 0, 0), (self._x - Camera.scroll[0], self._y - Camera.scroll[1], self._width, self._height), 2)

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def getEdgeR(self):
        return self._x + self._width
    def getEdgeB(self):
        return self._y + self._height

    def __str__(self):
        return "Hitbox: Pos = (" + str(self._x) + ", " + str(self._y) + ")"


class Interactbox(Hitbox):
    def __init__(self, x, y, width, height, screen):
        super().__init__(x,y,width, height, screen)

    def display(self):
        pygame.draw.rect(self._screen.getScreen(), (0, 255, 247), (self._x - Camera.scroll[0], self._y - Camera.scroll[1], self._width, self._height), 2)