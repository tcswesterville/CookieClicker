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

# Upgrades (relative path, price, adder, multiplier, addition per unit, non cummulative multiplier for addition per unit, unit is me, unlock condition)

CLICKERUPGRADES = [
    ("reinforcedindexfinger.png", 100, 0, 2, 0, 1, False, 1),
    ("carpaltunnelpreventioncream.png", 500, 0, 2, 0, 1, False, 1),
    ("ambidextrous.png", 10000, 0, 2, 0, 1, False, 10),
    ("thousandfingers.png", 100000, 0, 1, 0.1, 1, False, 25),
    ("millionfingers.png", 10000000, 0, 1, 0, 5, False, 50),
    ("billionfingers.png", 100000000, 0, 1, 0, 10, False, 100),
    ("trillionfingers.png", 1000000000, 0, 1, 0, 20, False, 150),
    ("quadrillionfingers.png", 10000000000, 0, 1, 0, 20, False, 200),
    ("quintillionfingers.png", 10000000000000, 0, 1, 0, 20, False, 250),
    ("sextillionfingers.png", 10000000000000000, 0, 1, 0, 20, False, 300),
    ("septillionfingers.png", 10000000000000000000, 0, 1, 0, 20, False, 350),
    ("octillionfingers.png", 10000000000000000000000, 0, 1, 0, 20, False, 400),
    ("nonillionfingers.png", 10000000000000000000000000, 0, 1, 0, 20, False, 450),
    ("decillionfingers.png", 10000000000000000000000000000, 0, 1, 0, 20, False, 500),
    ("undecillionfingers.png", 10000000000000000000000000000000, 0, 1, 0, 20, False, 550),
]

UPGRADEBUTTONHEGIHT = 50

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