import pygame
import math
import sys
import keyboard as keys
import pyautogui as gangalicious
import os 
import random


from Proxy import Player
from naoko_ueno import QuintessentialQuintuplets
from Obstacle import Obstacles
from objects import Food
from draw_test import Draw, pen

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



Nino =    QuintessentialQuintuplets(width/4, height/2, 1, 20, 25, 0.3, 0.70, 0.035, 247, 37, 133,  Screen, width, height, traits={"tsundere":True})
Miku =    QuintessentialQuintuplets(width/2, height/2, 1, 10, 5, 0.05, 0.75, 0.055, 72, 149, 239, Screen, width, height, traits={"shy":True, "loved":True})
Yotsuba = QuintessentialQuintuplets(width*3/4, height/2, 1, 13, 10, 0.2, 1, 0.1, 112, 224, 0,  Screen, width, height, traits={"athletic":True})
Itsuki =  QuintessentialQuintuplets(width, height/2, 1, 5, 19, 0.3, 0.65, 0.065, 239, 35, 60, Screen, width, height, traits={"fatso":True, "hungry":True})    
Ichika =  QuintessentialQuintuplets(0, height/2, 1, 15, 15, 0.3, 0.85, 0.05, 200, 200, 0, Screen, width, height, tomimic=Yotsuba, traits={"mimic":True})

Sisters = [Ichika, Nino, Miku, Yotsuba, Itsuki]
Entities = Sisters + objects + players

from achievements import achievements

achieve = achievements()


npc_number = 0
npc_name = "Miku_Lover_#"
Warriors = []
Warrior_Names = []
Warrior_Dialogues = ["I WILL FIGHT FOR MIKU", 
                     "Oh hey bob, u a miku  fan too??", 
                     "MIKU IS THE BEST QUINTESSENTIAL QUINTUPLET", 
                     "..with the sole exception of-- SHUT UP, NINO IS NOT THE SOLE EXCEPTION", 
                     "i love femboys but no one will know",
                     "Miku is soo cute",
                     "Hi lol (will it work?)",
                     "Yoo mike, u a fan of miku??",
                     "LARPER. I KNOW YOU LIKE NINO",
                     "I WILL DIE FOR MIKU",
                     "Who are we chasing Miku??",
                     "I WILL EAT MIKU'S FOOD",
                     "Stand aside chuds, let me impress Miku",
                     "I don't think this is the Hatsune Miku fan club",
                     "0 episodes, 100 edits, larp is free but not for Miku",
                     "Miku's food taste so good!!",
                     "I HEART MIKU",
                     "Fuutarou shoulda chosen Miku :((",
                     "But would Fuutarou be truly happy if it were Miku?",
                     "HEY NO SPOILERS",
                     "i REALLY love femboys",
                     "Im thinking Miku Miku oo-eee-oo",
                     "Ain't miku a vocaloid",
                     "She does NOT have twin tails",
                     "SHUT UP LARPERS, THIS THE REAL MIKU",
                     "...with the sole exception of Nakano Nin--SHUT UPPP",
                     "I can recite every single line of Miku's part in gotoubun no kimochi...'Futarou!!', 'Mittsu massugu na kono kimochi'...",
                     "WHO HAS THE WS990BT I NEED IT",
                     "FOR MIKU I WILL DO MY ASSIGNMENTS",
                     "FOR MIKU I WILL DO MY WORK",
                     "MIKUTEACHESEVERYTHING IS SO GOATED"
                     "HIIIII MIKUUUU",
                     "Ranking the quintessential quintuplets, id rank Miku, Miku, Miku, Miku and maybe just maybe...Miku",
                     "WE ARE THE BRIDES WE ARE THE BRIDES PLEASE",
                     "FUUTAROU PASS THE DAM CONTROLLER IF YOU WONT PLAY",
                     "..maybe fuutarou found joy with -- NO SPOILERS",
                     "haha you chuds, i have the ws990bt..whats that you say? these are bootleg? NOOOO",
                     "Miku Nakano rhymes with 'My Wife'",
                     "BACK OFF SHE'S MINE",
                     "MIKU DO U WANT SOME FOOD??",
                     ]
Pen = pen(width, height, Screen)
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
        p.math(Itsuki)
     

    renderorder = sorted(Entities, key=lambda sister:sister.z)

    #currently debugging sorry if its not the entire gang
    for name in renderorder:
        if name == Ichika or name == Yotsuba:
            if Active_food:
                name.aitracking(player, objects, Active_food[0])
            else:
                name.aitracking(player,objects)

        name.render()


    achieve.checker(player, Sisters, objects, width)
    #gangalicious.moveTo(100,100, 1, tween=gangalicious.easeInOutCirc)
    #print(Yotsuba.targetx)dddddd
    
    #print(Ichika.velocity)
    #print(Miku.velocity)
    #print("future x", player.futurex)
    #print("x", player.x)
    
    Pen.move()
    Wall = Draw(Pen.x, Pen.y, Pen.z, Screen)

    Entities.append(Wall)


    if player.isfood:
        meatbun = Food(player.x, player.y, player.z, Screen)
        Active_food.append(meatbun)
        Entities.append(meatbun)
        player.isfood = False
        Itsuki.doneating = False

    if Itsuki.doneating:
        if Active_food:
            remove_food = Active_food.pop(0)
            if remove_food in Entities:
                Entities.remove(remove_food)

    if Miku.summon and npc_number < 10:
        npc_number += 1
        npc_actualname = npc_name + str(npc_number)


        Warrior_Names.append(npc_actualname)

        print()
        print(f"{npc_actualname}: '{random.choice(Warrior_Dialogues)}'")
        print()

        npc_actualname = QuintessentialQuintuplets(Miku.x, Miku.y, Miku.z, 10, 5, 0.05, 0.75, 0.055, 72, 100, 249, Screen, width, height, widtho=width/384, heighto= height/72)
        Entities.append(npc_actualname)
        Warriors.append(npc_actualname)
        Miku.summon = False
    

    if Loopingtherooms % 500 == 0 and Warrior_Names:
        print()
        print(f"{random.choice(Warrior_Names)}: '{random.choice(Warrior_Dialogues)}'")
        print()
    Loopingtherooms += 1
        
               
                

    #print(Itsuki.velocity)
    #print(Itsuki.doneating)
    
    pygame.display.update()
    
