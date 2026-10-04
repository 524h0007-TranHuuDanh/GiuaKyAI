import pygame
from .. import ui_config


class MainMenuScreen:
    def __init__(self, screen):
        self.screen = screen

        self.title_font = pygame.font.Font(None, ui_config.TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)

        self.single_button = pygame.Rect(250, 220, 300, 70)
        self.competitive_button = pygame.Rect(250, 330, 300, 70)

    def draw(self):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        title = self.title_font.render("SOKOBAN", True, ui_config.TITLE_COLOR)
        self.screen.blit(title, (300, 100))

        pygame.draw.rect(self.screen, ui_config.SINGLE_BUTTON_COLOR, self.single_button)
        pygame.draw.rect(self.screen, ui_config.COMPETITIVE_BUTTON_COLOR, self.competitive_button)

        single_text = self.button_font.render("Single", True, ui_config.TEXT_COLOR)
        competitive_text = self.button_font.render("Competitive", True, ui_config.TEXT_COLOR)

        self.screen.blit(single_text, (355, 240))
        self.screen.blit(competitive_text, (320, 350))