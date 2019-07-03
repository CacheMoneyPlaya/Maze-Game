import pygame
from Wall import Wall
from Maze import Maze
from Enemy import Enemy
# from Entrance import Entrance

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Room1(Maze):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 780, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [150, 20, 20, 400, BLUE],
                 [300, 180, 20, 400, BLUE],
                 [450, 20, 20, 400, BLUE],
                 [600, 180, 20, 400, BLUE],
                 ]
        entrance = [[780, 250, 20, 100, YELLOW]]

        enemies = []


        for item in entrance:
            entrance = Wall(item[0], item[1], item[2], item[3], item[4])
            self.entrance_list.add(entrance)

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for item in enemies:
            enemy = Enemy(item[0], item[1], item[2], item[3], item[4])
            self.enemy_list.add(enemy)

