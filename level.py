import pygame
from settings import *
from tile import Tile
from player import Player
from dabug import dabug


class Level:
    # настройка группы спрайтов
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # настройка спрайтов
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites, ])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        # улудшение и прокачивание игры
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        dabug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2(100,200)

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)