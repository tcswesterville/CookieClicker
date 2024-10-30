import pygame
import sys
import buttonCircle
import button
from definitions import *
from userVariables import *

# Load and scale the mainBackground image
mainBackground = pygame.image.load(mainBackgroundImage)
mainBackground = pygame.transform.scale(mainBackground, (screen_width, screen_height))

# Initialize the screen
currentScreen = "mainScreen"

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
    x=screen_width - (screen_width // 8) - int(screen_width * 0.0125),
    y=screen_height - ((screen_height // 8) / 2) - int(screen_height  * (1 / 36)),
    width = screen_width // 8,
    height = screen_height // 8,
    backgroundImage = shopButtonImage
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
        if currentScreen == "main":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for main button click
                mousePosition = pygame.mouse.get_pos()
                if mainButton.onClicked(event, mousePosition):
                    cookies += 1
                    score += 1
                if shopButton.onClicked(event, mousePosition):
                    print("Shop Button Clicked:")
                    print(f"X: {mousePosition[0]}, Y: {mousePosition[1]}")
                    currentScreen = "shopScreen"
                    print("Switching to screen: shopScreen")
        elif currentScreen == "shopScreen":
            pass

    # Render main screen specific things
    if currentScreen == "mainScreen":
        # Render mainBackground
        screen.blit(mainBackground, (0, 0))

        # Render main button
        mainButton.renderButton(screen)

        # Render Shop Button
        shopButton.renderButton(screen)
    
    # Render shop screen specific things
    elif currentScreen == "shopScreen":
        screen.fill(0, 0, 0)

    # Screen agnostic elements

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

# Quit from running state
pygame.quit()
sys.exit()
