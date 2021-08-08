import pygame, os
from venv.Classes.Screen import *
from venv.Classes.Sprites import *
from venv.Functions.Controls import *
from venv.Classes.Background import *
from venv.Classes.Camera import *
from venv.Classes.Entities import *
from venv.Classes.Textbox import *
from venv.Classes.Buffer import *


def main():
    pygame.init()
    run = True

    clock = pygame.time.Clock()
    screen1 = Screen((1600, 900), "SpudNick: The Game", True)

    player = Player((500, 351), 128, 128, screen1)
    player.setViewHitbox(True)

    bg = Background(r'venv/Sprites/GroundTiles', 'venv/Backgrounds/map1.txt', screen1)

    # top, bottom,
    # left, right
    walls = [bg.getHitboxes()[0], bg.getHitboxes()[1], bg.getHitboxes()[2], bg.getHitboxes()[3]]

    for entity in bg.getEntityList():
        walls.append(entity.getHitbox())
    bg.setViewHitboxes(True)

    iBoxes = []
    dialogueBoxes = []
    held = [False, False]
    buff = Buffer(30)

    while run:
        # time delay for frame rate
        # pygame.time.delay(round((1 / 60 * 1000)))

        print(str(int(clock.get_fps())))
        # horizontal scroll set up
        if 0 < Camera.scroll[0] + (player.getX() - Camera.scroll[
            0] - screen1.getWidth() / 2 + player.getWidth()) / 10 < bg.getWidth() - screen1.getWidth():
            Camera.scroll[0] += (player.getX() - Camera.scroll[0] - screen1.getWidth() / 2 + player.getWidth()) / 10

        # vertical scroll set up
        if 0 < Camera.scroll[1] + (player.getY() - Camera.scroll[
            1] - screen1.getHeight() / 2 + player.getHeight()) / 10 < bg.getHeight() - screen1.getHeight():
            Camera.scroll[1] += (player.getY() - Camera.scroll[1] - screen1.getHeight() / 2 + player.getHeight()) / 10

        # stop game on closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        controls(player, walls, held, iBoxes, dialogueBoxes, buff)

        screen1.display(1)
        bg.display()
        player.display()

        for dBox in dialogueBoxes:
            dBox.display(screen1)

        # update screen
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
