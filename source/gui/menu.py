import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen

        self.titleFont = pygame.font.Font(None, 50)
        self.buttonFont = pygame.font.Font(None, 35)

        self.singleButton = pygame.Rect(250, 220, 300, 70)
        self.competitiveButton = pygame.Rect(250, 330, 300, 70)

        self.singleButtonColor = (100, 150, 220)
        self.competitiveButtonColor = (100, 180, 120)

    def draw(self):
        self.screen.fill((240, 240, 240))

        title = self.titleFont.render("SOKOBAN AI", True, (0, 0, 0))
        self.screen.blit(title, (300, 100))

        pygame.draw.rect(self.screen, self.singleButtonColor, self.singleButton)
        pygame.draw.rect(self.screen, self.competitiveButtonColor, self.competitiveButton)

        singleText = self.buttonFont.render("Single Agent", True, (255, 255, 255))
        competitiveText = self.buttonFont.render("Competitive", True, (255, 255, 255))

        self.screen.blit(singleText, (320, 240))
        self.screen.blit(competitiveText, (315, 350))