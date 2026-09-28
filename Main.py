import pygame
import math
import sys
import keyboard as keys
import pyautogui as gangalicious
import os 



from Proxy import Player

from naoko_ueno import QuintessentialQuintuplets

from Obstacle import Obstacles


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


width = 800
height = 600
RefreshRate = 60
Screen = pygame.display.set_mode((width, height))
gangalicious.PAUSE = False
Loopingtherooms = 0


refresh = pygame.time.Clock()
test = True
n = 0
s = 0
n = pygame.time.get_ticks()

player = Player(width, height, Screen, "w", "s", "a", "d", "space", "left shift", "q")
#player2 = Player(width, height, Screen, "up", "down", "left", "right", "right ctrl", "right shift", "right alt")
players = [player]
fan = Obstacles(100, 4, 20, 20, height, Screen)
wall = Obstacles(300, 2, 50, 50, height, Screen)

objects = [fan, wall]


Ichika =  QuintessentialQuintuplets(0/width, height/2, 1, 10, 15, 0.3, 0.85, 200, 200, 0, Screen, width, height, traits={"clingy":True})
Nino =    QuintessentialQuintuplets(width/4, height/2, 1, 14, 25, 0.3, 0.65, 247, 37, 133,  Screen, width, height, traits={"tsundere":True})
Miku =    QuintessentialQuintuplets(width/2, height/2, 1, 5, 5, 0.05, 0.75, 72, 149, 239, Screen, width, height, traits={"shy":True})
Yotsuba = QuintessentialQuintuplets(width*3/4, height/2, 1, 10, 10, 0.2, 1, 112, 224, 0,  Screen, width, height, traits={"athletic":True})
Itsuki =  QuintessentialQuintuplets(width, height/2, 1, 5, 10, 0.5, 0.55, 239, 35, 60, Screen, width, height, traits={"fatso":True})    

Sisters = [Ichika, Nino, Miku, Yotsuba, Itsuki]
Entities = Sisters + objects + players

from achievements import achievements

achieve = achievements()


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

    for p in players:
        p.controls()
        p.math()
     

    renderorder = sorted(Entities, key=lambda sister:sister.z)

    for name in renderorder:
        if name in Sisters:
            name.aitracking(player, objects)
        name.render()


    achieve.checker(player, Sisters, objects, width)
    #gangalicious.moveTo(100,100, 1, tween=gangalicious.easeInOutCirc)
    #print(Yotsuba.targetx)
    Loopingtherooms += 1
    print(Ichika.velocity)
    #print(Miku.velocity)
    pygame.display.update()