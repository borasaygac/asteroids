import pygame
import sys
from src.constants import *
from src.player import *
from src.asteroids import *
from src.asteroidfield import *
from src.text_visualization import *
from src.start_menu import start_menu, pause_menu

def main():

    pygame.init() #init pygame
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # define the screen size
    font = pygame.font.SysFont("freesansbold", 30) # define font 

    # Show the start menu 
    menu_choice = start_menu(screen = screen, font = font)
    if menu_choice == "options":
        screen.blit(screen ,"to be implemented")
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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Listen for Escape key
                pause_choice = pause_menu(screen = screen, font = font)
                if pause_choice == "restart":
                    return main() # Restart the game
                elif pause_choice == "resume":
                    continue
            
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