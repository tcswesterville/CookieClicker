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
upgradeShopButtonImage = "Assets/Images/upgradeShopButton"
cursorPurchaseButtonImage = "Assets/Images/Cursor.png"
grandmaPurchaseButtonImage = "Assets/Images/grandma.png"
farmPurchaseButtonImage = "Assets/Images/farm.png"
minePurchaseButtonImage = "Assets/Images/mine.png"
factoryPurchaseButtonImage = "Assets/Images/factory.png"
bankPurchaseButtonImage = "Assets/Images/Bank.png"
templePurchaseButtonImage = "Assets/Images/temple.png"
wizardTowerPurchaseButtonImage = "Assets/Images/wizardTower.png"

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