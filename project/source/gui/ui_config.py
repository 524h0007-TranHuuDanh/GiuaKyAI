import pygame

TEXT_COLOR = (35, 35, 45)
WHITE = (255, 255, 255)

BACKGROUND_COLOR = (245, 242, 248)
GRID_COLOR = (200, 195, 205)

WALL_COLOR = (85, 75, 95)
FLOOR_COLOR = (250, 248, 242)

GOAL_COLOR = (210, 75, 105)

BOX_COLOR = (205, 165, 85)
BOX_GOAL_COLOR = (105, 175, 115)

BOX_AGENT1_COLOR = (135, 85, 190)
BOX_AGENT2_COLOR = (45, 165, 150)

AGENT1_COLOR = (135, 85, 190)
AGENT2_COLOR = (45, 165, 150)

SINGLE_BUTTON_COLOR = (130, 165, 215)
COMPETITIVE_BUTTON_COLOR = (205, 135, 165)

BACK_BUTTON_COLOR = (175, 165, 185)
ACTION_BUTTON_COLOR = (125, 185, 175)

TITLE_FONT_SIZE = 42
BUTTON_FONT_SIZE = 28

TILE_SIZE = 48
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650


def draw_button(screen, rect, font, text, color):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, TEXT_COLOR, rect, 2)

    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, text_surface.get_rect(center=rect.center))