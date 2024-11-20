import pygame
import sys
import math
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

cursorPurchaseButton = button.Button(
    x=screen_width - shopWidth,
    y=0,
    width = shopWidth,
    height = 50,
    backgroundImage=cursorPurchaseButtonImage,
    text=cursorPrice
)

goldercursorPurchaseButton = button.Button(
    x=screen_width - shopWidth,
    y=cursorPurchaseButton.height,
    width = shopWidth,
    height = 50,
    backgroundImage=goldenCursorPurchaseButtonImage,
    text=goldenCursorPrice
)

farmPurchaseButton = button.Button(
    x=screen_width - shopWidth,
    y=goldercursorPurchaseButton.height + goldercursorPurchaseButton.y,
    width = shopWidth,
    height = 50,
    backgroundImage=farmPurchaseButtonImage,
    text=farmPrice
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
        if currentScreen == "mainScreen":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for main button click
                mousePosition = pygame.mouse.get_pos()
                if mainButton.onClicked(event, mousePosition):
                    cookies += cursorPower
                    score += cursorPower
                if (shopButton.onClicked(event, mousePosition)):
                    print("Shop Button Clicked:")
                    print(f"X: {mousePosition[0]}, Y: {mousePosition[1]}")
                    shopEnabled = not shopEnabled
                    print("Enabling Shop") if shopEnabled == True else print("Disabling Shop")
                if(shopEnabled == True):
                    if(cursorPurchaseButton.onClicked(event, mousePosition) and cookies >= cursorPrice):
                        cookies -= cursorPrice
                        cursorPower += 1
                        cursorPrice = int(cursorPrice * (math.pow(1.10, cursorPower - 1)))
                        cursorPurchaseButton.resetText(cursorPrice)
                    elif(goldercursorPurchaseButton.onClicked(event, mousePosition) and cookies >= goldenCursorPrice):
                        cookies -= goldenCursorPrice
                        goldenCursors += 1
                        goldenCursorPrice = int(goldenCursorPrice * (math.pow(1.10, goldenCursors)))
                        goldercursorPurchaseButton.resetText(goldenCursorPrice)
                    elif(farmPurchaseButton.onClicked(event, mousePosition) and cookies >= farmPrice):
                        cookies -= farmPrice
                        farms += 1
                        farmPrice = int(farmPrice * (math.pow(1.10, farms)))
                        farmPurchaseButton.resetText(farmPrice)


    # Render main screen specific things
    if currentScreen == "mainScreen":
        # Render mainBackground
        screen.blit(mainBackground, (0, 0))

        # Render main button
        mainButton.renderButton(screen)

        # Shop specific items
        
        if(shopEnabled == True):
            pygame.draw.rect(screen, BLACK, (screen_width - shopWidth, 0, shopWidth, shopHeight))
            cursorPurchaseButton.renderButton(screen)
            goldercursorPurchaseButton.renderButton(screen)
            farmPurchaseButton.renderButton(screen)
        # Render Shop Button
        shopButton.renderButton(screen)

    # Screen agnostic elements

    # Render cookie count
    cookieText = mainFont.render(f"Cookies: {cookies}", True, (255, 255, 255))
    screen.blit(cookieText, (10, 10))

    # Render score
    scoreText = mainFont.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(scoreText, (10, 10 + mainFontSize))

    # Update the display
    pygame.display.flip()

    # Per second events
    if (pygame.time.get_ticks() - lastEventTime >= 1000):
        cookies += goldenCursors + farms * 10
        score += goldenCursors + farms * 10
        lastEventTime = pygame.time.get_ticks()

    # Limit the frame rate
    clock.tick(60)  # Cap the frame rate at 60 FPS

# Quit from running state
pygame.quit()
sys.exit()
