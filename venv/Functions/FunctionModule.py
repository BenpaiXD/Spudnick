import pygame, os

def imageList(directory):
    lst = []
    for file in os.listdir(directory):

        if file.endswith(".jpg") or file.endswith(".png"):

            lst.append(pygame.image.load(os.path.join(directory, file)))

    return lst

def scale(spriteList, width, height):
    for i in range(len(spriteList)):
        spriteList[i] = pygame.transform.scale(spriteList[i], (width, height))
    return spriteList