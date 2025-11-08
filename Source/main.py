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

def create_category(ID, next_ID, price, cps, image, text, unlocking_ID, upgrade=None):
    userVariables.shopButtons.append(button.Button(
        x=screen_width - shopWidth,
        y=userVariables.shopButtons[ID].height + userVariables.shopButtons[ID].y,
        width=shopWidth,
        height = shopItemHeight,
        backgroundImage=image,
        text=text,
        unlocked=False
    ))
    userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[next_ID], price, True, cps, 0, 1, unlocking_ID, upgrade))


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

# Cursor Upgrade Line
userVariables.upgradeLines.append(upgrade.UpgradeLine(0, CLICKERUPGRADEPATH, CLICKERUPGRADES, 0, [0, 1]))

# Manual Clicker PowerUp
userVariables.powerUps.append(powerUp.PowerUP(None, 0, False, 0, 1, 0, -1))

# Cursor
userVariables.shopButtons.append(button.Button(
x=screen_width - shopWidth,
y=0,
width = shopWidth,
height = shopItemHeight,
backgroundImage=cursorPurchaseButtonImage,
text=cursorPrice
))
userVariables.powerUps.append(powerUp.PowerUP(userVariables.shopButtons[0], cursorPrice, True, 0.1, 0, 1, 1, userVariables.upgradeLines[0]))

# Grandma Upgrade Line
userVariables.upgradeLines.append(upgrade.UpgradeLine(50, GRANDMAUPGRADEPATH, GRANDMAUPGRADES, 0, []))

# Grandma
create_category(0,1, grandmaPrice, userVariables.grandmaPower, grandmaPurchaseButtonImage, grandmaPrice, 2, userVariables.upgradeLines[1])

# Farm
create_category(1, 2, farmPrice, userVariables.farmPower, farmPurchaseButtonImage, farmPrice, 3)

# Mine
create_category(2, 3, minePrice, userVariables.minePower, minePurchaseButtonImage, minePrice, 4)

# Factory
create_category(3, 4, factoryPrice, userVariables.factoryPower, factoryPurchaseButtonImage, factoryPrice, 5)

# Bank
create_category(4, 5, bankPrice, userVariables.bankPower, bankPurchaseButtonImage, bankPrice, 6)

# Temple
create_category(5, 6, templePrice, userVariables.templePower, templePurchaseButtonImage, templePrice, 7)

# Wizard Tower
create_category(6, 7, wizardtowerPrice, userVariables.wizardTowerPower, wizardTowerPurchaseButtonImage, wizardtowerPrice, 8)

# Shipment
create_category(7, 8, ShipmentPrice, userVariables.shipmentPower, ShipmentPurchaseButtonImage, ShipmentPrice, 9)

# Alchemy Lab
create_category(8, 9, AlchemyLabPrice, userVariables.alchemyLabPower, AlchamyLabPurchaseButtonImage, AlchemyLabPrice, 10)

# Portal
create_category(9, 10, PortalPrice, userVariables.portalPower, PortalPurchaseButtonImage, PortalPrice, 11)

# TimeMachine
create_category(10, 11, TimeMachinePrice, userVariables.timeMachinePower, TimeMachinePurchaseButtonImage, TimeMachinePrice, 12)

# AntiMatter Condenser
create_category(11, 12, AntiMatterCondenserPrice, userVariables.antimatterCondenserPower, AntiMatterCondenserPurchaseButtonImage, AntiMatterCondenserPrice, 13)

# Prism
create_category(12, 13, PrismPrice, userVariables.prismPower, PrismPurchaseButtonImage, PrismPrice, -1)

# numbers, price variables, cookies per second, image, text

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
