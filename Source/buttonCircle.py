import pygame

class ButtonCircle():
    def __init__(self, x: int, y: int, radius: int, backgroundImage: str):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = 0  # Initialize an angle for rotation

        # Load the background image
        self.backgroundImage = pygame.image.load(backgroundImage).convert_alpha()
        
        # Get original dimensions
        imgWidth, imgHeight = self.backgroundImage.get_size()

        # Calculate the scaling factor to fit within the circle
        scaleFactor = (2 * self.radius) / imgWidth if imgWidth > imgHeight else (2 * self.radius) / imgHeight

        # Scale the image while maintaining aspect ratio
        newWidth = int(imgWidth * scaleFactor)
        newHeight = int(imgHeight * scaleFactor)
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (newWidth, newHeight))
        
        # Create a circular mask for the button
        self.mask = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.mask, (255, 255, 255, 255), (self.radius, self.radius), self.radius)
        
        # Create a circular button image
        self.buttonImage = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        
        # Blit the scaled image centered on the circular button surface
        self.buttonImage.blit(self.backgroundImage, ((self.radius - newWidth // 2), (self.radius - newHeight // 2)))
        self.buttonImage.blit(self.mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    def renderButton(self, screen):
        # Rotate the button image
        rotatedImage = pygame.transform.rotate(self.buttonImage, self.angle)
        
        # Update the angle for the next frame
        self.angle = (self.angle + 1) % 360  # Rotate continuously
        
        # Calculate new position to keep the rotated image centered
        rotatedRect = rotatedImage.get_rect(center=(self.x, self.y))
        
        # Blit the rotated image to the screen
        screen.blit(rotatedImage, rotatedRect.topleft)

    def onClicked(self, event, mousePosition):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((mousePosition[0] - self.x) ** 2 + (mousePosition[1] - self.y) ** 2) ** 0.5 <= self.radius:
                return True
        return False
