import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

color = (255,192,120)
x, y = 100, 100
width, height = 400, 300
thickness = 2
pygame.draw.rect(screen, color, (x,y,width,height), thickness)

while (True):
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
   pygame.display.update()
