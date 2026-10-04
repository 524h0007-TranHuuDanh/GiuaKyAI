import os

from .screen.mainMenuScreen import MainMenuScreen
from .screen.mapSelectMenuScreen import MapSelectMenuScreen
from .screen.gameScreen import GameScreen
from ..shared.mapParser import parse_map


class ScreenController:
    def __init__(self, screen):
        self.mainMenuScreen = MainMenuScreen(screen)
        self.mapSelectMenuScreen = MapSelectMenuScreen(screen)
        self.gameScreen = GameScreen(screen)

        self.screenState = "mode"

        self.mode = None
        self.selectedMap = None
        self.mapNames = []

    def loadMapNames(self):
        if self.mode == "single":
            folder = "source/map/oneAgent"
        else:
            folder = "source/map/twoAgents"

        self.mapNames = []

        if not os.path.exists(folder):
            return

        for fileName in os.listdir(folder):
            if fileName.endswith(".txt"):
                self.mapNames.append(fileName)

        self.mapNames.sort()

    def selectMap(self, mapName):
        if self.mode == "single":
            folder = "source/map/oneAgent"
        else:
            folder = "source/map/twoAgents"

        self.selectedMap = os.path.join(folder, mapName)

        state = parse_map(self.selectedMap)

        self.gameScreen.loadGame(state)

        self.screenState = "game"

    def draw(self):
        if self.screenState == "mode":
            self.mainMenuScreen.draw()

        elif self.screenState == "map":
            self.mapSelectMenuScreen.draw(self.mapNames, self.mode)

        elif self.screenState == "game":
            self.gameScreen.draw()