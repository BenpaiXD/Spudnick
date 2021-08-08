import pygame
from venv.Classes.Sprites import Player
from venv.Classes.Textbox import *
from venv.Classes.Buffer import *

def controls(player, wall, held, iBoxes, dialogueBoxes, buffer):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.moveRight(wall)
    
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.moveLeft(wall)

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.moveUp(wall)

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.moveDown(wall)

    if keys[pygame.K_e] and not held[0]:
        if not dialogueBoxes:
            for iBox in iBoxes:
                iBox.interact(player, dialogueBoxes)

        else:
            for box in dialogueBoxes:
                if not box.nextLine():
                    dialogueBoxes.remove(box)
                    player.setFreeze(False)
        held[0] = True
    elif keys[pygame.K_e]:
        pass
    else:
        held[0] = False

    if keys[pygame.K_ESCAPE]:
        pygame.quit()



    """if keys[pygame.K_SPACE]:
        player.setAttackBox()"""


    if keys[pygame.K_SPACE] and not held[1] and buffer.check():
        buffer.reset()
        player.setAttackBox()
        held[1] = True

    elif keys[pygame.K_SPACE]:
        pass
    else:
        held[1] = False

    buffer.tick()