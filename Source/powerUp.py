from button import *
import userVariables
import schedule

class PowerUP():
    def __init__(self, button: Button, initialCost: int, timedEvent: bool, powerIncrement = 1, power = 0, intervalSeconds = 1):
        self.button = button
        self.cost = initialCost
        self.hasTimedEvent = timedEvent
        self.powerIncrement = powerIncrement
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
                print(userVariables.cookies)
                userVariables.cookies -= self.cost
                self.power += self.powerIncrement
                self.setPrice()
    def effect(self):
        userVariables.cookies += self.power
        userVariables.score += self.power
    def scheduledJob(self):
        print("Running Job")
    def initiateTimedEvent(self, intervalSeconds: int):
        if (self.hasTimedEvent):
            schedule.every(intervalSeconds).seconds.do(self.effect)
            #schedule.every(intervalSeconds).seconds.do(self.scheduledJob)