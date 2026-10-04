from ..map_renderer import MapRenderer
from .. import ui_config


class GameScreen:
    def __init__(self, screen):
        self.screen = screen

        self.map_renderer = MapRenderer(screen, ui_config.TILE_SIZE)

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