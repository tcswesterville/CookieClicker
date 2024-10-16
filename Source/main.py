import pygame, sys
import buttonCircle
from definitions import *
from userVariables import *

background = pygame.image.load("Assets/Images/CookieClickerBackground01.webp")
background = pygame.transform.scale(background, (screen_width, screen_height))

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(APPLICATION_CAPTION)

mainButton = buttonCircle.ButtonCircle(
    x = screen_width // 2, 
    y = screen_height // 2, 
    radius = ((screen_height if screen_height <= screen_width else screen_width) // 2), 
    backgroundImage = "Assets/Images/cookieButton.png")

isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    screen.blit(background, (0, 0))
    mainButton.renderButton(screen)
    pygame.display.flip()

# Quit from running state
pygame.quit()
sys.exit()