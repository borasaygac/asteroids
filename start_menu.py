import pygame 
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def start_menu(screen, font):
    # Displays the start menu with 3 buttons on it.
    # 1. Start game
    # 2. Options 
    # 3. Exit

    while True:

        screen.fill("black")
        title_text = font.render("Asteroids Game", "True", "white")
        start_button = font.render("Start Game", "True", "white")
        options_button = font.render("Options", "True", "white")
        exit_button = font.render("Quit Game", "True", "white")

        # get the button rectangles and their positions 
        title_rectangle = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        start_rectangle = start_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        options_rectangle = options_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        exit_rectangle = exit_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        # draw the buttons on the screen
        screen.blit(title_text, title_rectangle)
        screen.blit(start_button, start_rectangle)
        screen.blit(options_button, options_rectangle)
        screen.blit(exit_button, exit_rectangle)

        pygame.display.flip()

        #handle the events

                                              