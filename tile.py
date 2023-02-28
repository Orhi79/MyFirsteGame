import pygame
from settings import *
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/Пользователь/Desktop/gate/graphics/rock.png')
        self.rect= self.image.get_rect(topleft = pos)
        #создание хитбокса
        self.hitbox = self.rect.inflate(0, -10)