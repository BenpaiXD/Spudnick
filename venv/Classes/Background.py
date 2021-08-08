import pygame, os
from venv.Functions.FunctionModule import *
from venv.Classes.Camera import *
from venv.Classes.Hitbox import *
from venv.Classes.Sprites import *
from venv.Classes.Entities import *

class Background:
    def __init__(self, tilePath, mapPath, screen):
        self._tileHeight = 64
        self._tileWidth = 64
        self._height = 0
        self._width = 0
        self._background = pygame.Surface([0,0])
        self._x = 0
        self._y = 0
        self._screen = screen

        self._mapFile = open(mapPath, 'r')
        self._tiles = scale(imageList(tilePath), self._tileWidth, self._tileHeight)

        self._entities = Entities(screen)
        self._entities.viewHitboxes(True)

        self._tileMap = []

        self.readFile()
        print(self._entities)

        for row in self._tileMap:
            for tile in row:
                self._background.blit(tile._tileImage, (tile._x, tile._y))

        # top, bottom, left, right
        self._hitboxes = [Hitbox(-50, -50, self.getWidth() + 100, 50, screen), Hitbox(-50, self.getHeight(), self.getWidth() + 100, 50, screen), Hitbox(-50, -50, 50, self.getHeight() + 100, screen), Hitbox(self.getWidth(), -50, 50, self.getHeight() + 100, screen)]




    def readFile(self):
        lines = self._mapFile.readlines()
        for line in lines:
            if line == "|\n":
                break
            self._height += 1

        objects = lines[self._height+1:]
        lines = lines[:self._height]
        print(lines)
        print(objects)

        self._width = len(lines[0].split())
        self._background = pygame.Surface([self.getWidth(),self.getHeight()])
        j = 0
        for i in range(self._height):
            row = []
            for tile in lines[i].split():
                self._background.blit(self._tiles[int(tile)], (self._tileWidth * j, self._tileHeight * i))
                j+=1
            j = 0
            self._tileMap.append(row)

        for i in objects:
            i = i.split()
            self._entities.addID(int(i[0]), int(i[1]), int(i[2]))



    def getHeight(self):
        return self._tileHeight * self._height
    def getWidth(self):
        return self._tileWidth * self._width

    def getHitboxes(self):
        return self._hitboxes

    def getTiles(self):
        return self._tiles

    def getEntityList(self):
        return self._entities.getList()

    def setViewHitboxes(self, bool):
        self._entities.viewHitboxes(bool)

    def display(self):
        self._screen.getScreen().blit(self._background, (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))
        self._entities.displayEntities()


class Tile:
    def __init__(self, tileID, background, x, y):
        self._tileID = tileID
        self._tileImage = background.getTiles()[self._tileID];
        self._x = x
        self._y = y


    def display(self, screen):
        screen.getScreen().blit(self._tileImage, (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

    def __repr__(self):
        return "Tile = " + str(self._tileID)