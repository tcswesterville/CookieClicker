from button import *
import userVariables
from definitions import *
import upgrade
import schedule

class PowerUP():
    def __init__(self,
                 button: Button, 
                 initialCost: int, 
                 timedEvent: bool, 
                 powerIncrement = 1, 
                 power = 0, 
                 intervalSeconds = 1, 
                 childButton = -1, 
                 upgrade: upgrade.UpgradeLine = None
                 ):
        self.button = button
        self.cost = initialCost
        self.hasTimedEvent = timedEvent
        self.powerIncrement = powerIncrement
        self.power = power
        self.childButton = childButton
        self.upgrade = upgrade
        self.amount = 0

        self.initiateTimedEvent(intervalSeconds)

    def calculatePrice(self):
        self.cost *= 1.10
        self.cost = int(self.cost)

    def setPrice(self):
        self.calculatePrice()
        self.button.resetText(self.cost)

    def purchase(self, event, mousePosition):
        if (self.button != None and self.button.onClicked(event, mousePosition)):
            if self.button.unlocked and userVariables.cookies >= self.cost:
                userVariables.cookies -= self.cost
                self.amount += 1
                if (self.upgrade != None):
                    print("h")
                    self.upgrade.IncrementAmountOfBenefittingPowerUp()
                self.power += self.powerIncrement
                self.setPrice()
                self.unlockPowerup()

    def unlockPowerup(self):
        if (self.childButton != -1):
            userVariables.shopButtons[self.childButton].unlocked = True

    def effect(self):
        if (self.upgrade != None):
            power = self.upgrade.applyUpgrade(self.power)
            userVariables.cookies += power
            userVariables.score += power
        else:
            userVariables.cookies += self.power
            userVariables.score += self.power

    def initiateTimedEvent(self, intervalSeconds: int):
        if (self.hasTimedEvent):
            schedule.every(intervalSeconds).seconds.do(self.effect)
    def getAmount(self):
        return self.amount