# Score tracking variables
cookies = 1000
score = 0

shopButtons = []
powerUps = []

# Screen tracking varaible
currentScreen = "mainScreen"
shopEnabled = False
upgradeshopEnabled = False

lastEventTime = 0

# PowerUP
cursorPower = 1

goldenCursors = 0
goldenCursorPower = 0

farms = 0
farmPower = 0

mines = 0
minePower = 0

factories = 0
factoryPower = 0

banks = 0
bankPower = 0

temples = 0
templePower = 0

wizardTowers = 0
wizardTowerPower = 0

shipments = 0
shipmentPower = 0

alchemyLabs = 0
alchemyLabPower = 0

portals = 0
portalPower = 0

timeMachines = 0
timeMachinePower = 0

antimatterCondensers = 0
antimatterCondensrPower = 0

prisms = 0
prismPower = 0

chanceMakers = 0
chanceMakerPower = 0

fractalEngines = 0
fractalEnginePower = 0

javascriptConsoles = 0
javascriptConsolePower = 0

idleverses = 0
idleversePower = 0

cortexBakers = 0
cortexBakerPower = 0

yous = 0
youPower = 0

kittenUpgrades = 0

# Acheivements
acheivements = 0

# Power up power calculations
def getBuildingCount():
    return cursorPower + goldenCursors + farms + mines + factories + banks + temples + wizardTowers + shipments + alchemyLabs + portals + timeMachines + antimatterCondensers + prisms + chanceMakers + fractalEngines + javascriptConsoles + idleverses + cortexBakers + yous

def getGoldenCursorPower():
    return goldenCursors