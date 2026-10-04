import pygame
from . import ui_config


def draw_pixel_button(screen, rect, font, text, color):
    pygame.draw.rect(screen, ui_config.BUTTON_BORDER_COLOR, rect)

    inner_rect = rect.inflate(-8, -8)
    pygame.draw.rect(screen, color, inner_rect)

    text_surface = font.render(text, True, ui_config.TEXT_COLOR)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)