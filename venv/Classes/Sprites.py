from venv.Functions.FunctionModule import *
from venv.Classes.Hitbox import *
import pygame, os
from venv.Classes.Enums import *

class Sprite(object):
    def __init__(self, location, width, height, directory):
        self._x = location[0]
        self._y = location[1]
        self._width = width
        self._height = height
        self._directory = directory
        self._spriteList = scale(imageList(self._directory), height, width)
        self._spriteIndex = 0
        self._hitbox = Hitbox(self._x, self._y, self._width, self._height)
        self._viewHitbox = False
        self._facing = Direction.LEFT
        self._vel = 0;

        self._walkLeft = scale(imageList(self._directory + 'walkLeft/'), height, width)
        self._walkRight = scale(imageList(self._directory + 'walkRight/'), height, width)
        self._walkUp = scale(imageList(self._directory + 'walkUp/'), height, width)
        self._walkDown = scale(imageList(self._directory + 'walkDown/'), height, width)
        self._idle = scale(imageList(self._directory + 'idle/'), height, width)

        self._HBx = 0
        self._HBy = 0


    def display(self, screen):
        screen.getScreen().blit(self._spriteList[self._spriteIndex], (self._x, self._y))
        self.updateHitbox()

        if self._viewHitbox:
            self._hitbox.display(screen)


    def setLocation(self,x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x
    def y(self):
        return self._y

    def changeHitbox(self,x,y, width, height):
        self._HBx = x
        self._HBy = y
        self._hitbox.setDim(width, height)

    def getHitbox(self):
        return self._hitbox

    def moveUp(self, vWalls):
        self._y -= self._vel
        self._facing = Direction.UP
        self.updateHitbox()

        for wall in vWalls:
            if(self._hitbox.checkIntersect(wall, 1)):
                self._y += self._vel
                break

        self.updateHitbox()

    def moveDown(self, vWalls):
        self._y += self._vel
        self._facing = Direction.DOWN
        self.updateHitbox()

        for wall in vWalls:
            if(self._hitbox.checkIntersect(wall, 1)):
                self._y -= self._vel
                break
        self.updateHitbox()

    def moveRight(self, hWalls):
        self._x += self._vel
        self._facing = Direction.RIGHT
        self.updateHitbox()

        for wall in hWalls:
            if(self._hitbox.checkIntersect(wall, 1)):
                self._x -= self._vel
                break
        self.updateHitbox()

    def moveLeft(self, hWalls):
        self._x -= self._vel
        self._facing = Direction.LEFT
        self.updateHitbox()

        for wall in hWalls:
            if(self._hitbox.checkIntersect(wall, 1)):
                self._x += self._vel
                break
        self.updateHitbox()


    def setViewHitbox(self, TF):
        self._viewHitbox = TF

    def setVelocity(self, vel):
        self._vel = vel

    def updateHitbox(self):
        self._hitbox.setCoords(self._x +self._HBx, self._y + self._HBy)

class Player(Sprite):
    def __init__(self, location, width, height, directory):
        super().__init__(location, width, height, directory)
        self._walkCount = 0
        self._moving = False

    def display(self, screen):

        print(self._moving)
        #self.updateHitbox()
        if(self._moving):
            self.animate(screen)

        elif (self._facing == Direction.LEFT):
            screen.getScreen().blit(self._idle[1], (self._x, self._y))
        elif (self._facing == Direction.RIGHT):
            screen.getScreen().blit(self._idle[2], (self._x, self._y))
        elif (self._facing == Direction.UP):
            screen.getScreen().blit(self._idle[3], (self._x, self._y))
        elif (self._facing == Direction.DOWN):
            screen.getScreen().blit(self._idle[0], (self._x, self._y))

        
        if self._viewHitbox:
            self._hitbox.display(screen)

    def animate(self, screen):
        if(self._walkCount > 47):
            self._walkCount = 0

        if (self._facing == Direction.LEFT):
            screen.getScreen().blit(self._walkLeft[self._walkCount//12], (self._x, self._y))
        elif (self._facing == Direction.RIGHT):
            screen.getScreen().blit(self._walkRight[self._walkCount//12], (self._x, self._y))
        elif (self._facing == Direction.UP):
            screen.getScreen().blit(self._walkUp[self._walkCount//12], (self._x, self._y))
        elif (self._facing == Direction.DOWN):
            screen.getScreen().blit(self._walkDown[self._walkCount//12], (self._x, self._y))

        self._walkCount += 1
