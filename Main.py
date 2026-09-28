import pygame
import math
import sys
import keyboard as keys
import pyautogui as gangalicious
import os 



from Proxy import Player

from naoko_ueno import QuintessentialQuintuplets

from Obstacle import Obstacles

from objects import Food

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
Active_food = []
player = Player(width, height, Screen, "w", "s", "a", "d", "space", "left shift", "q", "e")
#player2 = Player(width, height, Screen, "up", "down", "left", "right", "right ctrl", "right shift", "right alt")
players = [player]
fan = Obstacles(100, 4, 20, 20, height, Screen)
wall = Obstacles(300, 2, 50, 50, height, Screen)

objects = [fan, wall]


Ichika =  QuintessentialQuintuplets(0/width, height/2, 1, 15, 15, 0.3, 0.85, 200, 200, 0, Screen, width, height)
Nino =    QuintessentialQuintuplets(width/4, height/2, 1, 20, 25, 0.3, 0.65, 247, 37, 133,  Screen, width, height, traits={"tsundere":True})
Miku =    QuintessentialQuintuplets(width/2, height/2, 1, 10, 5, 0.05, 0.75, 72, 149, 239, Screen, width, height, traits={"shy":True})
Yotsuba = QuintessentialQuintuplets(width*3/4, height/2, 1, 13, 10, 0.2, 1, 112, 224, 0,  Screen, width, height, traits={"athletic":True})
Itsuki =  QuintessentialQuintuplets(width, height/2, 1, 5, 19, 0.5, 0.55, 239, 35, 60, Screen, width, height, traits={"fatso":True, "hungry":True})    

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
            if Active_food:
                name.aitracking(player, objects, Active_food[0])
            else:
                name.aitracking(player,objects)
                  
        name.render()


    achieve.checker(player, Sisters, objects, width)
    #gangalicious.moveTo(100,100, 1, tween=gangalicious.easeInOutCirc)
    #print(Yotsuba.targetx)dddddd
    Loopingtherooms += 1
    #print(Ichika.velocity)
    #print(Miku.velocity)
    #print("future x", player.futurex)
    #print("x", player.x)

    if player.isfood:
        meatbun = Food(player.x, player.y, player.z, Screen)
        Active_food.append(meatbun)
        Entities.append(meatbun)
        player.isfood = False
        Itsuki.doneating = False
        print('hello')

    if Itsuki.doneating:
        if Active_food:
            remove_food = Active_food.pop(0)
            if remove_food in Entities:
                Entities.remove(remove_food)
               
                

    print(Itsuki.Loopingtherooms % 500)
    #print(Itsuki.doneating)
    pygame.display.update()
