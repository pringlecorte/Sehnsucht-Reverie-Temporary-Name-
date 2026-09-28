import pygame
import random
from resize import grow, shrink

class QuintessentialQuintuplets():
        def __init__(self, x, y, z, responsiveness, thresholdsx, thresholdsz, speed, R, G, B, Screen, width, height, traits=None):
            self.traits = traits if traits is not None else {}

            self.shy = self.traits.get("shy", False)
            self.athletic = self.traits.get("athletic", False)
            self.tsundere = self.traits.get("tsundere", False)
            self.hungry = self.traits.get("hungry", False)
            self.clingy = self.traits.get("clingy", False)
            self.smart = self.traits.get("smart", False)
            self.distracted = self.traits.get("distracted", False)
            self.fatso = self.traits.get("fatso", False)
            self.dangerous = self.traits.get("dangerous", False)
    

            #THE QUINTESSENTIAL QUINTUPLETS
            self.x = x
            self.y = y
            self.z = z

            self.widthb = width/192
            self.heightb = height/36

            self.responsiveness = responsiveness
            self.thresholdsx = thresholdsx
            self.thresholdsz = thresholdsz
            self.speed = speed

            self.dz = self.z
            self.dx = self.x

            self.widtha = self.widthb*self.z
            self.heighta = self.heightb*self.z 

            self.R = R
            self.G = G
            self.B = B

            self.velocity = 0
            self.juke = False

            self.futurex = self.x
            self.futurey = self.y
            self.futurez = self.z

            self.active = False
            self.Loopingtherooms = 1

            self.screen_width = width
            self.ScreenDisplay = Screen
            self.screen_height = height

            self.jump = False
            self.maxjumph = 8

            self.basex = self.x
            self.basey = self.y
            self.basez = self.z

            self.meatbun = None
            self.doneating = False
        def simplicityatitsfinest(self, obstacle):
                    for obs in obstacle:
                                if (obs.z - 0.1 <= self.futurez <= obs.z + 0.1) and (obs.x <= self.futurex <= obs.x + obs.widtha):
                                        self.x1 = abs(self.x - obs.x)
                                        self.x2 = abs(self.x - (obs.x + obs.widtha))

                                        if self.x1 < self.x2:
                                            self.dx = obs.x - 10
                                        else:   
                                            self.dx = obs.x + obs.widtha + 10

                                        self.futurex, self.futurey, self.futurez = self.x, self.y, self.z
                        
                    self.x, self.y, self.z = self.futurex, self.futurey, self.futurez
            


        def aitracking(self, player, obstacle, itsukisweakness=None):
            if self.Loopingtherooms % self.responsiveness == 0:
                    self.dx = random.uniform(player.futurex - self.z*self.thresholdsx, player.futurex + self.z*self.thresholdsx)
                    self.dz = random.uniform(player.futurez - self.z*self.thresholdsz, player.futurez + self.z*self.thresholdsz) 

            self.personality_intercept(player, itsukisweakness)
            #print(self.dx)
            if not (self.dz - 0.1  <= self.z <= self.dz + 0.1):
                if (self.z - self.dz < 0):
                    self.futurex, self.futurey, self.futurez = grow(self.x, self.y, self.z)
                    self.basey += 1.5* (self.z/5)
                    self.simplicityatitsfinest(obstacle)
                            

                elif (self.z - self.dz >= 0):
                    self.futurex, self.futurey, self.futurez = shrink(self.x, self.y, self.z)
                    self.basey -= 1.5 * (self.z/5)
                    self.simplicityatitsfinest(obstacle)


            if not(self.dx - 1 <= self.x <= self.dx + 1):
                if (self.x - self.dx < 0):
                     self.Right = 1

                     if self.velocity <= self.speed:
                        self.velocity += 0.05

        
                         
                elif (self.x - self.dx > 0):
                    self.Right = -1

                    if self.velocity >= -self.speed:
                        self.velocity -= 0.05

            #personality check

            

            self.x += self.velocity  * self.z

            if self.x < 0:
                self.x = self.screen_width

            elif self.x > self.screen_width:
                self.x = 0
    
        def personality_intercept(self, player, eatsuki):
            self.meatbun = eatsuki if eatsuki is not None else 0
            
            if self.shy:
                if abs(self.x - self.dx) < 20 * self.z:
                    self.velocity *= 1/1.2

            if self.fatso:
                self.velocity *= 1/1.1

            if self.tsundere:
                if self.Loopingtherooms % self.responsiveness == 0:
                    self.dx *= 2

                    if self.dx > self.screen_width:
                        self.dx = self.dx % self.screen_width


            if self.athletic and not self.jump:
                if self.Loopingtherooms % (self.responsiveness * random.randint(10,15)) == 0:                  
                    self.basey = self.y
                    self.basez = self.z
                    self.basex = self.x
                    self.jump = True
                    self.y_vel = self.maxjumph 
                    self.y -= 0.00000001
                    self.jump = True

                    
            if self.jump:  
                self.dx = player.futurex
                self.dz = player.futurez          
                if self.y < self.basey:
                    self.y -= self.y_vel * self.z
                    self.y_vel -= self.maxjumph/20

                  
                    self.x += ((player.futurex - self.x) * self.z)/(self.maxjumph*2/(self.maxjumph/20))
                    
                    if self.z < player.futurez:
                        self.x, self.y, self.z = grow(self.x, self.y, self.z)
                        self.basey += 1.5* (self.z/5)
                        

                    elif self.z > player.futurez:
                        self.x, self.y, self.z = shrink(self.x, self.y, self.z)
                        self.basey -= 1.5* (self.z/5)
                #print('hello')

                else:
                    self.jump = False
                    self.y = self.basey

            if self.clingy:
                self.dx = player.futurex
                self.dz = player.futurez

                if abs(self.x - player.futurex) < 5 * self.z:
                    self.velocity *= 1/1.2
            

            if self.hungry:
                if eatsuki:
                    self.dx = self.meatbun.x
                    self.dz = self.meatbun.z

                if self.dx - 5 <= self.x <= self.dx + 5 and self.dz - 0.5 <= self.z <= self.dz + 0.5: 
                    if self.Loopingtherooms % 500 != 0 and not self.doneating:
                        if eatsuki:
                            self.dx = self.meatbun.x
                            self.dz = self.meatbun.z
                        self.doneating = False
                        print("eating")
                    elif self.Loopingtherooms % 500 == 0:
                        self.doneating = True
                        print("done")
                    
                 
            
        def render(self):
            self.newR = self.R * (self.z/5)
            self.newG = self.G * (self.z/5)
            self.newB = self.B * (self.z/5)

            if self.newR > 255:
                self.newR = 255
            if self.newG > 255:
                self.newG = 255
            if self.newB > 255:
                self.newB = 255

            self.widtha = self.widthb*self.z
            self.heighta = self.heightb*self.z
            #print("hellO)")
            #print(f"x {self.x}")
            #print(f"y {self.y}")
            #print(f"z {self.z}")
            #print(f"height {self.heighta}")
            #print(f"width {self.widtha}")
            #print(f"R {self.R}")
            #print(f"G {self.G}")
            #print(f"B {self.B}")
            pygame.draw.rect(self.ScreenDisplay, (self.newR, self.newG, self.newB), (self.x, self.y - self.heighta, self.widtha, self.heighta))

            self.Loopingtherooms += 1
