import pygame
from .. import uiConfig


class MainMenuScreen:
    def __init__(self, screen):
        self.screen = screen

        self.titleFont = pygame.font.Font(None, uiConfig.TITLE_FONT_SIZE)
        self.buttonFont = pygame.font.Font(None, uiConfig.BUTTON_FONT_SIZE)

        self.singleButton = pygame.Rect(250, 220, 300, 70)
        self.competitiveButton = pygame.Rect(250, 330, 300, 70)

    def draw(self):
        self.screen.fill(uiConfig.BACKGROUND_COLOR)

        title = self.titleFont.render("SOKOBAN", True, uiConfig.TITLE_COLOR)
        self.screen.blit(title, (300, 100))

        pygame.draw.rect(self.screen, uiConfig.SINGLE_BUTTON_COLOR, self.singleButton)
        pygame.draw.rect(self.screen, uiConfig.COMPETITIVE_BUTTON_COLOR, self.competitiveButton)

        singleText = self.buttonFont.render("Single", True, uiConfig.TEXT_COLOR)
        competitiveText = self.buttonFont.render("Competitive", True, uiConfig.TEXT_COLOR)

        self.screen.blit(singleText, (355, 240))
        self.screen.blit(competitiveText, (320, 350))