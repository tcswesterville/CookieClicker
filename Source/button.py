import pygame

class Button():
    def __init__(self, x: int, y: int, width: int, height: int, backgroundImage: str):
        self.x = x
        self.y = y

        # Load the background image
        self.backgroundImage = pygame.image.load(backgroundImage).convert_alpha()
        
        # Get original dimensions
        imgWidth, imgHeight = self.backgroundImage.get_size()

        # Calculate the scaling factor
        scaleFactor = min(width // imgWidth, height // imgHeight)

        # Scale the image while maintaining aspect ratio
        self.width = int(imgWidth * scaleFactor)
        self.height = int(imgHeight * scaleFactor)
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonImage = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Blit the scaled image
        self.buttonImage.blit(self.backgroundImage, (0, 0))

    def renderButton(self, screen):
        # Blit the image to the screen
        screen.blit(self.buttonImage, (self.x, self.y))

    def onClicked(self, event, mousePosition):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN and self.buttonRect.collidepoint(mousePosition):
                return True
        return False
