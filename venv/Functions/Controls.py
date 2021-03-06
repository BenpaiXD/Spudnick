import pygame
from venv.Classes.Sprites import Player

def controls(player, vWall, hWall):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        player._moving = True
        player.moveRight(hWall)
    
    elif keys[pygame.K_LEFT]:
        player._moving = True
        player.moveLeft(hWall)

    if keys[pygame.K_UP]:
        player._moving = True
        player.moveUp(vWall)

    elif keys[pygame.K_DOWN]:
        player._moving = True
        player.moveDown(vWall)
