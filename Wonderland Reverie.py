import pygame
import math
import sys
import keyboard as keys
import pyautogui as gangalicious
import os 
import random 

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


width = 800
height = 600
RefreshRate = 60

Loopingtherooms = 0

class resize:
    def __init__(self):
        self.width = width
        self.height = height
        self.takedif = 1

    def fourthree(self):
        self.dwidth = 1440
        self.dheight = 1080

    def sixteennine(self):
        self.dwidth = 1920
        self.dheight = 1080

    def oneone(self):
        self.dwidth = 720
        self.dheight = 720
        

    def alter(self, duration):
        global width, height
        self.duration = duration
        width += (((self.dwidth - int(width)))/(RefreshRate * duration))/0.1
        height += (((self.dheight - int(height)))/(RefreshRate * duration))/0.1
        #yes it actually goes to 1920 and 1440

    def update(self):
        Screen = pygame.display.set_mode((int(width), int(height)))

resize = resize()
Screen = pygame.display.set_mode((width, height))
gangalicious.PAUSE = False


def shrink(x, y, z):
    z -= 0.05 * (z/5)
    x += 0.25 * (z/5)
    y -= 1.5 * (z/5)
    

    return x, y, z

def grow(x, y, z):
    z += 0.05 * (z/5)
    x -= 0.25* (z/5)
    y += 1.5* (z/5)

    return x, y, z


class Player:
    def __init__(self):
        self.x = width/3
        self.y = height/2
        self.z = 1

        self.widthb = width/192
        self.heightb = height/36

        self.widtha = self.widthb*self.z
        self.heighta = self.heightb*self.z 

        self.jump = False
        self.speed = 3
        self.maxjumph = 5

        self.basey = self.y

        self.crouch = False
        self.crouchval = 0

        self.resize = resize

        self.allinone = [self.x, self.y, self.z]

    def controls(self):
        self.Right = False

        self.widtha = self.widthb*self.z
        self.heighta = self.heightb*self.z 

        key = pygame.key.get_pressed()

        if key[pygame.K_w] and self.widtha > self.widthb:
            self.x, self.y, self.z = shrink(self.x, self.y, self.z)

            self.basey -= 1.5 * (self.z/5)


        if key[pygame.K_s] and self.z < 5:
            self.x, self.y, self.z = grow(self.x, self.y, self.z)

            self.basey += 1.5* (self.z/5)

        #print(self.z)

        if key[pygame.K_a]:
            self.Right = False
            self.x -= 1 * self.z

            if keys.is_pressed("left shift"):
                self.x -= 0.5*self.z

        elif key[pygame.K_d]:
            self.Right = True
            self.x += 1 * self.z

            if keys.is_pressed("left shift"):
                self.x += 0.5*self.z

        if keys.is_pressed("q"):
            self.basey1 = self.y
            self.crouch = True
        

        if keys.is_pressed("space") and not self.jump:

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
                self.y -= self.y_vel * self.z
                self.y_vel -= 0.5
                #print('hello')
            else:
                self.jump = False
                #self.heighta -= 20*self.z
                self.y = self.basey

            
            #print(f"basey:{self.basey}")
            #print(f"y:{self.y}")
            #print(f"vely{self.y_vel}")
        #print(f"z:{self.z}")

        if self.x < 0:
            self.x = width

        elif self.x > width:
            self.x = 0
    

        if self.crouch:
            self.heightb = height/72
        if not keys.is_pressed("q") and not self.jump:
            #self.y -= (height/36 - height/72)*self.z
            self.heightb = height/36
           
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

        pygame.draw.rect(Screen, (self.R, self.G, self.B), (self.x, self.y - self.heighta, self.widtha, self.heighta))


player = Player()

obstacle = []

class Obstacles():
    def __init__(self, x, z, widtha, heighta):
        self.x = x
        self.y = height/2
        self.z = z
        if self.z > 5:
            self.z = 5
        self.width = widtha
        self.height = heighta

        #for future me, if u want moving objects just put this part down into render
        self.heighta = self.height * self.z
        self.widtha = self.width * self.z

        obstacle.append(self)



    def render(self):
        pygame.draw.rect(Screen, (200*(self.z/5),200*(self.z/5), 200*(self.z/5)), (self.x, self.y, self.widtha, self.heighta))

fan = Obstacles(100, 4, 20, 20)
wall = Obstacles(300, 2, 50, 50)


