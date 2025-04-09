import pygame

class InitialsInputBox:
    def __init__(self, x, y, width, height, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color("lightskyblue3")
        self.color_active = pygame.Color("dodgerblue2")
        self.color = self.color_inactive
        self.text = ''
        self.font = font
        self.txt_surface = font.render(self.text, True, self.color)
        self.active = False
        self.max_length = 3 # for 3 letter initials

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggles active state if clicked
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else: 
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text.upper()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < self.max_length and event.unicode.isalpha():
                    self.text += event.unicode.upper()
        
        self.txt_surface = self.font.render(self.text, True, self.color)
        return None
            
    def draw(self, screen):
        # draw the text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # draw rect 
        pygame.draw.rect(screen, self.color, self.rect, 2)
