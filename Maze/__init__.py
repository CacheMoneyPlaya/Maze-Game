import pygame


class Maze(object):

    wall_list = None
    enemy_list = None
    entrance_list = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.entrance_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

