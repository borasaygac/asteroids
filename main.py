import pygame
from constants import *
from player import *

def main():

    pygame.init() #init pygame
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #define the screen size
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) # Instantiate a player

    dt = 0

    while True: #infinite game loop
        
        for event in pygame.event.get(): # Check for closed window and quit game
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black") 

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

       # 60 fps limit
        dt = clock.tick(60) / 1000 # delta time between frames in seconds

        

if __name__ == "__main__":
    main()