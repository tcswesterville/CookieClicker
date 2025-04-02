from button import *
from definitions import *
import userVariables

'''
benefitingPowerUp - the powerup that this upgrade line benefits
metaData - array of tuples for calculations
'''
class UpgradeLine():
    def __init__ (self, buttony: int, path: str, metaData, amountOfBenefittingPowerUp: int = 0):
        self.button = Button(0, buttony, shopWidth, UPGRADEBUTTONHEGIHT, path + metaData[0][0], "", amountOfBenefittingPowerUp >= metaData[0][7])
        self.path = path
        self.amountOfBenefittingPowerUp = amountOfBenefittingPowerUp
        self.metaData = metaData
        self.tier = 0
        self.adder = 0
        self.multiplier = 1

    def IncrementAmountOfBenefittingPowerUp(self):
        self.amountOfBenefittingPowerUp += 1
        self.calculateUnlocked()

    def calculateUnlocked(self):
        if (self.amountOfBenefittingPowerUp >= self.metaData[self.tier][7]):
            self.button.unlocked = True

    def update(self, screen):
        self.calculateUnlocked()
        if (self.button.unlocked):
            self.button.renderButton(screen)

    def purchase(self, event, mousePosition):
        if (self.button.onClicked(event, mousePosition)):
            if self.button.unlocked and userVariables.cookies >= self.metaData[self.tier][1]:
                userVariables.cookies -= self.metaData[self.tier][1]
                self.upgrade()

    def upgrade(self):
        print("Upgrading")
        self.calculatePower()
        self.tier += 1
        self.button.unlocked = False
        self.calculateUnlocked()
        self.button.changeBackground(self.path + self.metaData[self.tier][0])

    def calculatePower(self):
        print(f"Original Adder: {self.adder}, Original Multiplier: {self.multiplier}")
        self.adder += self.metaData[self.tier][2]
        self.multiplier = self.multiplier *  self.metaData[self.tier][3]
        print(f"Adder: {self.adder}, Multiplier: {self.multiplier}")

    def applyUpgrade(self, amount):
        if (self.tier == -1):
            return amount
        amountFromMultiplier = self.multiplier * amount
        return (amountFromMultiplier + self.adder)