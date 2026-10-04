import os

from .screen.main_menu_screen import MainMenuScreen
from .screen.map_select_menu_screen import MapSelectMenuScreen
from .screen.game_screen import GameScreen
from ..shared.map_parser import parse_map


class ScreenController:
    def __init__(self, screen):
        self.main_menu_screen = MainMenuScreen(screen)
        self.map_select_menu_screen = MapSelectMenuScreen(screen)
        self.game_screen = GameScreen(screen)

        self.screen_state = "mode"

        self.mode = None
        self.selected_map = None
        self.map_names = []

    def load_map_names(self):
        if self.mode == "single":
            folder = "source/map/one_agent"
        else:
            folder = "source/map/two_agents"

        self.map_names = []

        if not os.path.exists(folder):
            return

        for file_name in os.listdir(folder):
            if file_name.endswith(".txt"):
                self.map_names.append(file_name)

        self.map_names.sort()

    def select_map(self, map_name):
        if self.mode == "single":
            folder = "source/map/one_agent"
        else:
            folder = "source/map/two_agents"

        self.selected_map = os.path.join(folder, map_name)

        state = parse_map(self.selected_map)

        self.game_screen.load_game(state)

        self.screen_state = "game"

    def draw(self):
        if self.screen_state == "mode":
            self.main_menu_screen.draw()

        elif self.screen_state == "map":
            self.map_select_menu_screen.draw(self.map_names, self.mode)

        elif self.screen_state == "game":
            self.game_screen.draw()