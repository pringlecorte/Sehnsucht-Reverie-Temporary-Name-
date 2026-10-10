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

move = movez @ movey @ movex

def shift(x, y, z, p):     
    if wankel.is_pressed("up"):
        y = -10

    elif wankel.is_pressed("down"):
        y = 10

    if wankel.is_pressed("left"):
        x = -10

    elif wankel.is_pressed("right"):
        x = 10

    if wankel.is_pressed("q"):
        #smaller
        z = 1

    elif wankel.is_pressed("e"):
        #bigger
        if p[2] > 1: 
            z = -1

    return x, y, z

def rotate(x, y):
    global angle
    if wankel.is_pressed("a"):
        angle -= 5

    elif wankel.is_pressed("d"):
        angle += 5

    if wankel.is_pressed("w"):
        angle -= 5

    elif wankel.is_pressed("s"):
        y += math.sin(angle)  
        angle += 5  

    return x, y

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

    



    #move = moonpie.array(
    #    [[c, -s, 0, x_offset],
    #     [s, c, 0, y_offset],
    #     [0, 0, 1, z_offset],
    #     [0, 0, 0, 1]])
    
    for i in range(len(points)):
        x_offset, y_offset, z_offset = shift(x_offset, y_offset, z_offset, points[i])
        #x_rotate, y_rotate = rotate(x_rotate, y_rotate)
        move[0][3] = x_offset
        move[1][3] = y_offset
        move[2][3] = z_offset

        #move[0][0], move[0][1] = x_rotate, -y_rotate
        #move[1][0], move[1][1] = y_rotate, x_rotate 

        #print(x_rotate)
        #pygame.draw.circle(Screen, (255, 255, 255), (points[i][0]/points[i][2] + width/2, points[i][1]/points[i][2] + height/2), 100/points[i][2])
        

        #pygame.draw.line(Screen, (255, 255, 255), (points[1][0]/points[1][2] + width/2, points[1][1]/points[1][2] + height/2), (points[2][0]/points[2][2] + width/2, points[2][1]/points[2][2] + height/2))
        pygame.draw.line(Screen, (255, 255, 255), (points[i][0]/points[i][2] + width/2, points[i][1]/points[i][2] + height/2), (points[(i+1)%len(points)][0]/points[(i+1)%len(points)][2] + width/2, points[(i+1)%len(points)][1]/points[(i+1)%len(points)][2] + height/2))

        #points[i] = move @ points[i]


    pygame.display.update()
#code is still in progress lol thats why it seems a bit messy. im new to matrices so bear with me