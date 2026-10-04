import pygame

from ..map_renderer import MapRenderer
from .. import ui_config
from ..ui_components import draw_pixel_button


class GameScreen:
    def __init__(self, screen):
        self.screen = screen

        self.map_renderer = MapRenderer(screen, ui_config.TILE_SIZE)
        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)

        self.back_button = pygame.Rect(20, 20, 120, 50)

        self.state = None
        self.walls = None
        self.rows = 0
        self.columns = 0

    def load_game(self, state):
        self.state = state
        self.walls = state.walls
        self.rows = state.height
        self.columns = state.width

    def draw(self):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        if self.state is None:
            return

        self.map_renderer.draw(self.walls, self.state, self.rows, self.columns)

        draw_pixel_button(
            self.screen,
            self.back_button,
            self.button_font,
            "Back",
            ui_config.BACK_BUTTON_COLOR
        )