import pygame
from .. import ui_config
from ..ui_components import draw_button


class MainMenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, ui_config.TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)

        button_width = 300
        button_height = 60
        button_x = (ui_config.WINDOW_WIDTH - button_width) // 2

        self.single_button = pygame.Rect(button_x, 230, button_width, button_height)
        self.competitive_button = pygame.Rect(button_x, 320, button_width, button_height)

    def draw(self):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        title = self.title_font.render("SOKOBAN", True, ui_config.TEXT_COLOR)
        title_rect = title.get_rect(center=(ui_config.WINDOW_WIDTH // 2, 130))
        self.screen.blit(title, title_rect)

        draw_button(
            self.screen,
            self.single_button,
            self.button_font,
            "Single",
            ui_config.SINGLE_BUTTON_COLOR
        )

        draw_button(
            self.screen,
            self.competitive_button,
            self.button_font,
            "Competitive",
            ui_config.COMPETITIVE_BUTTON_COLOR
        )
