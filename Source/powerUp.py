from button import *
import userVariables
import schedule

class PowerUP():
    def __init__(self, button: Button, initialCost: int, timedEvent: bool, power: int, intervalSeconds: int):
        self.button = button
        self.amount = 0
        self.cost = initialCost
        self.hasTimedEvent = timedEvent
        self.power = power
        self.initiateTimedEvent(intervalSeconds)
    def calculatePrice(self):
        self.cost *= 1.10
        self.cost = int(self.cost)
    def setPrice(self):
        self.calculatePrice()
        self.button.resetText(self.cost)
    def purchase(self, event, mousePosition):
        if (self.button.onClicked(event, mousePosition)):
            if userVariables.cookies >= self.cost:
                userVariables.cookies -= self.cost
                self.amount += 1
                self.setPrice()
    def effect(self):
        userVariables.cookies += self.power
        userVariables.score += self.power
    def initiateTimedEvent(self, intervalSeconds: int):
        if (self.hasTimedEvent):
            schedule.every(intervalSeconds).seconds.do(self.effect)