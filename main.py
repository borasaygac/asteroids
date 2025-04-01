import pygame
from constants import *

def main():

    pygame.init() #init pygame
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #define the screen size
    
    while True: #infinite game loop
        
        for event in pygame.event.get(): # Check for closed window and quit game
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black") 
        pygame.display.flip()
        delta = clock.tick(60) # 60 fps limit
        dt = delta / 1000 # delta time between frames in seconds

if __name__ == "__main__":
    main()