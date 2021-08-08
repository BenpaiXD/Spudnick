from venv.Functions.FunctionModule import *
from venv.Classes.Hitbox import *
import pygame, os
from venv.Classes.Enums import *
from venv.Classes.Camera import *
from venv.Classes.Textbox import *

class Sprite(object):
    def __init__(self, location, width, height, directory, screen):
        self._x = location[0]
        self._y = location[1]
        self._width = width
        self._height = height
        self._directory = directory
        self._spriteList = scale(imageList(self._directory), width, height)
        self._spriteIndex = 0
        self._hitbox = Hitbox(self._x, self._y, self._width, self._height, screen)
        self._viewHitbox = False
        self._vel = 0;
        self._screen = screen

        self._HBx = 0
        self._HBy = 0


    def display(self):
        self._screen.getScreen().blit(self._spriteList[self._spriteIndex], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))
        self.updateHitbox()

        if self._viewHitbox:
            self._hitbox.display()


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




    def setViewHitbox(self, TF):
        self._viewHitbox = TF

    def setVelocity(self, vel):
        self._vel = vel
    def setSpriteIndex(self, i):
        self._spriteIndex = i

    def updateHitbox(self):
        self._hitbox.setCoords(self._x +self._HBx, self._y + self._HBy)

    def getX(self):
        return self._x

    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height


class Character(Sprite):
    def __init__(self, location, width, height, directory, screen):
        super().__init__(location, width, height, directory, screen)

        self._walkCount = 0
        self._moving = False

        self._facing = Direction.LEFT

        self._walkLeft = scale(imageList(self._directory + 'walkLeft/'), height, width)
        self._walkRight = scale(imageList(self._directory + 'walkRight/'), height, width)
        self._walkUp = scale(imageList(self._directory + 'walkUp/'), height, width)
        self._walkDown = scale(imageList(self._directory + 'walkDown/'), height, width)
        self._idle = scale(imageList(self._directory + 'idle/'), height, width)

        self._freeze = False

    def setFreeze(self, TF):
        self._freeze = TF


    def moveUp(self, vWalls):
        if (not self._freeze):

            self._moving = True
            self._y -= self._vel
            self._facing = Direction.UP
            self.updateHitbox()

            for wall in vWalls:
                if(self._hitbox.checkIntersect(wall, 1)):
                    self._y += self._vel
                    break

            self.updateHitbox()

    def moveDown(self, vWalls):
        if (not self._freeze):
            self._moving = True
            self._y += self._vel
            self._facing = Direction.DOWN
            self.updateHitbox()

            for wall in vWalls:
                if(self._hitbox.checkIntersect(wall, 1)):
                    self._y -= self._vel
                    break
            self.updateHitbox()

    def moveRight(self, hWalls):
        if (not self._freeze):
            self._moving = True
            self._x += self._vel
            self._facing = Direction.RIGHT
            self.updateHitbox()

            for wall in hWalls:
                if(self._hitbox.checkIntersect(wall, 1)):
                    self._x -= self._vel
                    break
            self.updateHitbox()

    def moveLeft(self, hWalls):
        if(not self._freeze):
            self._moving = True
            self._x -= self._vel
            self._facing = Direction.LEFT
            self.updateHitbox()

            for wall in hWalls:
                if(self._hitbox.checkIntersect(wall, 1)):
                    self._x += self._vel
                    break
            self.updateHitbox()


