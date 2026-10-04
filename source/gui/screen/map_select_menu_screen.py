import pygame
from .. import ui_config


class MapSelectMenuScreen:
    def __init__(self, screen):
        self.screen = screen

        self.title_font = pygame.font.Font(None, ui_config.TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)

        self.map_buttons = []
        self.back_button = pygame.Rect(30, 30, 100, 45)

    def draw(self, map_names, mode):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        if mode == "single":
            title_text = "SELECT SINGLE MAP"
        else:
            title_text = "SELECT COMPETITIVE MAP"

        title = self.title_font.render(title_text, True, ui_config.TITLE_COLOR)
        self.screen.blit(title, (190, 70))

        self.map_buttons = []

        y = 160

        for map_name in map_names:
            button = pygame.Rect(250, y, 300, 50)

            self.map_buttons.append((button, map_name))

            pygame.draw.rect(self.screen, ui_config.SINGLE_BUTTON_COLOR, button)

            text = self.button_font.render(map_name, True, ui_config.TEXT_COLOR)
            self.screen.blit(text, (280, y + 12))

            y = y + 60

        pygame.draw.rect(self.screen, ui_config.WALL_COLOR, self.back_button)

        back_text = self.button_font.render("Back", True, ui_config.TEXT_COLOR)
        self.screen.blit(back_text, (50, 40))