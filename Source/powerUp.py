from button import *
import userVariables
from definitions import *
import upgrade
import schedule

class PowerUP():
    def __init__(self,
                 upgradeButtonLiney: int,
                 upgradeButtonLinePath: str,
                 metaData,
                 button: Button, 
                 initialCost: int, 
                 timedEvent: bool, 
                 powerIncrement = 1, 
                 power = 0, 
                 intervalSeconds = 1, 
                 childButton = -1, 
                 ):
        self.button = button
        self.cost = initialCost
        self.hasTimedEvent = timedEvent
        self.powerIncrement = powerIncrement
        self.power = power
        self.childButton = childButton
        self.amount = 0
        if (metaData != None):
            self.upgradeButtonLine = upgrade.UpgradeLine(upgradeButtonLiney, upgradeButtonLinePath, self, metaData)
        else:
            self.upgradeButtonLine = None

        self.initiateTimedEvent(intervalSeconds)
    def addUpgrade(self, upgrade):
        self.upgradeButtonLine = upgrade
    def calculatePrice(self):
        self.cost *= 1.10
        self.cost = int(self.cost)
    def setPrice(self):
        self.calculatePrice()
        self.button.resetText(self.cost)

    def purchase(self, event, mousePosition):
        if (self.button.onClicked(event, mousePosition)):
            if self.button.unlocked and userVariables.cookies >= self.cost:
                userVariables.cookies -= self.cost
                self.amount += 1
                self.power += self.powerIncrement
                self.setPrice()
                self.unlockPowerup()
    def purchaseUpgrade(self, event, mousePosition):
        if (self.upgradeButtonLine != None and self.upgradeButtonLine.benefitingPowerUp == self):
            self.upgradeButtonLine.purchase(event, mousePosition)
    def unlockPowerup(self):
        if (self.childButton != -1):
            userVariables.shopButtons[self.childButton].unlocked = True
    def effect(self):
        if (self.upgradeButtonLine != None):
            power = self.upgradeButtonLine.applyUpgrade(self.power)
            userVariables.cookies += power
            userVariables.score += power
        else:
            userVariables.cookies += self.power
            userVariables.score += self.power
    def scheduledJob(self):
        if (self.upgradeButtonLine != None):
            print(self.upgradeButtonLine.applyUpgrade(self.power))
    def initiateTimedEvent(self, intervalSeconds: int):
        if (self.hasTimedEvent):
            schedule.every(intervalSeconds).seconds.do(self.effect)
        schedule.every(1).seconds.do(self.scheduledJob)
    def getAmount(self):
        return self.amount