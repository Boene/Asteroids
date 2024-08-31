import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    i = 1
    while i < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return
        pygame.Surface.fill(screen, color = (0,0,0))
        pygame.display.flip()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

if __name__ =="__main__":
    main()