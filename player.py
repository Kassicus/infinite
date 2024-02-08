import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(int(lib.SCREEN_WIDTH / 2), 100)
        self.vel = pygame.math.Vector2(0, 0)
        self.speed = 300

        self.gravity = 10
        self.jumping = False
        self.sprint = False

        self.width = 32
        self.height = 64

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        keys = pygame.key.get_pressed()

        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        if self.vel.y < 0:
            self.jumping = False

        if self.pos.y < lib.SCREEN_HEIGHT - 133:
            self.vel.y += self.gravity
        else:
            if not self.jumping:
                self.vel.y = 0
                self.pos.y = lib.SCREEN_HEIGHT - 132

        if keys[pygame.K_a]:
            self.vel.x = -self.speed
        elif keys[pygame.K_d]:
            self.vel.x = self.speed
        else:
            self.vel.x = 0

        if keys[pygame.K_LSHIFT]:
            self.sprint = True
        else:
            self.sprint = False

        if self.sprint:
            self.speed = 400
        else:
            self.speed = 300

    def jump(self):
        if self.pos.y > lib.SCREEN_HEIGHT - 140:
            self.jumping = True
            self.vel.y = -600