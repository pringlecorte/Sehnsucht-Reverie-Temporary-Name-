import pygame
obstacle = []

class Obstacles():
    def __init__(self, x, z, widtha, heighta, height, Screen):
        self.x = x
        self.y = height/2
        self.z = z
        if self.z > 5:
            self.z = 5
        self.width = widtha
        self.height = heighta

        self.ScreenDisplay = Screen
        #for future me, if u want moving objects just put this part down into render
        self.heighta = self.height * self.z
        self.widtha = self.width * self.z

        obstacle.append(self)



    def render(self):
        pygame.draw.rect(self.ScreenDisplay, (200*(self.z/5),200*(self.z/5), 200*(self.z/5)), (self.x, self.y, self.widtha, self.heighta))