import pygame

TEXT_COLOR = (30, 30, 30)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (238, 241, 245)
GRID_COLOR = (190, 195, 205)
WALL_COLOR = (70, 75, 85)
FLOOR_COLOR = (245, 245, 240)
GOAL_COLOR = (220, 70, 70)
BOX_COLOR = (184, 132, 70)
BOX_GOAL_COLOR = (90, 170, 95)
BOX_AGENT1_COLOR = (55, 110, 210)
BOX_AGENT2_COLOR = (220, 130, 45)
AGENT1_COLOR = (55, 110, 210)
AGENT2_COLOR = (220, 130, 45)
SINGLE_BUTTON_COLOR = (100, 160, 230)
COMPETITIVE_BUTTON_COLOR = (225, 110, 120)
BACK_BUTTON_COLOR = (170, 175, 185)
ACTION_BUTTON_COLOR = (155, 200, 160)

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