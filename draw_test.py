import keyboard as keys
import pygame
from resize import shrink, grow
class pen:
    def __init__(self, width, height, screen):
        self.x = width/2
        self.z = 1
        self.y = height/2

        self.ScreenDisplay = screen

        self.up = keys.is_pressed("up")
        self.down = keys.is_pressed("down")
        self.right = keys.is_pressed("right")
        self.left = keys.is_pressed("left")

        self.widthb = 100
        self.heightb = 100

    def move(self):

        self.up = keys.is_pressed("up")
        self.down = keys.is_pressed("down")
        self.right = keys.is_pressed("right")
        self.left = keys.is_pressed("left")

        if self.up:
            self.x, self.y, self.z = shrink(self.x, self.y, self.z)
        if self.down:
            self.x, self.y, self.z = grow(self.x, self.y, self.z)
        if self.right:
            self.x += 1
        if self.left:
            self.x -= 1

        print(f"x {self.x}")
        print(f"z {self.z}")

class Draw:
    def __init__(self, x, y, z, Screen):
        self.R = 100
        self.G = 100
        self.B = 100

        self.x = x
        self.y = y
        self.z = z

        self.width = 10*self.z
        self.height = 10 * self.z

        self.ScreenDisplay = Screen
    def render(self):
        self.newR = min(self.R * (self.z/5), 255)
        self.newG = min(self.G * (self.z/5), 255)
        self.newB = min(self.B * (self.z/5), 255)

            #print("hellO)")
            #print(f"x {self.x}")
            #print(f"y {self.y}")
            #print(f"z {self.z}")
            #print(f"height {self.heighta}")
            #print(f"width {self.widtha}")
            #print(f"R {self.R}")
            #print(f"G {self.G}")
            #print(f"B {self.B}")
        pygame.draw.rect(self.ScreenDisplay, (self.newR, self.newG, self.newB), (self.x, self.y, self.width, self.height))
