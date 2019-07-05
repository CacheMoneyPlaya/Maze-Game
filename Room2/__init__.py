import pygame
from Wall import Wall
from Maze import Maze
from Enemy import Enemy
from Collectable import Collectable
from Entrance import Entrance
from Complete import Complete

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 127)
RED = (244, 11, 11)


class Room2(Maze):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 780, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [20, 260, 150, 20, BLUE],
                 [20, 360, 150, 20, BLUE],
                 [200, 150, 150, 20, BLUE],
                 [200, 450, 150, 20, BLUE],
                 [350, 150, 20, 160, BLUE],
                 [350, 310, 20, 160, BLUE],
                 [450, 20, 20, 160, BLUE],
                 [450, 410, 20, 160, BLUE]]

        entrance = [[780, 250, 20, 100, YELLOW]]

        complete = []

        enemies = [[500, 190, 70, 70, WHITE],
                   [600, 390, 70, 70, WHITE],
                   [700, 590, 70, 70, WHITE]]

        collectables = [[375, 150, 50, 50, YELLOW],
                        [550, 380, 50, 50, YELLOW],
                        [400, 400, 50, 50, YELLOW]]

        for item in entrance:
            entrance = Wall(item[0], item[1], item[2], item[3], item[4])
            self.entrance_list.add(entrance)

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for item in enemies:
            enemy = Enemy(item[0], item[1], item[2], item[3], item[4])
            self.enemy_list.add(enemy)

        for item in collectables:
            collectable = Collectable(item[0], item[1], item[2], item[3], item[4])
            self.collectable_list.add(collectable)

        for item in complete:
            exit = Complete(item[0], item[1], item[2], item[3], item[4])
            self.exit_list.add(exit)


