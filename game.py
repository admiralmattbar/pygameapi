import pygame, sys, time
from pygame.locals import *

pygame.init()


#Constants
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0,  0, 255)
FUSCHIA = (255, 0, 255)
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
FPS = 60
fpsClock = pygame.time.Clock()

#Variables
sprites = []
TITLE = ""
WIDTH = 400
HEIGHT = 300

#Functions


def addSprite(imageName):
    sp = pygame.image.load(imageName)
    sprites.append(sp)
    return sp

def runGame():
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption(TITLE)
    

'''
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('That darn cat!', True, RED, BLACK)
textRect = text.get_rect()
textRect.center = (200, 150)

sound = pygame.mixer.Sound('hushbomb.wav')
sound.play()

direction = 'right'
rectx = 10
recty = 10

rect = pygame.Rect(rectx, recty, 10, 10)
'''

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(text, textRect)
    pixObj = pygame.PixelArray(DISPLAYSURF)
    pixObj[200][200] = BLACK
    pixObj[201][200] = BLACK
    pixObj[202][200] = BLACK
    pixObj[203][200] = BLACK
    pixObj[200][201] = BLACK
    pixObj[200][202] = BLACK
    pixObj[200][203] = BLACK

    del pixObj

    if direction == 'right':
        rectx += 5
        if rectx > 375:
            direction = 'down'
    elif direction == 'down':
        recty += 5
        if recty > 275:
            direction = 'left'
    elif direction == 'left':
        rectx -= 5
        if rectx < 10:
            direction = 'up'
    elif direction == 'up':
        recty -= 5
        if recty < 10:
            direction = 'right'

    pygame.draw.rect(DISPLAYSURF, RED, (rectx, recty, 10, 10))

    DISPLAYSURF.blit(catImg, (rectx - 25, 50))

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)


if __name__ == "__main__":
    main()
