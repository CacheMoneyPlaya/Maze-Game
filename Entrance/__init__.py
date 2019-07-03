import pygame


class Entrance(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
