# Score tracking variables
cookies = 10000000000000000
score = 0

shopButtons = []
upgradeLines = []
powerUps = []
scrollHandler = None

# Screen tracking varaible
currentScreen = "mainScreen"
shopEnabled = False
upgradeshopEnabled = False

lastEventTime = 0

# PowerUP
cursorPower = 0.1

grandma = 0
grandmaPower = 1

farms = 0
farmPower = 8

mines = 0
minePower = 47

factories = 0
factoryPower = 260

banks = 0
bankPower = 1400

temples = 0
templePower = 7800

wizardTowers = 0
wizardTowerPower = 44000

shipments = 0
shipmentPower = 260000

alchemyLabs = 0
alchemyLabPower = 1600000

portals = 0
portalPower = 10000000

timeMachines = 0
timeMachinePower = 65000000

antimatterCondensers = 0
antimatterCondenserPower = 430000000

prisms = 0
prismPower = 2900000000

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
    return cursorPower + farms + mines + factories + banks + temples + wizardTowers + shipments + alchemyLabs + portals + timeMachines + antimatterCondensers + prisms + chanceMakers + fractalEngines + javascriptConsoles + idleverses + cortexBakers + yous

