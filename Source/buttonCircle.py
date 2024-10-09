import pygame

class ButtonCircle():

    def __init__(self, x: int, y: int, radius: int, backgroundImage: str):
        self.x = x
        self.y = y
        self.radius = radius
        self.center = (self.x, self.y)
        self.backgroundImage = pygame.image.load(backgroundImage).convert_alpha()
        #self.backgroundImage = pygame.transform.scale(self.backgroundImage, (2 * self.radius, 2 * self.radius))
        self.mask = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.mask, (255, 255, 255, 255), self.center, self.radius)
        self.backgroundImage.blit(self.mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    def renderButton(self, screen):
        screen.blit(self.backgroundImage, (self.x - self.radius, self.y - self.radius))
    
    def onClicked(self, event, mousePosition):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((mousePosition[0] - self.x) ** 2 + (mousePosition[1] - self.y) ** 2) ** 0.5 <= self.radius:
                return True
        return False