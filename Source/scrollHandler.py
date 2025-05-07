import button

# screenWidth ignored because shop buttons take up entire shop width and are static
class ScrollHandler():
    def __init__(
                    self,
                    buttons: list[button.Button], 
                    xStart: int,
                    yStart: int,
                    xOffset: int,
                    yOffset: int,
                    screenHeight: int,
                 ):
        self.buttons = buttons
        self.xStart = xStart
        self.yStart = yStart
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.screenHeight = screenHeight
        self.maximumButtons = self.calculateMaximumButtons()
        self.buttonPositions = self.calculateButtonPositions() # list of tuples (x, y) for each button

    def calculateMaximumButtons(self):
        return int(self.screenHeight // self.yOffset)
    
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
                self.buttons[i].renderButton(screen)