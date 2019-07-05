import pygame
from Wall import Wall
from Maze import Maze
from Enemy import Enemy
from Collectable import Collectable
from Complete import Complete
from Entrance import Entrance

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 127)
RED = (244, 11, 11)


class Room3(Maze):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 780, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [20, 260, 150, 20, BLUE],
                 [20, 360, 150, 20, BLUE]]

        enemies = [[400, 190, 70, 70, WHITE],
                   [500, 390, 70, 70, WHITE],
                   [600, 590, 70, 70, WHITE],
                   [300, 290, 70, 70, WHITE],
                   [200, 690, 70, 70, WHITE]]

        entrance = []

        collectables = [[40, 40, 50, 50, YELLOW],
                        [30, 400, 50, 50, YELLOW],
                        [400, 400, 50, 50, YELLOW],
                        [400, 100, 50, 50, YELLOW]]

        complete = [[780, 250, 20, 100, GREEN]]

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

        for item in entrance:
            entrance = Wall(item[0], item[1], item[2], item[3], item[4])
            self.entrance_list.add(entrance)
