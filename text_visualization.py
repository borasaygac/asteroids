import pygame

def score_box_visualization(font, player, screen): #Print the current score of the player in the main screen
    txt_score_label = font.render("SCORE", True, "white")
    txt_score_value = font.render(f"{player.score}", True, "white")
    screen.blit(txt_score_label,(10, 10))
    screen.blit(txt_score_value, (txt_score_label.get_width() // 2, txt_score_label.get_height()* 1.5))