import pygame
from . import ui_config


def draw_button(screen, rect, font, text, color):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, ui_config.TEXT_COLOR, rect, 2)

    text_surface = font.render(text, True, ui_config.TEXT_COLOR)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
