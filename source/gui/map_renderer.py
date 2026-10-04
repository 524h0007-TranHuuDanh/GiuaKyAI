import pygame
from . import ui_config


class MapRenderer:
    def __init__(self, screen, tile_size):
        self.screen = screen
        self.tile_size = tile_size

        self.floor_image = pygame.image.load(ui_config.FLOOR_IMAGE).convert_alpha()
        self.wall_image = pygame.image.load(ui_config.WALL_IMAGE).convert_alpha()
        self.box_image = pygame.image.load(ui_config.BOX_IMAGE).convert_alpha()
        self.goal_image = pygame.image.load(ui_config.GOAL_IMAGE).convert_alpha()
        self.agent1_image = pygame.image.load(ui_config.AGENT1_IMAGE).convert_alpha()
        self.agent2_image = pygame.image.load(ui_config.AGENT2_IMAGE).convert_alpha()

        self.floor_image = pygame.transform.scale(self.floor_image, (tile_size, tile_size))
        self.wall_image = pygame.transform.scale(self.wall_image, (tile_size, tile_size))
        self.box_image = pygame.transform.scale(self.box_image, (tile_size, tile_size))
        self.goal_image = pygame.transform.scale(self.goal_image, (tile_size, tile_size))
        self.agent1_image = pygame.transform.scale(self.agent1_image, (tile_size, tile_size))
        self.agent2_image = pygame.transform.scale(self.agent2_image, (tile_size, tile_size))

    def draw_floor(self, x, y):
        pixel_x = x * self.tile_size
        pixel_y = y * self.tile_size
        self.screen.blit(self.floor_image, (pixel_x, pixel_y))

    def draw_wall(self, position):
        x, y = position
        pixel_x = x * self.tile_size
        pixel_y = y * self.tile_size
        self.screen.blit(self.wall_image, (pixel_x, pixel_y))

    def draw_goal(self, position):
        x, y = position
        pixel_x = x * self.tile_size
        pixel_y = y * self.tile_size
        self.screen.blit(self.goal_image, (pixel_x, pixel_y))

    def draw_box(self, position):
        x, y = position
        pixel_x = x * self.tile_size
        pixel_y = y * self.tile_size
        self.screen.blit(self.box_image, (pixel_x, pixel_y))

    def draw_agent(self, position, agent_id):
        x, y = position
        pixel_x = x * self.tile_size
        pixel_y = y * self.tile_size

        if agent_id == 1:
            image = self.agent1_image
        else:
            image = self.agent2_image

        self.screen.blit(image, (pixel_x, pixel_y))

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