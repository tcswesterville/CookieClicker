from button import *
from definitions import *
import userVariables

'''
benefitingPowerUp - the powerup that this upgrade line benefits
metaData - array of tuples for calculations
'''
class UpgradeLine():
    def __init__ (self, buttony: int, path: str, benefitingPowerUp, metaData):
        self.button = Button(0, buttony, shopWidth, UPGRADEBUTTONHEGIHT, path + metaData[0][0], "", benefitingPowerUp.getAmount() >= metaData[0][7])
        self.path = path
        self.benefitingPowerUp = benefitingPowerUp
        self.metaData = metaData
        self.tier = 0
        self.adder = 0
        self.multiplier = 1

    def calculateUnlocked(self):
        if (self.benefitingPowerUp.getAmount() >= self.metaData[self.tier][7]):
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
        self.tier += 1
        self.button.unlocked = False
        self.calculateUnlocked()
        self.button.changeBackground(self.path + self.metaData[self.tier][0])

    def calculatePower(self):
        self.adder += self.metaData[self.tier][2]
        self.multiplier *= self.metaData[self.tier][3]

    def applyUpgrade(self):
        if (self.tier > 0):
            amount = self.benefitingPowerUp.getAmount()
            multiplier = self.multiplier + amount * self.metaData[self.tier - 1][5]
            adder = self.adder + amount * self.metaData[self.tier - 1][4]
            return (amount * multiplier * self.benefitingPowerUp.power + adder)
        else:
            return (self.benefitingPowerUp.getAmount() * self.benefitingPowerUp.power)