import pygame, sys
from definitions import *

background = pygame.image.load("Assets/Images/CookieClickerBackground01.webp")
background = pygame.transform.scale(background, (screen_width, screen_height))

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(APPLICATION_CAPTION)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    screen.blit(background, (0, 0))
    pygame.display.flip()

# Quit from running state
pygame.quit()
sys.exit()