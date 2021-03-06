from venv.Functions.FunctionModule import * 
import pygame, os

class Screen:
    def __init__(self, dimensions, caption, visible):
        self._width = dimensions[0]
        self._height = dimensions[1]
        self._caption = caption
        self._visible = visible
        self._backgroundList = imageList(r'venv/Backgrounds/')
        self._background = 0

        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._caption)

    def setCaption(self, caption):
        self._caption = caption
        pygame.display.set_caption(self._caption)

    def setDimensions(self, dimensions):
        self._width = dimensions[0]
        self._height = dimensions[1]

    def display(self, background):
        if self._visible:
            self._background = background
            self._screen.fill((0,0,0))
            self._screen.blit(self._backgroundList[self._background],(0,0))
            

    def getScreen(self):
        return self._screen

    def getHeight(self):
        return self._height

    def getWidth(self):
        return self._width

    def getBackground(self):
        return self._background