import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from text_visualization import *
from start_menu import start_menu

def main():

    pygame.init() #init pygame
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # define the screen size
    font = pygame.font.SysFont("freesansbold", 30) # define font 

    # Shot the start menu 
    menu_choice = start_menu(screen = screen, font = font)
    if menu_choice == "options":
        screen.blit("to be implemented")
        return 

    score_box = pygame.Surface((SCREEN_WIDTH // 4, SCREEN_HEIGHT // 8)) # define a score_box to display current score
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) # Instantiate a player
    
    dt = 0

    while True: #infinite game loop
        
        for event in pygame.event.get(): # Check for closed window and quit game
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black") # fill the screen black
        pygame.Surface.fill(score_box, "black") # fill the surface box black 

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split(player)
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        score_box_visualization(font = font, player = player,screen = screen) # Visualizes the score in a box

        pygame.display.flip()

       # 60 fps limit
        dt = clock.tick(60) / 1000 # delta time between frames in seconds

if __name__ == "__main__":
    main()