import pygame
import math
import sys
import keyboard as keys
import pyautogui as gangalicious


from resize import shrink, grow, grow_thresholds, shrink_thresholds

class Player:
    def __init__(self, width, height, stage, Screen, up, down, left, right, jump, run, crouch, drop):
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
        self.stage = stage

        self.velocity = 0

        self.keyup = up
        self.keydown = down
        self.keyright = right
        self.keyleft = left
        self.keyjump = jump
        self.keyrun = run
        self.keycrouch = crouch
        self.keyattack = drop

        self.futurex, self.futurey, self.futurez = self.x, self.y, self.z

        self.isfood = False
        self.foodwhereabouts = {}

        self.finalrenderx = 0

        self.originalz = 1
        self.original_dist_cent = 0

        self.min_thresh = self.screen_width/2 - self.stage/2
        self.max_thresh = self.screen_width/2 + self.stage/2



    def controls(self):
        self.Right = False

        self.widtha = self.widthb*self.z
        self.heighta = self.heightb*self.z 



        if keys.is_pressed(self.keyup) and self.widtha > self.widthb:
            self.futurey, self.futurez = shrink(self.y, self.z, self.screen_width, self.originalz, self.original_dist_cent)
            self.y, self.z = self.futurey, self.futurez
            self.basey -= 1
            self.min_thresh, self.max_thresh = shrink_thresholds(self.min_thresh, self.max_thresh, self.z)
            
            
            #threshold
            #self.min_thresh, self.max_thresh = grow(self.min_thresh, self.y, self.z, self.screen_width, self.originalz, self.original_dist_cent)[0], grow(self.max_thresh, self.y, self.z, self.screen_width, self.originalz, self.original_dist_cent)[0]


        elif keys.is_pressed(self.keydown) and self.z < 5:
            self.futurey, self.futurez = grow(self.y, self.z, self.screen_width, self.originalz, self.original_dist_cent)
            self.y, self.z = self.futurey, self.futurez
            self.basey += 1

            #thresold
            #self.min_thresh, self.max_thresh = shrink(self.min_thresh, self.y, self.z, self.screen_width, self.originalz, self.original_dist_cent)[0], shrink(self.max_thresh, self.y, self.z, self.screen_width, self.originalz, self.original_dist_cent)[0]
            self.min_thresh, self.max_thresh = grow_thresholds(self.min_thresh, self.max_thresh, self.z)
            #print(self.original_dist_cent)
        #print(self.z)
        self.min_thresh = max(0, self.min_thresh)
        self.max_thresh = min(self.screen_width, self.max_thresh)

        if keys.is_pressed(self.keyleft):
            self.Right = False
            if int(self.velocity) > 0:
                self.velocity -= self.velocity/5

            elif self.velocity >= -self.speed:
                self.velocity -= 0.025

            if keys.is_pressed(self.keyrun) and self.velocity >= -self.speed - 0.1:
                self.velocity -= 0.1

                self.x += self.velocity * self.z
                self.futurex = self.x
            else:
                if self.velocity < -self.speed:
                    self.velocity += 0.1

        elif keys.is_pressed(self.keyright):
            self.Right = True

            if int(self.velocity) < 0:
                self.velocity += abs(self.velocity/4)

            elif self.velocity <= self.speed:
                self.velocity += 0.025
            if keys.is_pressed(self.keyrun) and self.velocity <= self.speed + 0.1:
                self.velocity += 0.1

                self.x += self.velocity * self.z
                self.futurex = self.x
            else:
                if self.velocity > self.speed:
                    self.velocity -= 0.1
            

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

        if keys.is_pressed(self.keyattack):
            self.isfood = True


    def attack(self):
        if self.attack:
            pass
    
    def math(self, Itsuki):
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

        if self.x < self.min_thresh:
            self.futurex = self.max_thresh

        if self.x > self.max_thresh:
            self.futurex = self.min_thresh

        self.x = self.futurex
    

        if self.crouch:
            self.heightb = self.screen_height/72
        if not keys.is_pressed(self.keycrouch) and not self.jump:
            #self.y -= (height/36 - height/72)*self.z
            self.heightb = self.screen_height/36
           
            self.crouch = False
        #print(self.crouch)
    
        if Itsuki.x - Itsuki.thresholdsx <= int(self.x) <= Itsuki.x + Itsuki.thresholdsx and Itsuki.z - Itsuki.thresholdsz <= self.z <= Itsuki.z + Itsuki.thresholdsz and Itsuki.y - 1 <= self.y <= Itsuki.y + 1:
            self.velocity *= -(10*abs(Itsuki.velocity) + 3)

    def render(self):
        #print(self.y)
        self.finalrenderx = self.x - self.widtha/2
        self.finalrendery = self.y - self.heighta/2

        self.R = 0
        self.G = 30 * self.z
        self.B = 30 * self.z

        if self.G > 200:
            self.G = 200
        if self.B > 200:
            self.B = 200


        pygame.draw.rect(self.ScreenDisplay, (self.R, self.G, self.B), (self.finalrenderx, self.finalrendery, self.widtha, self.heighta))
        pygame.draw.circle(self.ScreenDisplay, (255,255,255), (self.x, self.y), 2)

        pygame.draw.circle(self.ScreenDisplay, (255, 255, 255), (self.min_thresh, self.y), 2)
        pygame.draw.circle(self.ScreenDisplay, (255, 255, 255), (self.max_thresh, self.y), 2)
        #print(self.max_thresh)

print("saved. but you shouldnt run the code from here you idiot")

