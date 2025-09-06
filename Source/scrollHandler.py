import button
import pygame
# screenWidth ignored because shop buttons take up entire shop width and are static
class ScrollHandler():
    def draw(self, surface):
        for x in self.buttons:
            scroll_rect = x.rect.move(0, self.scroll_Offset)
            x.draw(surface, scroll_rect)
    def click(self, mouse_pos):
        adj=(mouse_pos[0], mouse_pos[1] - self.scroll_Offset)
        for x in self.buttons:
            if x.rect.collidepoint(adj):
                x.click()
                return True
    def scroll(self, direction):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if not (self.min_x <= mouse_x <= self.max_x):
            return
        self.scroll_Offset += direction*self.scroll_Speed
        Max=0
        Min=-len(self.buttons)*self.scroll_Speed
        self.scroll_Offset = max(min(self.scroll_Offset, Max), Min)
    def __init__(
                    self,
                    buttons: list[button.Button], 
                    xStart: int,
                    yStart: int,
                    xOffset: int,
                    yOffset: int,
                    screenHeight: int,
                    min_x = 0,
                    max_x = 0
                 ):
        self.min_x = min_x
        self.max_x = max_x
        self.scroll_Speed = 20
        self.scroll_Offset = 0
        self.buttons = buttons
        self.xStart = xStart
        self.yStart = yStart
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.screenHeight = screenHeight
        self.maximumButtons = self.calculateMaximumButtons()
        self.buttonPositions = self.calculateButtonPositions() # list of tuples (x, y) for each button
#remove later
    def calculateMaximumButtons(self):
        return int(self.screenHeight // self.yOffset)*2
    
    def calculateButtonPositions(self):
        buttonPositions = []

        for i in range(self.maximumButtons - 1):
            buttonPositions.append((self.xStart, self.yStart + (i * self.yOffset)))
        return buttonPositions
    
    def scrollUp(self):
        if (len(self.buttons) > self.maximumButtons):
            self.buttons = self.buttons[1:] + self.buttons[:1]

    def scrollDown(self):
        if (len(self.buttons) > self.maximumButtons):
            self.buttons = self.buttons[-1:] + self.buttons[:-1]

    def renderButtons(self, screen):
        for i in range(self.maximumButtons - 1):
            if (i < len(self.buttons)):
                self.buttons[i].x = self.buttonPositions[i][0]
                self.buttons[i].y = self.buttonPositions[i][1]
                self.buttons[i].renderButton(screen, self.scroll_Offset)