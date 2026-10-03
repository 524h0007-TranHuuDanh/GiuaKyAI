import pygame


class MapRenderer:
    def __init__(self, screen, tileSize):
        self.screen = screen
        self.tileSize = tileSize

        self.floorColor = (240, 240, 240)
        self.gridColor = (200, 200, 200)
        self.wallColor = (80, 80, 80)

        self.goalColor = (220, 70, 70)
        self.boxColor = (180, 120, 60)

        self.agent1Color = (70, 120, 220)
        self.agent2Color = (70, 180, 100)

    def drawFloor(self, x, y):
        pixelX = x * self.tileSize
        pixelY = y * self.tileSize

        rect = pygame.Rect(pixelX, pixelY, self.tileSize, self.tileSize)

        pygame.draw.rect(self.screen, self.floorColor, rect)
        pygame.draw.rect(self.screen, self.gridColor, rect, 1)

    def drawWall(self, position):
        x, y = position

        pixelX = x * self.tileSize
        pixelY = y * self.tileSize

        rect = pygame.Rect(pixelX, pixelY, self.tileSize, self.tileSize)

        pygame.draw.rect(self.screen, self.wallColor, rect)

    def drawGoal(self, position):
        x, y = position

        centerX = x * self.tileSize + self.tileSize // 2
        centerY = y * self.tileSize + self.tileSize // 2

        pygame.draw.circle(self.screen, self.goalColor, (centerX, centerY), 10)

    def drawBox(self, box):
        x, y = box.position

        pixelX = x * self.tileSize + 5
        pixelY = y * self.tileSize + 5

        boxSize = self.tileSize - 10

        rect = pygame.Rect(pixelX, pixelY, boxSize, boxSize)

        pygame.draw.rect(self.screen, self.boxColor, rect)

    def drawAgent(self, agent):
        x, y = agent.position

        centerX = x * self.tileSize + self.tileSize // 2
        centerY = y * self.tileSize + self.tileSize // 2

        if agent.agentId == 1:
            color = self.agent1Color
        else:
            color = self.agent2Color

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

        for agent in state.agents:
            self.drawAgent(agent)