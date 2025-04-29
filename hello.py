import sys
import pygame


pygame.init()
pygame.display.set_caption("Alien Invasion")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
  
