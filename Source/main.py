import pygame
import sys
import buttonCircle
import button
from definitions import *
from userVariables import *

# Load and scale the background image
background = pygame.image.load(mainBackgroundImage)
background = pygame.transform.scale(background, (screen_width, screen_height))

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(APPLICATION_CAPTION)

# Create the main button
mainButton = buttonCircle.ButtonCircle(
    x=screen_width // 2,
    y=screen_height // 2,
    radius=((screen_height if screen_height <= screen_width else screen_width) // 2),
    backgroundImage=mainButtonImage
)

# Create the shop button
shopButton = button.Button(
    x=0,
    y=0,
    width=1000,
    height=1000,
    backgroundImage=shopButtonImage
)

# Set up clock for fixed frame rate
clock = pygame.time.Clock()
fixed_delta_time = 1 / 60  # Targeting 60 frames per second

# Initialize game variables
isRunning = True
while isRunning:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        # Check for main button click
        elif mainButton.onClicked(event, pygame.mouse.get_pos()):
            cookies += 1
            score += 1
            print(f"Main button clicked! Cookies: {cookies}, Score: {score}")  # Debugging

        # Check for shop button click
        elif shopButton.onClicked(event, pygame.mouse.get_pos()):
            print("Shop button clicked!")  # Debugging

    # Render background
    screen.blit(background, (0, 0))

    # Render buttons
    mainButton.renderButton(screen)
    shopButton.renderButton(screen)

    # Render cookie count
    cookieText = mainFont.render(f"Cookies: {cookies}", True, (255, 255, 255))
    screen.blit(cookieText, (10, 10))

    # Render score
    scoreText = mainFont.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(scoreText, (10, 10 + mainFontSize))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)  # Cap the frame rate at 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
