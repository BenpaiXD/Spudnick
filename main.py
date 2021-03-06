import pygame, os
from venv.Classes.Screen import *
from venv.Classes.Sprites import *
from venv.Functions.Controls import *
from venv.Classes.Hitbox import *


def main():
    pygame.init()

    frameCount = 0
    run = True

    screen1 = Screen((800, 600), "SpudNick: The Game", True)

    player = Player((301, 351), 128, 128, r'venv/Sprites/Spudnick/')
    player.setVelocity(5)
    player.changeHitbox(18, 6, 92, 110)
    #player.setViewHitbox(True)

    #top, bottom,
    # left, right
    vWalls = [Hitbox(-50,-50, screen1.getWidth() + 100, 50),Hitbox(-50,screen1.getHeight(), screen1.getWidth() + 100, 50)]
    hWalls = [Hitbox(-50,-50, 50, screen1.getHeight() + 100), Hitbox(screen1.getWidth(),-50, 50, screen1.getHeight() + 100)]

    while run:
        pygame.time.delay(round((1 / 60 * 1000)))

        # stop game on closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player._moving = False
        controls(player, vWalls, hWalls)

        screen1.display(1)
        player.display(screen1)

        #update screen
        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main()
