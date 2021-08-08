import pygame
import os
from venv.Functions.FunctionModule import *

class TextBox:

    def __init__(self, String, x, y, font, size, BGColour, FGColour):
        self._String = String
        self._x = x
        self._y = y
        self._font = pygame.font.SysFont(font, size)
        self._FGColour = FGColour
        self._BGColour = BGColour

        self._text = self._font.render(self._String, True, self._FGColour, self._BGColour)
        self._textRect = self._text.get_rect()
        # self._textRect.center = (self._x, self._y)

    def setPos(self, x, y):
        self._x = x
        self._y = y
        self._textRect.center = (self._x, self._y)

    def setText(self, text):
        self._String = text
        self._text = self._font.render(self._String, True, self._FGColour, self._BGColour)
        self._textRect = self._text.get_rect()
        self._textRect.center = (self._x, self._y)

    def display(self, screen):
        screen.getScreen().blit(self._text, self._textRect)

class DialogueBox:
    def __init__(self, imageDirectory, txtDirectory, screen):
        self._x = int(screen.getWidth() * 0.05)
        self._y = int(screen.getHeight() * 0.6)
        self._width = int(screen.getWidth() * 0.9)
        self._height = int(screen.getHeight() * 1 / 3)
        self._padding = 10
        self._BGC = (0, 0, 0)
        self._FGC = (255, 255, 255)
        self._font = pygame.font.SysFont("arial", 24)
        self._textFile = open(txtDirectory, "r")


        self._textRect = pygame.Rect(self._x, self._y , self._width, self._height)

        self._imageSize = self._height - 2 * self._padding
        self._spriteList = scale(imageList(imageDirectory), self._imageSize, self._imageSize)

        self._lines = []
        self.readLines(txtDirectory)
        self._numLines = len(self._lines)
        self._lineIndex = 0
        self._text = self._font.render(self._lines[self._lineIndex], True, self._FGC, self._BGC)


    def readLines(self, directory):
        lines = self._textFile.readlines()
        string = ""
        for line in lines:
            if line[0] =="|":
                self._lines.append(string)
                string = ""
            else:
                string = string + line

    def nextLine(self):
        self._lineIndex += 1
        if self._lineIndex < self._numLines:
            self._text = self._font.render(self._lines[self._lineIndex], True, self._FGC, self._BGC)

            return True
        return False



    def display(self, screen):
        pygame.draw.rect(screen.getScreen(), self._BGC, self._textRect)
        screen.getScreen().blit(self._spriteList[0], (self._x + self._padding, self._y + self._padding))

        screen.getScreen().blit(self._text, (self._x + 2 * self._padding + self._imageSize, self._y + self._padding))