class Player(Character):
    def __init__(self, location, width, height, screen):
        super().__init__(location, width, height, r'venv/Sprites/Spudnick/', screen)
        self.changeHitbox(24, 6, 80, 110)
        self.setVelocity(5)
        self._IBox = Interactbox(0, 0, 0, 0, screen)
        self._IBheight = 20
        self._IBwidth = 10
        self._attackTime = 0
        self._maxAttackTime = 23
        self._attackBox = None
        self._attacking = False
        self._attackCount = 0

        self._attackDown = scale(imageList(self._directory + 'attackDown/'), self._width, self._height)
        self._attackLeft = scale(imageList(self._directory + 'attackLeft/'), self._width, self._height)
        self._attackUp = scale(imageList(self._directory + 'attackUp/'), self._width, self._height)
        self._attackRight = scale(imageList(self._directory + 'attackRight/'), self._width, self._height)


    def updateHitbox(self):
        self._hitbox.setCoords(self._x +self._HBx, self._y + self._HBy)

    def getIBox(self):
        return self._IBox

    def attack(self):
        # print(str(self._attackBox) + ", " + str(self._attackTime))
        if self._attackTime == 0:
            self._freeze = False
            self._attackBox = None
            self._attacking = False
            self._attackCount = 0
            return

        self._attacking = True
        self._freeze = True
        self._attackTime -= 1

    def setAttackBox(self):
        if self._attackTime == 0:
            self._attackTime = self._maxAttackTime
            if self._facing == Direction.DOWN:
                self._attackBox = Hitbox(self._x, self._y + self._hitbox.getHeight(), self._width, self._hitbox.getHeight()/2, self._screen)

            elif self._facing == Direction.UP:
                self._attackBox = Hitbox(self._x, self._y - self._hitbox.getHeight()/2, self._width, self._hitbox.getHeight()/2, self._screen)

            elif self._facing == Direction.RIGHT:
                self._attackBox = Hitbox(self._x + self._width, self._y + self._HBy, self._width / 2, self._hitbox.getHeight(), self._screen)

            elif self._facing == Direction.LEFT:
                self._attackBox = Hitbox(self._x - self._width/2, self._y + self._HBy, self._width/2, self._hitbox.getHeight(), self._screen)


    def display(self):
        self.attack()

        if(self._moving):
            self._walkCount += 1
            if (self._walkCount > 47):
                self._walkCount = 0

        if self._attacking:
            self._attackCount += 1
            if(self._attackCount > 23):
                self._attackCount = 0


        if (self._facing == Direction.LEFT):
            self._IBox.setCoords(self._hitbox.getX() - self._IBwidth, self._hitbox.getY())
            self._IBox.setDim(self._IBwidth, self._hitbox.getHeight())

            if self._attacking:
                self._screen.getScreen().blit(self._attackLeft[self._attackCount // 6], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

            elif(self._moving):
                self._screen.getScreen().blit(self._walkLeft[self._walkCount//12], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))
            else:
                self._screen.getScreen().blit(self._idle[1], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

        elif (self._facing == Direction.RIGHT):
            self._IBox.setCoords(self._hitbox.getEdgeR(), self._hitbox.getY())
            self._IBox.setDim(self._IBwidth, self._hitbox.getHeight())

            if self._attacking:
                self._screen.getScreen().blit(self._attackRight[self._attackCount // 6], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

            elif (self._moving):
                self._screen.getScreen().blit(self._walkRight[self._walkCount // 12], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))
            else:
                self._screen.getScreen().blit(self._idle[2], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

        elif (self._facing == Direction.UP):
            self._IBox.setCoords(self._hitbox.getX(), self._hitbox.getY() - self._IBheight)
            self._IBox.setDim(self._hitbox.getWidth(), self._IBheight)

            if self._attacking:
                self._screen.getScreen().blit(self._attackUp[self._attackCount // 6], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

            elif (self._moving):
                self._screen.getScreen().blit(self._walkUp[self._walkCount//12], (self._x- Camera.scroll[0], self._y - Camera.scroll[1]))
            else:
                self._screen.getScreen().blit(self._idle[3], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

        elif (self._facing == Direction.DOWN):
            self._IBox.setCoords(self._hitbox.getX(), self._hitbox.getEdgeB())
            self._IBox.setDim(self._hitbox.getWidth(), self._IBheight)

            if self._attacking:
                self._screen.getScreen().blit(self._attackDown[self._attackCount // 6], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

            elif (self._moving):
                self._screen.getScreen().blit(self._walkDown[self._walkCount // 12], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))
            else:
                self._screen.getScreen().blit(self._idle[0], (self._x - Camera.scroll[0], self._y - Camera.scroll[1]))

        self._moving = False

        if self._viewHitbox:
            self._hitbox.display()
            self._IBox.display()
            if self._attackBox != None:
                self._attackBox.display()


class Spider(Character):
    def __init__(self, location, width, height, screen):
        super(Spider, self).__init__(location, width, height, screen)




class Croc(Sprite):
    def __init__(self, location, width, height, screen):
        super().__init__(location, width, height, r'venv/Sprites/FuzzyCroc/', screen)
        self.changeHitbox(0,32, 128,128)

    def interact(self, player, dBoxes):
        if(self._hitbox.checkIntersect(player.getIBox(), 1)):
            player.setFreeze(True)
            dBoxes.append(DialogueBox(r'venv/Sprites/FuzzyCroc/', 'venv/Dialogue/FuzzyCroc/FuzzyCroc.txt', self._screen))



class Tree(Sprite):
    def __init__(self, location, width, height, screen):
        super().__init__(location, width, height,  r'venv/Sprites/Tree/', screen)
        self.changeHitbox(11, 10, 170, 170)

    def __str__(self):
        return "Tree"