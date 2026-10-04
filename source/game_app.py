import pygame

from .gui.screen_controller import ScreenController
from .gui.event_handler import EventHandler
from .gui import ui_config


class GameApp:
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((ui_config.WINDOW_WIDTH, ui_config.WINDOW_HEIGHT))
        pygame.display.set_caption("Sokoban")

        screen_controller = ScreenController(screen)
        event_handler = EventHandler(screen_controller)

        running = True

        while running:
            running = event_handler.handle_events()

            screen_controller.draw()

            pygame.display.flip()

        pygame.quit()