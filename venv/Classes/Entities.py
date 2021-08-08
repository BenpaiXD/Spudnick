from venv.Classes.Sprites import *

class Entities:
    def __init__(self, screen):
        self._entities = []
        self._screen = screen

    def add(self, entity):
        self._entities.append(entity)

    def addID(self, ID, x, y):
        if ID == 1:
            self._entities.append(Tree((x, y), 192, 256, self._screen))
        elif ID == 2:
            self._entities.append(Tree((x, y), 192,256, self._screen))
            self._entities[-1].setSpriteIndex(1)
        elif ID == 3:
            self._entities.append(Croc((x, y), 128, 256, self._screen))


    def displayEntities(self):
        for entity in self._entities:
            entity.display()

    def viewHitboxes(self, bool):
        for entity in self._entities:
            entity.setViewHitbox(bool)

    def get(self, i):
        return self._entities[i];

    def getList(self):
        return self._entities

    def __str__(self):
        string = ""
        for e in self._entities:
            string += e.__str__() + ", "

        return string