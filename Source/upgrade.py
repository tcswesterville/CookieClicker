from button import *
from definitions import *
import userVariables

'''
benefitingPowerUp - the powerup that this upgrade line benefits
metaData - array of tuples for calculations
ignoredPowerUpsList - list of indecies of powers from the power up list to be ignored in per unit calculations
'''
class UpgradeLine():
    def __init__ (self, buttony: int, path: str, metaData, amountOfBenefittingPowerUp: int = 0, ignoredPowerUps: list = []):
        self.button = Button(0, buttony, shopWidth, UPGRADEBUTTONHEGIHT, path + metaData[0][0], "", amountOfBenefittingPowerUp >= metaData[0][7])
        self.path = path
        self.amountOfBenefittingPowerUp = amountOfBenefittingPowerUp
        self.metaData = metaData
        self.ignoredPowerUps = ignoredPowerUps
        self.tier = 0
        self.adder = 0
        self.multiplier = 1
        # Adders and multipliers that are not applied due to upgrade purchase
        self.perUnitAdder = 0
        self.perUnitAdderMultiplier = 1
        self.perUnitAdderEffect = 0

    def IncrementAmountOfBenefittingPowerUp(self):
        self.amountOfBenefittingPowerUp += 1
        self.calculateUnlocked()

    def calculateUnlocked(self):
        if (self.amountOfBenefittingPowerUp >= self.metaData[self.tier][7]):
            self.button.unlocked = True

    def update(self, screen, powerUpList: list):
        amount = 0
        for i in range(len(powerUpList)):
            if (i not in self.ignoredPowerUps):
                amount += powerUpList[i].getAmount()
        
        self.calculateUnlocked()
        if (self.button.unlocked):
            self.button.renderButton(screen)
        perUnitAdderEffect = self.perUnitAdderEffect
        self.calculatePerUnitPower(amount)
        if(perUnitAdderEffect != self.perUnitAdderEffect):
            print(f"Per Unit Adder Effect Changed: {perUnitAdderEffect} -> {self.perUnitAdderEffect}")

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
        if (self.tier == 0):
            return
        print(f"Original Adder: {self.adder}, Original Multiplier: {self.multiplier}")
        self.adder += self.metaData[self.tier][2]
        self.multiplier *= self.metaData[self.tier][3]
        print(f"Original Per Unit Adder: {self.perUnitAdder}, Original Per Unit Adder Multiplier: {self.perUnitAdderMultiplier}")
        self.perUnitAdder += self.metaData[self.tier][4]
        self.perUnitAdderMultiplier *= self.metaData[self.tier][5]
        print(f"New Adder: {self.adder}, New Multiplier: {self.multiplier}")
        print(f"New Per Unit Adder: {self.perUnitAdder}, New Per Unit Adder Multiplier: {self.perUnitAdderMultiplier}")

    # Calculate power not caused by a purchase of an upgrade
    def calculatePerUnitPower(self, amountOfUnits: int):
        if (self.tier == 0):
            return
        self.perUnitAdderEffect = self.perUnitAdder * amountOfUnits * self.perUnitAdderMultiplier

    def applyUpgrade(self, amount):
        if (self.tier == 0):
            return amount
        amountFromMultiplier = self.multiplier * amount
        return (amountFromMultiplier + self.adder + self.perUnitAdderEffect * self.perUnitAdderMultiplier)