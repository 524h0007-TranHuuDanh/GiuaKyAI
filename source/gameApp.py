import pygame

from .gui.screenController import ScreenController
from .gui.eventHandler import EventHandler
from .gui import uiConfig


class GameApp:
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((uiConfig.WINDOW_WIDTH, uiConfig.WINDOW_HEIGHT))
        pygame.display.set_caption("Sokoban")

        screenController = ScreenController(screen)
        eventHandler = EventHandler(screenController)

        running = True

        while running:
            running = eventHandler.handleEvents()

            screenController.draw()

            pygame.display.flip()

        pygame.quit()