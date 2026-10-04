import pygame
from . import ui_config


class MapRenderer:
    def __init__(self, screen, tile_size):
        self.screen = screen
        self.tile_size = tile_size

    def cell_rect(self, x, y, offset_x, offset_y):
        return pygame.Rect(
            offset_x + x * self.tile_size,
            offset_y + y * self.tile_size,
            self.tile_size,
            self.tile_size
        )

    def draw(self, state, offset_x, offset_y):
        for y in range(state.height):
            for x in range(state.width):
                rect = self.cell_rect(x, y, offset_x, offset_y)

                if (x, y) in state.walls:
                    color = ui_config.WALL_COLOR
                else:
                    color = ui_config.FLOOR_COLOR

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, ui_config.GRID_COLOR, rect, 1)

        for goal in state.goals:
            x, y = goal
            rect = self.cell_rect(x, y, offset_x, offset_y)
            center = rect.center
            pygame.draw.circle(self.screen, ui_config.GOAL_COLOR, center, self.tile_size // 7)

        for box in state.boxes:
            x, y = box
            rect = self.cell_rect(x, y, offset_x, offset_y).inflate(-10, -10)

            if box in state.goals:
                color = ui_config.BOX_GOAL_COLOR
            else:
                color = ui_config.BOX_COLOR

            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, ui_config.TEXT_COLOR, rect, 2)

        if state.agent1 is not None:
            self.draw_agent(state.agent1, 1, offset_x, offset_y)

        if state.agent2 is not None:
            self.draw_agent(state.agent2, 2, offset_x, offset_y)

    def draw_agent(self, position, agent_id, offset_x, offset_y):
        x, y = position
        rect = self.cell_rect(x, y, offset_x, offset_y).inflate(-12, -12)

        if agent_id == 1:
            color = ui_config.AGENT1_COLOR
        else:
            color = ui_config.AGENT2_COLOR

        pygame.draw.circle(self.screen, color, rect.center, rect.width // 2)
