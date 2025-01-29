import pygame
import helperFunctions
import numpy as np
from definitions import mainFont

class Button():
    def __init__(self, x: int, y: int, width: int, height: int, backgroundImage: str, text="", unlocked=True):
        self.amount = 1
        self.x = x
        self.y = y
        self.text = text
        self.resetText(text)
        self.unlocked = unlocked

        # Load the background image and handle exceptions
        try:
            self.backgroundImage = pygame.image.load(backgroundImage).convert_alpha()
        except pygame.error as e:
            print(f"Failed to load image: {backgroundImage}")
            raise e

        # Get original dimensions
        imgWidth, imgHeight = self.backgroundImage.get_size()

        # Calculate the scaling factor
        scaleFactor = min(width / imgWidth, height / imgHeight)

        # Scale the image while maintaining aspect ratio
        self.width = int(imgWidth * scaleFactor)
        self.height = int(imgHeight * scaleFactor)
        self.originalBackgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))
        
        imageArray = pygame.surfarray.array3d(self.originalBackgroundImage)
        meanRGBValues = np.mean(imageArray, axis = 2)
        meanArray = meanRGBValues[..., np.newaxis]
        meanArray = np.repeat(meanArray[:, :, :], 3, axis=2)
        self.backgroundImage = pygame.surfarray.make_surface(meanArray)

        # Define button rectangle for click detection
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

    def renderButton(self, screen):
        # Blit the scaled image to the screen
        if self.unlocked:
            screen.blit(self.originalBackgroundImage, (self.x, self.y))
        else:
            screen.blit(self.backgroundImage, (self.x, self.y))
        if self.text != "":
            screen.blit(self.text, (self.x + self.width, self.y + self.height // 2))

    def onClicked(self, event, mousePosition: tuple[int, int]):
            # Check if the mouse position is within the button rectangle
            if event.type == pygame.MOUSEBUTTONDOWN and self.buttonRect.collidepoint(mousePosition):
                return True
            return False
    
    def resetText(self, text: str):
        if self.text == "":
            self.text = mainFont.render(str(text), True, (255, 255, 255))
        else:
            self.text = mainFont.render(helperFunctions.simplifyNumber(text), True, (255, 255, 255))