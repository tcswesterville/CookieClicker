import pygame
import sys
import math
import buttonCircle
import button
from definitions import *
import userVariables
import powerUp
import upgrade
import scrollHandler
import helperFunctions
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
    height = shopButtonHeight,
    backgroundImage = shopButtonImage
)

upgradeShopButton = button.Button(
    x=0,
    y=screen_height - ((screen_height // 5) / 2) - int(screen_height  * (1 / 25)),
    width = screen_width // 5,
    height = shopButtonHeight*1.5,
    backgroundImage = upgradeShopButtonImage
)

# Clicker Upgrade Line - Amount only affected by auto clicker amount
userVariables.upgradeLines.append(upgrade.UpgradeLine(0, CLICKERUPGRADEPATH, CLICKERUPGRADES, 0, [0, 1]))

# Manual Clicker PowerUp
userVariables.powerUps.append(powerUp.PowerUP(None, 0, False, 0, 1, 0, -1, userVariables.upgradeLines[0]))

# Shop Button for Auto Cursor PowerUp
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=0,
    width = shopWidth,
    height = shopItemHeight,
    backgroundImage=cursorPurchaseButtonImage,
    text=cursorPrice
))

# Auto Cursor PowerUp (Cursor - not your mouse)
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[0], cursorPrice, True, 0.1, 0, 1, 1, userVariables.upgradeLines[0]))

# Clicker Upgrade Line - Amount only affected by auto clicker amount
userVariables.upgradeLines.append(upgrade.UpgradeLine(50, GRANDMAUPGRADEPATH, GRANDMAUPGRADES, 0, []))

# Grandma Shop Button
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[0].height + userVariables.shopButtons[0].y,
    width = shopWidth,
    height = shopItemHeight,
    backgroundImage=grandmaPurchaseButtonImage,
    text=grandmaPrice,
    unlocked=False
))
# Grandma PowerUp
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[1], grandmaPrice, True, 1, 0, 1, 2, userVariables.upgradeLines[1]))

# Farm Shop Button
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[1].height + userVariables.shopButtons[1].y,
    width = shopWidth,
    height = shopItemHeight,
    backgroundImage=farmPurchaseButtonImage,
    text=farmPrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[2], farmPrice, True, 8, 0, 1, 3))

# Mine Shop Button
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[2].height + userVariables.shopButtons[2].y,
    width = shopWidth,
    height = shopItemHeight,
    backgroundImage=minePurchaseButtonImage,
    text=minePrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[3], minePrice, True, 47, 0, 1, 4))

# Factory Shop Button
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[3].height + userVariables.shopButtons[3].y,
    width = shopWidth,
    height = shopItemHeight,
    backgroundImage=factoryPurchaseButtonImage,
    text=factoryPrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[4], factoryPrice, True, 260, 0, 1, 5))

# Bank Shop Button
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[4].height + userVariables.shopButtons[4].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=bankPurchaseButtonImage,
    text=bankPrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[5], bankPrice, True, 1400, 0, 1, 6))

# Temple Shop Button
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[5].height + userVariables.shopButtons[5].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=templePurchaseButtonImage,
    text=templePrice,
    unlocked=False
))

userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[6], templePrice, True, 7800, 0, 1, 7))

# Wizard Tower Shop Button
userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[6].height + userVariables.shopButtons[6].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=wizardTowerPurchaseButtonImage,
    text=wizardtowerPrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[7], wizardtowerPrice, True, 44000, 0, 1, 8))

userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[7].height + userVariables.shopButtons[7].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=ShipmentPurchaseButtonImage,
    text=ShipmentPrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[8], ShipmentPrice, True, 260000, 0, 1, 9))

userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[8].height + userVariables.shopButtons[8].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=AlchamyLabPurchaseButtonImage,
    text=AlchamyLabPrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[9], AlchamyLabPrice, True, 1600000, 0, 1, 10))

userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[9].height + userVariables.shopButtons[9].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=PortalPurchaseButtonImage,
    text=PortalPrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[10], PortalPrice, True, 10000000, 0, 1, 11))

userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[10].height + userVariables.shopButtons[10].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=TimeMachinePurchaseButtonImage,
    text=TimeMachinePrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[11], TimeMachinePrice, True, 65000000, 0, 1, -1))

userVariables.shopButtons.append(button.Button(
    x=screen_width - shopWidth,
    y=userVariables.shopButtons[11].height + userVariables.shopButtons[11].y,
    width=shopWidth,
    height = shopItemHeight,
    backgroundImage=AntimPurchaseButtonImage,
    text=TimeMachinePrice,
    unlocked=False
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[12], AntimPrice, True, 430000000, 0, 1, -1))

userVariables.scrollHandler = scrollHandler.ScrollHandler(
    userVariables.shopButtons,
    xStart=screen_width - shopWidth,
    yStart=0,
    xOffset=0,
    yOffset=shopItemHeight,
    screenHeight=screen_height,
    min_x = screen_width - shopWidth,
    max_x = screen_width
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check for main button click
                mousePosition = pygame.mouse.get_pos()
                if mainButton.onClicked(event, mousePosition):
                    userVariables.powerUps[0].effect()
                if (shopButton.onClicked(event, mousePosition)):
                    userVariables.shopEnabled = not userVariables.shopEnabled
                if (upgradeShopButton.onClicked(event, mousePosition)):
                    userVariables.upgradeshopEnabled = not userVariables.upgradeshopEnabled
                if(userVariables.shopEnabled == True):
                    for powerup in userVariables.powerUps:
                        powerup.purchase(event, mousePosition)
                if(userVariables.upgradeshopEnabled == True):
                    for ugrade in userVariables.upgradeLines:
                        ugrade.purchase(event, mousePosition)
            elif event.type==pygame.MOUSEWHEEL:
                userVariables.scrollHandler.scroll(event.y)

    # Render main screen specific things
    if currentScreen == "mainScreen":
        # Render mainBackground
        screen.blit(mainBackground, (0, 0))

        # Render main button
        mainButton.renderButton(screen)

        # Shop specific items
        
        if(userVariables.shopEnabled == True):
            pygame.draw.rect(screen, BLACK, (screen_width - shopWidth, 0, shopWidth, shopHeight))
            userVariables.scrollHandler.renderButtons(screen)
        if(userVariables.upgradeshopEnabled == True):
            pygame.draw.rect(screen, BLACK, (0, 0, shopWidth, shopHeight))
            for upgrade in userVariables.upgradeLines:
                upgrade.update(screen, userVariables.powerUps)
        # Render Shop Button
        shopButton.renderButton(screen)
        upgradeShopButton.renderButton(screen)

    # Screen agnostic elements

    # Render cookie count
    cookieText = mainFont.render(f"Cookies: {helperFunctions.simplifyNumber(userVariables.cookies)}", True, (255, 255, 255))
    cookieTextRectangle = cookieText.get_rect(center=(screen_width // 2, 154))
    screen.blit(cookieText, cookieTextRectangle)

    # Render score
    scoreText = mainFont.render(f"Score: {helperFunctions.simplifyNumber(userVariables.score)}", True, (255, 255, 255))
    scoreTextRectangle = scoreText.get_rect(center=(screen_width // 2, 10 + mainFontSize))
    screen.blit(scoreText, (scoreTextRectangle))

    # Update the display
    pygame.display.flip()

    # Scheduled events
    schedule.run_pending()

    # Limit the frame rate
    clock.tick(60)  # Cap the frame rate at 60 FPS

# Quit from running state
pygame.quit()
sys.exit()
