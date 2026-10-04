import pygame

from ..map_renderer import MapRenderer
from .. import ui_config
from ..ui_components import draw_button


class GameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.renderer = MapRenderer(screen, ui_config.TILE_SIZE)

        self.button_font = pygame.font.Font(None, ui_config.BUTTON_FONT_SIZE)
        self.info_font = pygame.font.Font(None, ui_config.INFO_FONT_SIZE)

        self.back_button = pygame.Rect(20, 20, 100, 42)

        self.mode = None
        self.state = None

    def load_game(self, state, mode):
        self.mode = mode
        self.state = state.copy()

    def draw_info(self):
        if self.mode == "single":
            text = "Single map"
        else:
            text = "Competitive map"

        info = self.info_font.render(text, True, ui_config.TEXT_COLOR)
        self.screen.blit(info, (720, 160))

    def draw(self):
        self.screen.fill(ui_config.BACKGROUND_COLOR)

        if self.state is None:
            return

        map_width = self.state.width * ui_config.TILE_SIZE
        map_height = self.state.height * ui_config.TILE_SIZE

        offset_x = (680 - map_width) // 2
        offset_y = (ui_config.WINDOW_HEIGHT - map_height) // 2

        if offset_x < 20:
            offset_x = 20

        if offset_y < 90:
            offset_y = 90

        self.renderer.draw(self.state, offset_x, offset_y)
        draw_button(self.screen, self.back_button, self.button_font, "Back", ui_config.BACK_BUTTON_COLOR)
        self.draw_info()
