import pygame
from .. import ui_config
from ..ui_components import draw_button


class MapSelectMenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, ui_config.TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)
        self.map_buttons = []
        self.back_button = pygame.Rect(25, 25, 110, 45)

    def draw(self, map_names, mode):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        if mode == "single":
            title_text = "SELECT SINGLE MAP"
            button_color = ui_config.SINGLE_BUTTON_COLOR
        else:
            title_text = "SELECT COMPETITIVE MAP"
            button_color = ui_config.COMPETITIVE_BUTTON_COLOR

        title = self.title_font.render(title_text, True, ui_config.TEXT_COLOR)
        title_rect = title.get_rect(center=(ui_config.WINDOW_WIDTH // 2, 90))
        self.screen.blit(title, title_rect)

        self.map_buttons = []
        button_width = 320
        button_height = 48
        button_x = (ui_config.WINDOW_WIDTH - button_width) // 2
        y = 150

        for map_name in map_names:
            button = pygame.Rect(button_x, y, button_width, button_height)
            self.map_buttons.append((button, map_name))
            draw_button(self.screen, button, self.button_font, map_name, button_color)
            y += 60

        draw_button(
            self.screen,
            self.back_button,
            self.button_font,
            "Back",
            ui_config.BACK_BUTTON_COLOR
        )