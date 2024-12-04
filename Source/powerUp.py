from button import *
from userVariables import cookies

class PowerUP(Button):
    def __init__(self, initialCost):
        self.amount = 0
        self.cost = initialCost
    def calculatePrice(self):
        self.cost *= 1.10
    def setPrice(self):
        self.cost = self.calculatePrice()
        self.resetText(self.cost)
    def purchase(self):
        if cookies >= self.cost:
            cookies -= self.cost
            self.amount += 1
            self.setPrice()