class QuintessentialQuintuplets():
        def __init__(self, x, y, z, responsiveness, thresholdsx, thresholdsz, speed, R, G, B):
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

        def simplicityatitsfinest(self):
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
            


        def aitracking(self):
            if Loopingtherooms % self.responsiveness == 0:
                    self.dx = random.uniform(player.x - self.thresholdsx, player.x + self.thresholdsx)
                    self.dz = random.uniform(player.z - self.thresholdsz, player.z + self.thresholdsz) 
            #
            #print(self.dx)
            if not (self.dz - 0.1  <= self.z <= self.dz + 0.1):
                if (self.z - self.dz < 0):
                    self.futurex, self.futurey, self.futurez = grow(self.x, self.y, self.z)

                    self.simplicityatitsfinest()
                            

                elif (self.z - self.dz >= 0):
                    self.futurex, self.futurey, self.futurez = shrink(self.x, self.y, self.z)

                    self.simplicityatitsfinest()


            if not(self.dx - 1 <= self.x <= self.dx + 1):
                    if (self.x - self.dx < 0):
                         self.Right = 1

                         if self.velocity <= self.speed:
                            self.velocity += 0.1

                         self.x += self.velocity *  self.z
                         
                    elif (self.x - self.dx > 0):
                        self.Right = -1

                        if self.velocity >= -self.speed:
                            self.velocity -= 0.1

                        self.x += self.velocity  * self.z

            if self.x < 0:
                    self.x = width
                    self.juke = True
            elif self.x >= width:
                    self.x = 0
                    self.juke = True
    
            
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
            pygame.draw.rect(Screen, (self.newR, self.newG, self.newB), (self.x, self.y - self.heighta, self.widtha, self.heighta))

Ichika = QuintessentialQuintuplets(0/width, height/2, 1, 16, 20, 0.1, 0.65, 200, 200, 0)
Nino = QuintessentialQuintuplets(width/4, height/2, 1, 20, 25, 0.2, 0.45, 247, 37, 133)
Miku = QuintessentialQuintuplets(width/2, height/2, 1, 10, 10, 0.05, 0.55, 72, 149, 239)
Yotsuba = QuintessentialQuintuplets(width*3/4, height/2, 1, 10, 1, 0.1, 0.70, 112, 224, 0)
Itsuki = QuintessentialQuintuplets(width, height/2, 1, 20, 10, 1, 0.35, 239, 35, 60)    

Sisters = [Ichika, Nino, Miku, Yotsuba, Itsuki]
Entities = [Ichika, Nino, Miku, Yotsuba, Itsuki, player, fan, wall]

class achievements:
    def __init__(self):
        self.progress={
            "Miku":False,
            "Nino":False,
            "Itsuki":False,
            "Ichika":False,
            "Yotsuba":False,
            "Jump":False,
            "Beginning":False,
            "Pacman":False,
            "Flash":False,
            "WrongKeyE":False,
            "Order":False
        }

    
    def unlock(self, name, messages):
        if not self.progress[name]:
            print(f"Achievement Unlocked!!: {messages}")
            self.progress[name] = True

    def checker(self):
        if player.x - 2 <= Miku.x <= player.x + 2 and player.z - 0.1 <= Miku.z <= player.z + 0.1:
            self.unlock("Miku", "Love At First Lesson?")

        if player.x - width/3 != 0:
            self.unlock("Beginning", "Welcome to Huss Valley")

        if player.x >= width or player.x <= 0:
            self.unlock("Pacman", "Wakka Wakka")

        if player.jump and Yotsuba.x - 3 <= player.x <= Yotsuba.x + 3:
            self.unlock("Yotsuba", "Random Dude Vs. Lebron Nakano")

        if player.crouch and Nino.x - 1 <= player.x <= Nino.x + 1:
            self.unlock("Nino", "With The Sole Exception Of Nakano Nino Of Course")
        if Ichika.juke:
            self.unlock("Ichika", "Onee-Chan Wanted To Give You A Hug :(")
        if player.jump:
            self.unlock("Jump", "Jump Up, Superstar!")
        if Itsuki.x - 10 <= player.x <= Itsuki.x + 10:
            self.unlock("Itsuki", "Star Struck With The Star Pins")

        if keys.is_pressed("left shift"):
            self.unlock("Flash", "Assetto Corsa")

        if keys.is_pressed("e"):
            self.unlock("WrongKeyE", "Hahaha, Buddy Thought I Was Motivated Enough To Code Something For The E Key")

        if Ichika.z > Nino.z > Miku.z > Yotsuba.z > Itsuki.z:
            self.unlock("Order", "'Ichi, Ni, Mi, Yotsu, Itsu...' 'PICK A SYSTEM BRO'")
                
 
        
achieve = achievements()

refresh = pygame.time.Clock()
test = True
n = 0
s = 0
n = pygame.time.get_ticks()
while True:
    refresh.tick(RefreshRate)
    now = pygame.time.get_ticks()

      
        #if test:
         #   Otsu.x = Otsu.x/(resize.width/resize.dwidth)
          #  test = False
        #resize.width = width

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    Screen.fill((0, 0, 0))
    player.controls()
    player.math()
     

    renderorder = sorted(Entities, key=lambda sister:sister.z)

    for name in renderorder:
        if name in Sisters:
            name.aitracking()
        name.render()


    achieve.checker()
    #gangalicious.moveTo(100,100, 1, tween=gangalicious.easeInOutCirc)
    #print(Yotsuba.targetx)
    Loopingtherooms += 1
    pygame.display.update()
