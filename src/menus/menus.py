import pygame 
import sys
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH, LEADERBOARD_PATH, MAX_ENTRIES, BG_COLOR, TITLE_COLOR
from .input_box import InitialsInputBox
from ..leaderboard.leaderboard import load_leaderboard

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

def final_menu(screen, score):
    pygame.font.init()
    font = pygame.font.SysFont('consolas', 48)
    small_font = pygame.font.SysFont('consolas', 24)
    clock = pygame.time.Clock()

    leaderboard = load_leaderboard()
    is_high_score = len(leaderboard) < MAX_ENTRIES or score > leaderboard[-1]['score']
    initials = ""

    if is_high_score:
        input_box = InitialsInputBox(300, 220, 140, 50, font)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if is_high_score:
                result = input_box.handle_event(event)
                if result:
                    initials = result
                    add_score(initials, score, leaderboard, MAX_ENTRIES)
                    save_leaderboard(LEADERBOARD_PATH, leaderboard)
                    is_high_score = False  # Hide input box now

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "replay"
                elif event.key == pygame.K_q:
                    return "quit"

        screen.fill(BG_COLOR)

        # Title
        title = font.render("GAME OVER", True, TITLE_COLOR)
        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 50))

        # Score
        score_text = font.render(f"Your Score: {score}", True, "white")
        screen.blit(score_text, (screen.get_width()//2 - score_text.get_width()//2, 120))

        # Input for initials
        if is_high_score:
            prompt = small_font.render("New High Score! Enter your initials:", True, "white")
            screen.blit(prompt, (screen.get_width()//2 - prompt.get_width()//2, 180))
            input_box.draw(screen)
        
        # Leaderboard
        leaderboard_title = small_font.render("Top Pilots of the Galaxy:", True, "white")
        screen.blit(leaderboard_title, (screen.get_width()//2 - leaderboard_title.get_width()//2, 300))

        for idx, entry in enumerate(leaderboard[:MAX_ENTRIES]):
            line = small_font.render(f"{idx+1}. {entry['name']} .... {entry['score']}", True, "white")
            screen.blit(line, (screen.get_width()//2 - line.get_width()//2, 340 + idx * 30))

        # Footer
        footer = small_font.render("[R] Replay    [Q] Quit", True, "white")
        screen.blit(footer, (screen.get_width()//2 - footer.get_width()//2, screen.get_height() - 60))

        pygame.display.flip()
        clock.tick(30)


    