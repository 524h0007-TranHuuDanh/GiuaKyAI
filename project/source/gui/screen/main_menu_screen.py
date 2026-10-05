import pygame
from .. import ui_config


class MainMenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, ui_config.TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)
        self.single_button = pygame.Rect(350, 230, 300, 60)
        self.competitive_button = pygame.Rect(350, 320, 300, 60)

    def draw(self):
        self.screen.fill(ui_config.BACKGROUND_COLOR)
        title = self.title_font.render("SOKOBAN", True, ui_config.TEXT_COLOR)
        self.screen.blit(title, title.get_rect(center=(ui_config.WINDOW_WIDTH // 2, 130)))
        ui_config.draw_button(self.screen, self.single_button, self.button_font, "Single", ui_config.SINGLE_BUTTON_COLOR)
        ui_config.draw_button(self.screen, self.competitive_button, self.button_font, "Competitive", ui_config.COMPETITIVE_BUTTON_COLOR)