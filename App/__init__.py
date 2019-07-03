import pygame
from Player import Player
from Room1 import Room1
from Room2 import Room2
from pygame.locals import *
from time import sleep
class App:
    windowWidth = 600
    windowHeight = 800
    player = 0
    player_sprite = pygame.sprite.Group()
    FPS = 30
    clock = pygame.time.Clock()
    rooms = []
    current_room = None
    increment = 3

    def __init__(self):
        self._running = True
        self.display = None
        self.finish_loop = True
        self.player = Player()
        self.current_room_no = 0
        self.enemy_image = pygame.image.load("kim.jpg")
        self.enemy_image = pygame.transform.scale(self.enemy_image, (70, 70))
        self.player_image = pygame.image.load("trump.jpg")
        self.player_image = pygame.transform.scale(self.player_image, (50, 50))

    def on_init(self):

        pygame.init()
        self.display = pygame.display.set_mode([self.windowHeight, self.windowWidth])
        self.player_sprite.add(self.player)
        room = Room1()
        self.rooms.append(room)
        room = Room2()
        self.rooms.append(room)
        self.current_room = self.rooms[self.current_room_no]
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self.display.fill((105, 105, 105))
        pygame.display.flip()

    def end_game(self):
        # for x in range(1, 10):
        #     if(x % 2) == 0:
        #         self.display.fill((125, 0, 0))
        #         pygame.display.update()
        #         sleep(0.3)
        #     else:
        #         self.display.fill((255, 255, 0))
        #         pygame.display.update()
        #         sleep(0.3)
        self.display.fill((255, 255, 0))
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init():
            self._running = False

        self.on_render()
        while self._running:

            pygame.event.pump()
            self.on_render()
            keys = pygame.key.get_pressed()
            pygame.display.update()
            self.player_sprite.draw(self.display)
            self.player_sprite.update()
            self.current_room.wall_list.draw(self.display)
            self.current_room.entrance_list.draw(self.display)
            self.current_room.enemy_list.draw(self.display)

            self.display.blit(self.player_image, self.player.rect)

            for enemy in self.current_room.enemy_list:
                self.display.blit(self.enemy_image, enemy.rect)
               ## logic for moving enemies about
                if enemy.rect.y > 500:
                    enemy.rect.y = -3
                if enemy.rect.y < 100:
                    self.increment = 3
                enemy.rect.y += self.increment
            pygame.display.update()

            self.clock.tick(self.FPS)
            pygame.display.update()

            if keys[K_RIGHT]:
                if pygame.sprite.groupcollide(self.player_sprite,
                                              self.current_room.entrance_list,
                                              False,
                                              False):
                    self.current_room_no += 1
                    self.on_init()
                    self.player.reset_position()
                if self.player.right(self.player_sprite,
                                     self.current_room.wall_list,
                                     self.current_room.enemy_list):
                    self.end_game()

            if keys[K_LEFT]:
                if self.player.left(self.player_sprite,
                                    self.current_room.wall_list,
                                    self.current_room.enemy_list):
                    self.end_game()

            if keys[K_UP]:
                if self.player.up(self.player_sprite,
                                  self.current_room.wall_list,
                                  self.current_room.enemy_list):
                    self.end_game()

            if keys[K_DOWN]:
                if self.player.down(self.player_sprite,
                                    self.current_room.wall_list,
                                    self.current_room.enemy_list):
                    self.end_game()

            if keys[K_ESCAPE]:
                self._running = False

        self.on_cleanup()
