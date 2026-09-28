import pygame

class Food:
    def __init__(self, x, y, z, Screen):
        self.x = x
        self.y = y
        self.z = z

        self.width = 3 * self.z
        self.height = 3 * self.z

        self.R, self.G, self.B = 188, 133, 67
        self.ScreenDisplay = Screen

    def render(self):
        pygame.draw.rect(self.ScreenDisplay, (self.R, self.G, self.B), (self.x, self.y, self.width, self.height))
        