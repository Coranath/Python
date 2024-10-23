import pygame
import math

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

WIDTH = 80
HEIGHT = 80
MARGIN = 5
grid = []

for row in range(3):
    grid.append([])
    for column in range(3):
        grid[row].append(0)

pygame.init()

window_size = [255,255]

scr = pygame.display.set_mode(window_size)

pygame.display.set_caption("Grid")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = math.ceil(pos[0]/85)-1
            row = math.ceil(pos[1]/85)-1
            grid[row][column] = 1
            print("Click ", pos, " Grid coordinates: ", row, column)
    #scr.fill(black)
    for row in range(3):
        for column in range(3):
            color = white
            pygame.draw.line(scr, color, (WIDTH*(column+1),HEIGHT*(row+1)),
             (WIDTH*(column+1)+80, HEIGHT*(row+1)))
    clock.tick(50)
    pygame.display.flip()

pygame.quit()

