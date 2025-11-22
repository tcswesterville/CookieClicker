from pygame import font

# Initial Screen dimensions
screen_width = 800
screen_height = 600

# Shop dimensions
shopWidth = screen_width // 3
shopHeight = screen_height

shopButtonHeight = screen_height // 8

shopItemHeight = 50

shopItemCount = 1 + (shopHeight - shopButtonHeight) // shopItemHeight

# Text
APPLICATION_CAPTION = "Cookie Clicker"

POWERUPSPATH = "Assets/Images/PowerUps/"
UPGRADESPATH = "Assets/Images/Upgrades/"


# Image Imports
mainBackgroundImage = "Assets/Images/CookieClickerBackground01.webp"
mainButtonImage ="Assets/Images/cookieButton.png"
shopButtonImage = "Assets/Images/shopButton.png"
upgradeShopButtonImage = "Assets/Images/upgradeShopButton.png"

# PowerUp Images (relative path)
cursorPurchaseButtonImage = POWERUPSPATH + "Cursor.png"
grandmaPurchaseButtonImage = POWERUPSPATH + "grandma.png"
farmPurchaseButtonImage =  POWERUPSPATH + "farm.png"
minePurchaseButtonImage =  POWERUPSPATH + "mine.png"
factoryPurchaseButtonImage =  POWERUPSPATH + "factory.png"
bankPurchaseButtonImage =  POWERUPSPATH + "Bank.png"
templePurchaseButtonImage =  POWERUPSPATH + "temple.png"
wizardTowerPurchaseButtonImage =  POWERUPSPATH + "wizardTower.png"
ShipmentPurchaseButtonImage =  POWERUPSPATH + "Shipment.png"
AlchamyLabPurchaseButtonImage =  POWERUPSPATH + "AlchemyLab.png"
PortalPurchaseButtonImage =  POWERUPSPATH + "Portal.png"
TimeMachinePurchaseButtonImage =  POWERUPSPATH + "TimeMachine.png"
AntiMatterCondenserPurchaseButtonImage =  POWERUPSPATH + "Antim.png"
PrismPurchaseButtonImage = POWERUPSPATH + "Prism.png"

CLICKERUPGRADEPATH = UPGRADESPATH + "Clicker/"
GRANDMAUPGRADEPATH = UPGRADESPATH + "Grandma/"

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

GRANDMAUPGRADES = [
    ("ForwardsFromGrandma.png", 1000, 0, 2, 0, 1, False, 1),
    ("SteelPlatedRollingPins.png", 5000, 0, 2, 0, 1, False, 5),
    ("LubricatedDentures.png", 50000, 0, 2, 0, 1, False, 25),
    ("PruneJuice.png", 5000000, 0, 2, 0, 1, False, 50),
    ("DoubleThickGlasses.png", 500000000, 0, 2, 0, 1, False, 100),
    ("AgingAgents.png", 50000000000, 0, 2, 0, 1, False, 150),
    ("XtremeWalkers.png", 50000000000000, 0, 2, 0, 1, False, 200),
    ("TheUnbridling.png", 50000000000000000, 0, 2, 0, 1, False, 250),
    ("ReverseDementia.png", 50000000000000000000, 0, 2, 0, 1, False, 300),
    ("TimeproofHairDyes.png", 50000000000000000000000, 0, 2, 0, 1, False, 350),
    ("GoodManners.png", 500000000000000000000000000, 0, 2, 0, 1, False, 400),
    ("GenerationDegeration.png", 5000000000000000000000000000, 0, 2, 0, 1, False, 450),
    ("Visits.png", 50000000000000000000000000000000, 0, 2, 0, 1, False, 500),
    ("KitchenCabinets.png", 500000000000000000000000000000000000, 0, 2, 0, 1, False, 550),
    ("FoamTippedCanes.png", 5000000000000000000000000000000000000, 0, 2, 0, 1, False, 600),
]

FARMUPGRADES = [
    ("CheapHoes.png", 1000, 0, 2, 0, 1, False, 1),
    ("Fertilizer", 5000, 0, 2, 0, 1, False, 5),
    ("CookieTrees.png", 50000, 0, 2, 0, 1, False, 25),
    ("Genetically-ModifiedCookies.png", 5000000, 0, 2, 0, 1, False, 50),
    ("GingerbreadScarecrows.png", 500000000, 0, 2, 0, 1, False, 100),
    ("PulsarSprinklers.png", 50000000000, 0, 2, 0, 1, False, 150),
    ("FudgeFungus.png", 50000000000000, 0, 2, 0, 1, False, 200),
    ("WheatTriffids.png", 50000000000000000, 0, 2, 0, 1, False, 250),
    ("HumanPesticides.png", 50000000000000000000, 0, 2, 0, 1, False, 300),
    ("Barnstars.png", 50000000000000000000000, 0, 2, 0, 1, False, 350),
    ("Lindworms.png", 500000000000000000000000000, 0, 2, 0, 1, False, 400),
    ("GlobalSeedVault.png", 5000000000000000000000000000, 0, 2, 0, 1, False, 450),
    ("Reverse-Veganism.png", 50000000000000000000000000000000, 0, 2, 0, 1, False, 500),
    ("CookieMulch.png", 500000000000000000000000000000000000, 0, 2, 0, 1, False, 550),
    ("Self-DrivingTractors.png", 5000000000000000000000000000000000000, 0, 2, 0, 1, False, 600),
]

UPGRADEBUTTONHEGIHT = 100

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
ShipmentPrice = 5100000000
AlchemyLabPrice = 75000000000
PortalPrice = 1000000000000
TimeMachinePrice = 14000000000000
AntiMatterCondenserPrice = 170000000000000
PrismPrice = 2100000000000000