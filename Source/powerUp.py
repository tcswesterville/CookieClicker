from button import *
import userVariables
import schedule

class PowerUP():
    def __init__(self, button: Button, initialCost: int, timedEvent: bool, powerIncrement = 1, power = 0, intervalSeconds = 1, childButton = -1):
        self.button = button
        self.cost = initialCost
        self.hasTimedEvent = timedEvent
        self.powerIncrement = powerIncrement
        self.power = power
        self.childButton = childButton
        self.amount = 0
        if (intervalSeconds > 0):
            self.initiateTimedEvent(intervalSeconds)
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
    def unlockPowerup(self):
        if (self.childButton != -1):
            userVariables.shopButtons[self.childButton].unlocked = True
    def effect(self):
        userVariables.cookies += self.power
        userVariables.score += self.power
    def scheduledJob(self):
        print("Running Job")
    def initiateTimedEvent(self, intervalSeconds: int):
        if (self.hasTimedEvent):
            schedule.every(intervalSeconds).seconds.do(self.effect)
            #schedule.every(intervalSeconds).seconds.do(self.scheduledJob)
    def getAmount(self):
        return self.amount