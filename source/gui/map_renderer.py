import pygame
from . import ui_config


class MapRenderer:
    def __init__(self, screen, tile_size):
        self.screen = screen
        self.tile_size = tile_size

    def draw_floor(self, x, y):
        pixel_x = x * self.tile_size
        pixel_y = y * self.tile_size

        rect = pygame.Rect(pixel_x, pixel_y, self.tile_size, self.tile_size)

        pygame.draw.rect(self.screen, ui_config.FLOOR_COLOR, rect)
        pygame.draw.rect(self.screen, ui_config.GRID_COLOR, rect, 1)

    def draw_wall(self, position):
        x, y = position

        pixel_x = x * self.tile_size
        pixel_y = y * self.tile_size

        rect = pygame.Rect(pixel_x, pixel_y, self.tile_size, self.tile_size)

        pygame.draw.rect(self.screen, ui_config.WALL_COLOR, rect)

    def draw_goal(self, position):
        x, y = position

        center_x = x * self.tile_size + self.tile_size // 2
        center_y = y * self.tile_size + self.tile_size // 2

        pygame.draw.circle(self.screen, ui_config.GOAL_COLOR, (center_x, center_y), 10)

    def draw_box(self, position):
        x, y = position

        pixel_x = x * self.tile_size + 5
        pixel_y = y * self.tile_size + 5

        box_size = self.tile_size - 10
        rect = pygame.Rect(pixel_x, pixel_y, box_size, box_size)

        pygame.draw.rect(self.screen, ui_config.BOX_COLOR, rect)

    def draw_agent(self, position, agent_id):
        x, y = position

        center_x = x * self.tile_size + self.tile_size // 2
        center_y = y * self.tile_size + self.tile_size // 2

        if agent_id == 1:
            color = ui_config.AGENT1_COLOR
        else:
            color = ui_config.AGENT2_COLOR

        pygame.draw.circle(self.screen, color, (center_x, center_y), 18)

    def draw(self, walls, state, rows, columns):
        for y in range(rows):
            for x in range(columns):
                self.draw_floor(x, y)

        for wall in walls:
            self.draw_wall(wall)

        for goal in state.goals:
            self.draw_goal(goal)

        for box in state.boxes:
            self.draw_box(box)

        if state.agent1 is not None:
            self.draw_agent(state.agent1, 1)

        if state.agent2 is not None:
            self.draw_agent(state.agent2, 2)