from pathlib import Path

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

        self.project_dir = Path(__file__).resolve().parents[2]

    def go_to_mode_menu(self):
        self.mode = None
        self.selected_map = None
        self.screen_state = "mode"

    def get_map_folder(self):
        if self.mode == "single":
            return self.project_dir / "source" / "map" / "one_agent"

        return self.project_dir / "source" / "map" / "two_agents"

    def load_map_names(self):
        folder = self.get_map_folder()
        self.map_names = []

        if not folder.exists():
            return

        for file_path in folder.iterdir():
            if file_path.suffix == ".txt":
                self.map_names.append(file_path.name)

        self.map_names.sort()

    def select_map(self, map_name):
        folder = self.get_map_folder()
        self.selected_map = folder / map_name

        state = parse_map(self.selected_map)
        self.game_screen.load_game(state, self.mode)
        self.screen_state = "game"

    def draw(self):
        if self.screen_state == "mode":
            self.main_menu_screen.draw()
        elif self.screen_state == "map":
            self.map_select_menu_screen.draw(self.map_names, self.mode)
        elif self.screen_state == "game":
            self.game_screen.draw()
