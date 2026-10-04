import pygame
from . import uiConfig


class MapRenderer:
    def __init__(self, screen, tileSize):
        self.screen = screen
        self.tileSize = tileSize

    def drawFloor(self, x, y):
        pixelX = x * self.tileSize
        pixelY = y * self.tileSize

        rect = pygame.Rect(pixelX, pixelY, self.tileSize, self.tileSize)

        pygame.draw.rect(self.screen, uiConfig.FLOOR_COLOR, rect)
        pygame.draw.rect(self.screen, uiConfig.GRID_COLOR, rect, 1)

    def drawWall(self, position):
        x, y = position

        pixelX = x * self.tileSize
        pixelY = y * self.tileSize

        rect = pygame.Rect(pixelX, pixelY, self.tileSize, self.tileSize)

        pygame.draw.rect(self.screen, uiConfig.WALL_COLOR, rect)

    def drawGoal(self, position):
        x, y = position

        centerX = x * self.tileSize + self.tileSize // 2
        centerY = y * self.tileSize + self.tileSize // 2

        pygame.draw.circle(self.screen, uiConfig.GOAL_COLOR, (centerX, centerY), 10)

    def drawBox(self, position):
        x, y = position

        pixelX = x * self.tileSize + 5
        pixelY = y * self.tileSize + 5

        boxSize = self.tileSize - 10
        rect = pygame.Rect(pixelX, pixelY, boxSize, boxSize)

        pygame.draw.rect(self.screen, uiConfig.BOX_COLOR, rect)

    def drawAgent(self, position, agentId):
        x, y = position

        centerX = x * self.tileSize + self.tileSize // 2
        centerY = y * self.tileSize + self.tileSize // 2

        if agentId == 1:
            color = uiConfig.AGENT1_COLOR
        else:
            color = uiConfig.AGENT2_COLOR

        pygame.draw.circle(self.screen, color, (centerX, centerY), 18)

    def draw(self, walls, state, rows, columns):
        for y in range(rows):
            for x in range(columns):
                self.drawFloor(x, y)

        for wall in walls:
            self.drawWall(wall)

        for goal in state.goals:
            self.drawGoal(goal)

        for box in state.boxes:
            self.drawBox(box)

        if state.agent1 is not None:
            self.drawAgent(state.agent1, 1)

        if state.agent2 is not None:
            self.drawAgent(state.agent2, 2)