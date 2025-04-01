import pygame
from constants import *

def main():

    pygame.init() #init pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #define the screen size
    while True:
        
        for event in pygame.event.get(): # Check for closed window and quit game
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black") 
        pygame.display.flip()

if __name__ == "__main__":
    main()