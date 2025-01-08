import pygame
import sys
import math
import buttonCircle
import button
from definitions import *
import userVariables
import powerUp
import schedule

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

shopButtons = []
powerUps = []

shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=0,
    width = shopWidth,
    height = 50,
    backgroundImage=cursorPurchaseButtonImage,
    text=cursorPrice
))
powerUps.append(powerUp.PowerUP(shopButtons[0], 15, False, 1, 0))

shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=shopButtons[0].height,
    width = shopWidth,
    height = 50,
    backgroundImage=goldenCursorPurchaseButtonImage,
    text=goldenCursorPrice
))
powerUps.append(powerUp.PowerUP(shopButtons[1], 100, True, 1, 1))

shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=shopButtons[1].height + shopButtons[1].y,
    width = shopWidth,
    height = 50,
    backgroundImage=farmPurchaseButtonImage,
    text=farmPrice
))
powerUps.append(powerUp.PowerUP(shopButtons[2], 1000, True, 10, 1))

shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=shopButtons[2].height + shopButtons[2].y,
    width = shopWidth,
    height = 50,
    backgroundImage=minePurchaseButtonImage,
    text=minePrice
))
powerUps.append(powerUp.PowerUP(shopButtons[3], 10000, True, 100, 1))

shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=shopButtons[3].height + shopButtons[3].y,
    width = shopWidth,
    height = 50,
    backgroundImage=factoryPurchaseButtonImage,
    text=factoryPrice
))
powerUps.append(powerUp.PowerUP(shopButtons[4], 100000, True, 1000, 1))

shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=shopButtons[4].height + shopButtons[4].y,
    width=shopWidth,
    height=50,
    backgroundImage=bankPurchaseButtonImage,
    text=bankPrice
))
powerUps.append(powerUp.PowerUP(shopButtons[5], 1000000, True, 10000, 1))

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
        if currentScreen == "mainScreen":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for main button click
                mousePosition = pygame.mouse.get_pos()
                if mainButton.onClicked(event, mousePosition):
                    userVariables.cookies += userVariables.cursorPower
                    userVariables.score += userVariables.cursorPower
                if (shopButton.onClicked(event, mousePosition)):
                    print("Shop Button Clicked:")
                    print(f"X: {mousePosition[0]}, Y: {mousePosition[1]}")
                    userVariables.shopEnabled = not userVariables.shopEnabled
                    print("Enabling Shop") if userVariables.shopEnabled == True else print("Disabling Shop")
                if(userVariables.shopEnabled == True):
                    for powerup in powerUps:
                        powerup.purchase(event, mousePosition)

    # Render main screen specific things
    if currentScreen == "mainScreen":
        # Render mainBackground
        screen.blit(mainBackground, (0, 0))

        # Render main button
        mainButton.renderButton(screen)

        # Shop specific items
        
        if(userVariables.shopEnabled == True):
            pygame.draw.rect(screen, BLACK, (screen_width - shopWidth, 0, shopWidth, shopHeight))
            for button in shopButtons:
                button.renderButton(screen)
        # Render Shop Button
        shopButton.renderButton(screen)

    # Screen agnostic elements

    # Render cookie count
    cookieText = mainFont.render(f"Cookies: {userVariables.cookies}", True, (255, 255, 255))
    screen.blit(cookieText, (10, 10))

    # Render score
    scoreText = mainFont.render(f"Score: {userVariables.score}", True, (255, 255, 255))
    screen.blit(scoreText, (10, 10 + mainFontSize))

    # Update the display
    pygame.display.flip()

    # Scheduled events
    schedule.run_pending()

    # Limit the frame rate
    clock.tick(60)  # Cap the frame rate at 60 FPS

# Quit from running state
pygame.quit()
sys.exit()
