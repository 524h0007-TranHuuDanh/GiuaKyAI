import pygame


class EventHandler:
    def __init__(self, screenController):
        self.screenController = screenController

    def handleModeMenu(self, mousePosition):
        if self.screenController.mainMenuScreen.singleButton.collidepoint(mousePosition):
            self.screenController.mode = "single"
            self.screenController.loadMapNames()
            self.screenController.screenState = "map"

        elif self.screenController.mainMenuScreen.competitiveButton.collidepoint(mousePosition):
            self.screenController.mode = "competitive"
            self.screenController.loadMapNames()
            self.screenController.screenState = "map"

    def handleMapMenu(self, mousePosition):
        if self.screenController.mapSelectMenuScreen.backButton.collidepoint(mousePosition):
            self.screenController.mode = None
            self.screenController.selectedMap = None
            self.screenController.screenState = "mode"
            return

        for button, mapName in self.screenController.mapSelectMenuScreen.mapButtons:
            if button.collidepoint(mousePosition):
                self.screenController.selectMap(mapName)
                return

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = event.pos

                if self.screenController.screenState == "mode":
                    self.handleModeMenu(mousePosition)

                elif self.screenController.screenState == "map":
                    self.handleMapMenu(mousePosition)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.screenController.screenState == "map":
                        self.screenController.mode = None
                        self.screenController.selectedMap = None
                        self.screenController.screenState = "mode"
                    else:
                        return False

        return True