import pygame
from .. import ui_config
from ..ui_components import draw_pixel_button


class MainMenuScreen:
    def __init__(self, screen):
        self.screen = screen

        self.title_font = pygame.font.Font(None, ui_config.TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)

        self.background = pygame.image.load(ui_config.BACKGROUND_IMAGE).convert()
        self.background = pygame.transform.scale(self.background, (ui_config.WINDOW_WIDTH, ui_config.WINDOW_HEIGHT))

        button_width = 300
        button_height = 70
        button_x = (ui_config.WINDOW_WIDTH - button_width) // 2

        self.single_button = pygame.Rect(button_x, 220, button_width, button_height)
        self.competitive_button = pygame.Rect(button_x, 330, button_width, button_height)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        title = self.title_font.render("SOKOBAN", True, ui_config.TITLE_COLOR)
        title_rect = title.get_rect(center=(ui_config.WINDOW_WIDTH // 2, 110))
        self.screen.blit(title, title_rect)

        draw_pixel_button(self.screen, self.single_button, self.button_font, "Single", ui_config.SINGLE_BUTTON_COLOR)
        draw_pixel_button(self.screen, self.competitive_button, self.button_font, "Competitive", ui_config.COMPETITIVE_BUTTON_COLOR)