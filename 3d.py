import math
import numpy as moonpie
import pygame
import sys
import keyboard as wankel

pygame.init()
width = 800
height = 600
Screen = pygame.display.set_mode((width, height))
RefreshRate = 24
refresh = pygame.time.Clock()

anglex = math.radians(1)
angley = math.radians(1)
anglez = math.radians(1)

cx, sx = math.cos(anglex), math.sin(anglex)
cy, sy = math.cos(angley), math.sin(angley)
cz, sz = math.cos(anglez), math.sin(anglez)


x_offset = 0
y_offset = 0
z_offset = 0




p1 = moonpie.array([-1000, -1000, 5, 1])
p2 = moonpie.array([1000, -1000, 5, 1])
p3 = moonpie.array([1000, 1000, 5, 1])
p4 = moonpie.array([-1000, 1000, 5, 1])
p5 = moonpie.array([-1000, -1000, 10, 1])
p6 = moonpie.array([1000, -1000, 10, 1])
p7 = moonpie.array([1000, 1000, 10, 1])
p8 = moonpie.array([-1000, 1000, 10, 1])
original = [p1, p4, p3, p2, p1, p2, p6, p7, p3, p7, p8, p4, p8, p5, p6, p5]
changed = [p1, p4, p3, p2, p1, p2, p6, p7, p3, p7, p8, p4, p8, p5, p6, p5]
points = [p1, p4, p3, p2, p1, p2, p6, p7, p3, p7, p8, p4, p8, p5, p6, p5]


movex = moonpie.array(
    [[1, 0, 0, 0],
     [0, cx, -sx, 0],
     [0, sx, cx, 0],
     [0, 0, 0, 1]])

movey = moonpie.array(
    [[cy, 0, sy, 0],
     [0, 1, 0, 0],
     [-sy, 0, cy, 0],
     [0, 0, 0, 1]])
movez = moonpie.array(
    [[cz, -sz, 0, 0],
     [sz, cz, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]])



def shift(x, y, z):     
    if wankel.is_pressed("up"):
        y = -100

    elif wankel.is_pressed("down"):
        y = 100

    if wankel.is_pressed("left"):
        x = -100

    elif wankel.is_pressed("right"):
        x = 100

    if wankel.is_pressed("q"):
        #smaller
        z = 1

    elif wankel.is_pressed("e"):
        z = -1
        #bigger
        

    return x, y, z

def rotate(ax, ay, az):
    ax, ay, az = 0, 0, 0
    if wankel.is_pressed("a"):
        ax = -5

    elif wankel.is_pressed("d"):
        ax = 5

    if wankel.is_pressed("w"):
        ay = -5

    elif wankel.is_pressed("s"):
        ay = 5

    if wankel.is_pressed("z"):
        az = -5

    elif wankel.is_pressed("x"):
        az = 5

    return ax, ay, az

while True:
    refresh.tick(RefreshRate)
    Screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    


        
    #pygame.draw.rect(Screen,(255,255,255), (x1/z1 + width/2, y1/z1 + height/2, 300/z1, 300/z1))
    #pygame.draw.circle(Screen, (255, 255, 255), (x1/z1 + width/2, y1/z1 + height/2), 300/z1,)
    #pygame.draw.rect(Screen,(255,255,255), (width/2, height/2, 10, 10))


    x_offset = y_offset = z_offset = 0
    #x_rotate, y_rotate = math.cos(0), math.sin(0)
    anglex, angley, anglez = rotate(anglex, angley, anglez)

    cx, sx = math.cos(anglex), math.sin(anglex)
    cy, sy = math.cos(angley), math.sin(angley)
    cz, sz = math.cos(anglez), math.sin(anglez)

    movex[1][1], movex[1][2], movex[2][1], movex[2][2] = cx, -sx, sx, cx
    movey[0][0], movey[0][2], movey[2][0], movey[2][2] = cy, sy, -sy, cy
    movez[0][0], movez[0][1], movez[1][0], movez[1][1] = cz, -sz, sz, cz 

    move = movez @ movey @ movex
        
        
    x_offset, y_offset, z_offset = shift(x_offset, y_offset, z_offset)

    move[0][3] = x_offset
    move[1][3] = y_offset
    move[2][3] = z_offset
    



    #move = moonpie.array(
    #    [[c, -s, 0, x_offset],
    #     [s, c, 0, y_offset],
    #     [0, 0, 1, z_offset],
    #     [0, 0, 0, 1]])

    for i in range(len(original)):


        changed[i] = move @ changed[i]
        print(move)
        #print(changed[0])
        
        pygame.draw.circle(Screen, (255, 255, 255), (changed[0][0]/changed[0][2] + width/2, changed[0][1]/changed[0][2] + height/2), 100/changed[0][2])
        

        #pygame.draw.line(Screen, (255, 255, 255), (changed[1][0]/changed[1][2] + width/2, changed[1][1]/changed[1][2] + height/2), (changed[2][0]/changed[2][2] + width/2, changed[2][1]/changed[2][2] + height/2))
        #pygame.draw.line(Screen, (255, 255, 255), (changed[i][0]/changed[i][2] + width/2, changed[i][1]/changed[i][2] + height/2), (changed[(i+1)%len(changed)][0]/changed[(i+1)%len(changed)][2] + width/2, changed[(i+1)%len(changed)][1]/changed[(i+1)%len(changed)][2] + height/2))
        
        



    pygame.display.update()
#code is still in progress lol thats why it seems a bit messy. im new to matrices so bear with me
