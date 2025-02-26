from pygame import font

# Initial Screen dimensions
screen_width = 800
screen_height = 600

# Shop dimensions
shopWidth = screen_width // 3
shopHeight = screen_height // (3 / 4)

# Text
APPLICATION_CAPTION = "Cookie Clicker"

# Image Imports
mainBackgroundImage = "Assets/Images/CookieClickerBackground01.webp"
mainButtonImage = "Assets/Images/cookieButton.png"
shopButtonImage = "Assets/Images/shopButton.png"
upgradeShopButtonImage = "Assets/Images/upgradeShopButton.png"
cursorPurchaseButtonImage = "Assets/Images/Cursor.png"
grandmaPurchaseButtonImage = "Assets/Images/grandma.png"
farmPurchaseButtonImage = "Assets/Images/farm.png"
minePurchaseButtonImage = "Assets/Images/mine.png"
factoryPurchaseButtonImage = "Assets/Images/factory.png"
bankPurchaseButtonImage = "Assets/Images/Bank.png"
templePurchaseButtonImage = "Assets/Images/temple.png"
wizardTowerPurchaseButtonImage = "Assets/Images/wizardTower.png"

UPGRADESPATH = "Assets/Images/Upgrades/"
CLICKERUPGRADEPATH = UPGRADESPATH + "Clicker/"
CLICKERUPGRADES = {(CLICKERUPGRADEPATH + "reinforcedindexfinger.png", 10000000000000000)}

# Upgrades (relative path, price, adder, multiplier, addition per unit, multiplier per unit, unit is me, unlock condition)
CLICKERUPGRADES = {
    ("reinforcedindexfinger.png", 100, 0, 2, 0, 1, False, 1),
    ("carpaltunnel.png", 500, 0, 2, 0, 1, False, 1),
    ("ambidextrous.png", 10000, 0, 2, 0, 1, False, 10),
    ("thousandfingers.png", 100000, 0, 1, 0.1, 1, False),
    ("millionfingers.png", 10000000, 0, 1, 0, 5, False),
    ("billionfingers.png", 100000000, 0, 1, 0, 10, False),
    ("trillionfingers.png", 1000000000, 0, 1, 0, 20, False),
    ("quadrillionfingers.png", 10000000000, 0, 1, 0, 20, False),
    ("quintillionfingers.png", 10000000000000, 0, 1, 0, 20, False),
    ("sextillionfingers.png", 10000000000000000, 0, 1, 0, 20, False),
    ("septillionfingers.png", 10000000000000000000, 0, 1, 0, 20, False),
    ("octillionfingers.png", 10000000000000000000000, 0, 1, 0, 20, False),
    ("nonillionfingers.png", 10000000000000000000000000, 0, 1, 0, 20, False),
    ("decillionfingers.png", 10000000000000000000000000000, 0, 1, 0, 20, False),
    ("undecillionfingers.png", 10000000000000000000000000000000, 0, 1, 0, 20, False),
}

# Fonts
font.init()
mainFontSize = 36
mainFont = font.Font(None, mainFontSize)

# Colors
BLACK = (0, 0, 0)

# Shop Price
cursorPrice = 15
grandmaPrice = 100
farmPrice = 1100
minePrice = 12000
factoryPrice = 130000
bankPrice = 1400000
templePrice = 20000000
wizardtowerPrice = 330000000