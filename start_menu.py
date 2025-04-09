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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left mouse click
                if start_rectangle.collidepoint(event.pos):
                    return "start"
                elif options_rectangle.collidepoint(event.pos):
                    return "options"
                elif exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def pause_menu(screen, font):
    # Displays the start menu with 3 buttons on it.
    # 1. Resume
    # 2. Restart 
    # 3. Quit

    while True:
        screen.fill("black")
        pause_text = font.render("Paused", True, "white")
        resume_button = font.render("Resume", True, "white")
        restart_button = font.render("Restart", True, "white")
        quit_button = font.render("Quit Game", True, "white")

        # Get button rectangles for positioning
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        resume_rect = resume_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        restart_rect = restart_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        quit_rect = quit_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        # Draw buttons and title
        screen.blit(pause_text, pause_rect)
        screen.blit(resume_button, resume_rect)
        screen.blit(restart_button, restart_rect)
        screen.blit(quit_button, quit_rect)

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse click
                if resume_rect.collidepoint(event.pos):
                    return "resume"
                elif restart_rect.collidepoint(event.pos):
                    return "restart"
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()