import pygame
from .. import uiConfig


class MapSelectMenuScreen:
    def __init__(self, screen):
        self.screen = screen

        self.titleFont = pygame.font.Font(None, uiConfig.TITLE_FONT_SIZE)
        self.buttonFont = pygame.font.Font(None, uiConfig.BUTTON_FONT_SIZE)

        self.mapButtons = []
        self.backButton = pygame.Rect(30, 30, 100, 45)

    def draw(self, mapNames, mode):
        self.screen.fill(uiConfig.BACKGROUND_COLOR)

        if mode == "single":
            titleText = "SELECT SINGLE MAP"
        else:
            titleText = "SELECT COMPETITIVE MAP"

        title = self.titleFont.render(titleText, True, uiConfig.TITLE_COLOR)
        self.screen.blit(title, (190, 70))

        self.mapButtons = []

        y = 160

        for mapName in mapNames:
            button = pygame.Rect(250, y, 300, 50)

            self.mapButtons.append((button, mapName))

            pygame.draw.rect(self.screen, uiConfig.SINGLE_BUTTON_COLOR, button)

            text = self.buttonFont.render(mapName, True, uiConfig.TEXT_COLOR)
            self.screen.blit(text, (280, y + 12))

            y = y + 60

        pygame.draw.rect(self.screen, uiConfig.WALL_COLOR, self.backButton)

        backText = self.buttonFont.render("Back", True, uiConfig.TEXT_COLOR)
        self.screen.blit(backText, (50, 40))