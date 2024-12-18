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
cursorPurchaseButtonImage = "Assets/Images/Cursor.png"
goldenCursorPurchaseButtonImage = "Assets/Images/goldencursor.png"
farmPurchaseButtonImage = "Assets/Images/farm.png"
minePurchaseButtonImage = "Assets/Images/mine.png"
factoryPurchaseButtonImage = "Assets/Images/factory.png"

# Fonts
font.init()
mainFontSize = 36
mainFont = font.Font(None, mainFontSize)

# Colors
BLACK = (0, 0, 0)

# Shop Price
cursorPrice = 15
goldenCursorPrice = 100
farmPrice = 1000
minePrice = 10000
factoryPrice = 100000