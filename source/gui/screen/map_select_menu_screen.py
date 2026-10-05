import pygame
from .. import ui_config


class MapSelectMenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, ui_config.TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)
        self.back_button = pygame.Rect(25, 25, 110, 45)
        self.map_buttons = []

    def draw(self, map_names, mode):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        if mode == "single":
            title_text = "SELECT SINGLE MAP"
            button_color = ui_config.SINGLE_BUTTON_COLOR
        else:
            title_text = "SELECT COMPETITIVE MAP"
            button_color = ui_config.COMPETITIVE_BUTTON_COLOR

        title = self.title_font.render(title_text, True, ui_config.TEXT_COLOR)
        self.screen.blit(title, title.get_rect(center=(ui_config.WINDOW_WIDTH // 2, 90)))

        self.map_buttons = []
        y = 150
        for map_name in map_names:
            button = pygame.Rect(340, y, 320, 48)
            self.map_buttons.append((button, map_name))
            ui_config.draw_button(self.screen, button, self.button_font, map_name, button_color)
            y += 60

        ui_config.draw_button(self.screen, self.back_button, self.button_font, "Back", ui_config.BACK_BUTTON_COLOR)