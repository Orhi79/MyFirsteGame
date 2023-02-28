import pygame
from settings import WHITE, BLACK
pygame.init()
font = pygame.font.Font(None, 30)

def dabug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    dabug_surf = font.render(str(info), True, WHITE)
    dabug_rect = dabug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, BLACK, dabug_rect)
    display_surface.blit(dabug_surf, dabug_rect)