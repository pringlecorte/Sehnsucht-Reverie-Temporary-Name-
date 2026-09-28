import pygame
import math
import sys
import keyboard as keys
import pyautogui as gangalicious


from resize import shrink, grow

class Player:
    def __init__(self, width, height, Screen, up, down, left, right, jump, run, crouch):
        #screen width, height, Screen
        self.x = width/3
        self.y = height/2
        self.z = 1

        self.widthb = width/192
        self.heightb = height/36

        self.widtha = self.widthb*self.z
        self.heighta = self.heightb*self.z 

        self.jump = False
        self.speed = 0.90
        self.velocity = 0
        self.maxjumph = 5

        self.basey = self.y

        self.crouch = False
        self.crouchval = 0

        self.screen_width = width
        self.screen_height = height
        self.ScreenDisplay = Screen

        self.velocity = 0

        self.keyup = up
        self.keydown = down
        self.keyright = right
        self.keyleft = left
        self.keyjump = jump
        self.keyrun = run
        self.keycrouch = crouch

        self.futurex, self.futurey, self.futurez = self.x, self.y, self.z
        
    def controls(self):
        self.Right = False

        self.widtha = self.widthb*self.z
        self.heighta = self.heightb*self.z 


        if keys.is_pressed(self.keyup) and self.widtha > self.widthb:
            self.futurex, self.futurey, self.futurez = shrink(self.x, self.y, self.z)
            self.x, self.y, self.z = self.futurex, self.futurey, self.futurez
            self.basey -= 1.5 * (self.z/5)


        if keys.is_pressed(self.keydown) and self.z < 5:
            self.futurex, self.futurey, self.futurez = grow(self.x, self.y, self.z)
            self.x, self.y, self.z = self.futurex, self.futurey, self.futurez
            self.basey += 1.5* (self.z/5)

        #print(self.z)

        if keys.is_pressed(self.keyleft):
            self.Right = False
            if int(self.velocity) > 0:
                self.velocity -= self.velocity/4

            elif self.velocity >= -self.speed:
                self.velocity -= 0.025

                if keys.is_pressed(self.keyrun):
                    self.velocity -= 0.05

                    self.x += self.velocity * self.z
                    self.futurex = self.x
        elif keys.is_pressed(self.keyright):
            self.Right = True

            if int(self.velocity) < 0:
                self.velocity += abs(self.velocity/4)

            elif self.velocity <= self.speed:
                self.velocity += 0.025
                if keys.is_pressed(self.keyrun):
                    self.velocity += 0.05

                    self.x += self.velocity * self.z
                    self.futurex = self.x
            

        else:
            if self.velocity > 0:
                self.velocity -= 0.075
            elif self.velocity < 0:
                self.velocity += 0.075

        self.futurex += self.velocity * self.z


        self.x = self.futurex

       


        if keys.is_pressed(self.keycrouch):
            self.basey1 = self.y
            self.crouch = True
        
        if keys.is_pressed(self.keyjump) and not self.jump:

            self.basey = self.y
            self.basez = self.z
            self.jump = True
            #self.time = -50
            #self.time1= -75
            self.y_vel = self.maxjumph 
            self.y -= 0.00000001
            

    def attack(self):
        if self.attack:
            pass
    
    def math(self):
        if self.jump:            
            if self.y < self.basey:
                self.futurey -= self.y_vel * self.z
                self.y = self.futurey
                self.y_vel -= 0.5
                #print('hello')
            else:
                self.jump = False
                #self.heighta -= 20*self.z
                self.futurey = self.basey
                self.y = self.futurey

            
            #print(f"basey:{self.basey}")
            #print(f"y:{self.y}")
            #print(f"vely{self.y_vel}")
        #print(f"z:{self.z}")

        if self.x < 0:
            self.futurex = self.screen_width

        elif self.x > self.screen_width:
            self.futurex = 0

        self.x = self.futurex
    

        if self.crouch:
            self.heightb = self.screen_height/72
        if not keys.is_pressed(self.keycrouch) and not self.jump:
            #self.y -= (height/36 - height/72)*self.z
            self.heightb = self.screen_height/36
           
            self.crouch = False
        #print(self.crouch)
    


    def render(self):
        self.R = 0
        self.G = 30 * self.z
        self.B = 30 * self.z

        if self.G > 200:
            self.G = 200
        if self.B > 200:
            self.B = 200


        pygame.draw.rect(self.ScreenDisplay, (self.R, self.G, self.B), (self.x, self.y - self.heighta, self.widtha, self.heighta))




