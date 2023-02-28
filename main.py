import pygame, sys
from settings import *
from level import Level

ARIAL_50 = font.SysFont('arial', 50)


class Menu:
    def __init__(self):
        pygame.init()
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('rogalick')

        self.menu = Menu


    def append_option(self,option,callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, RED))
        self._callbacks.append(callback)




    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))


    def select(self):
        self._callbacks[self._current_option_index]()


    def draw(self, surf, x , y, option_y_padding):

        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
                surf.blit(option, option_rect)
menu = Menu()
menu.append_option('Hello world', lambda: print('Hello world'))
menu.append_option('Quit', quit)

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('rogalick')
        self.clock = pygame.time.Clock()

        self.level = Level()

        self.running = True
        self.current_scene = None

    def swich_menu(self, libmenu):
        self.current_scene = libmenu

    def menu1(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    Game.swich_menu(None)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    Game.swich_menu(Game.menu2(self))
                    running = False

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def menu2(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.swich_menu(None)
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    Game.swich_menu(Game.menu1(self))
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        menu.switch(-1)
                    elif event.key == K_DOWN:
                        menu.switch(1)
                    elif event.key == K_RETURN:
                        menu.select()
            self.screen.fill('black')
            menu.draw(self.screen, 100, 100, 75)
            pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.menu2()