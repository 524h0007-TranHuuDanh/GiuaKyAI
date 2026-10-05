import pygame
from . import ui_config


class MapRenderer:
    def __init__(self, screen, tile_size):
        self.screen = screen
        self.tile_size = tile_size

    def cell_rect(self, x, y, offset_x, offset_y):
        return pygame.Rect(offset_x + x * self.tile_size, offset_y + y * self.tile_size, self.tile_size, self.tile_size)

    def draw(self, state, offset_x, offset_y):
        for y in range(state.height):
            for x in range(state.width):
                rect = self.cell_rect(x, y, offset_x, offset_y)
                color = ui_config.WALL_COLOR if (x, y) in state.walls else ui_config.FLOOR_COLOR
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, ui_config.GRID_COLOR, rect, 1)

        for x, y in state.goals:
            rect = self.cell_rect(x, y, offset_x, offset_y)
            pygame.draw.circle(self.screen, ui_config.GOAL_COLOR, rect.center, 5)

        for box in state.boxes:
            rect = self.cell_rect(box[0], box[1], offset_x, offset_y).inflate(-8, -8)
            owner = state.get_box_owner(box) if hasattr(state, "get_box_owner") else None

            if box in state.goals:
                color = ui_config.BOX_GOAL_COLOR
            elif owner == 1:
                color = ui_config.BOX_AGENT1_COLOR
            elif owner == 2:
                color = ui_config.BOX_AGENT2_COLOR
            else:
                color = ui_config.BOX_COLOR

            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, ui_config.TEXT_COLOR, rect, 2)

        if state.agent1:
            self.draw_agent(state.agent1, ui_config.AGENT1_COLOR, offset_x, offset_y)
        if state.agent2:
            self.draw_agent(state.agent2, ui_config.AGENT2_COLOR, offset_x, offset_y)

    def draw_agent(self, position, color, offset_x, offset_y):
        rect = self.cell_rect(position[0], position[1], offset_x, offset_y)
        pygame.draw.circle(self.screen, color, rect.center, self.tile_size // 3)