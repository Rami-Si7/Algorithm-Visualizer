import pygame

BUTTON_HOVER_COLOR = (150, 150, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)


class Button:
    def __init__(self, text, pos, width, height, font, bg="black", fg="white"):
        self.text = text
        self.pos = pos
        self.width = width
        self.height = height
        self.font = font
        self.bg = bg
        self.fg = fg
        self.rect = pygame.Rect(pos, (width, height))
        self.text_surf = font.render(text, True, self.fg)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(screen, self.bg, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
