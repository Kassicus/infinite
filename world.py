import pygame

import lib

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(0, int(lib.SCREEN_HEIGHT - 100))

        self.image = pygame.Surface([lib.SCREEN_WIDTH, 100])
        self.image.fill(lib.color.random_custom('g'))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        pass