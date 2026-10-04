from ..mapRenderer import MapRenderer
from .. import uiConfig


class GameScreen:
    def __init__(self, screen):
        self.screen = screen

        self.mapRenderer = MapRenderer(screen, uiConfig.TILE_SIZE)

        self.state = None
        self.walls = None
        self.rows = 0
        self.columns = 0

    def loadGame(self, state):
        self.state = state
        self.walls = state.walls
        self.rows = state.height
        self.columns = state.width

    def draw(self):
        self.screen.fill(uiConfig.BACKGROUND_COLOR)

        if self.state is None:
            return

        self.mapRenderer.draw(self.walls, self.state, self.rows, self.columns)