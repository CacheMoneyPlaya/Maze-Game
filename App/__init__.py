import pygame
import os
import sys
from Player import Player
from Room1 import Room1
from Room2 import Room2
from Room3 import Room3
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
    score = 0

    def __init__(self):
        self._running = True
        self.display = None
        self.finish_loop = True
        self.is_end_game = False
        self.game_is_complete = False
        self.player = Player()
        self.current_room_no = 0
        self.enemy_image = pygame.image.load("kim.jpg")
        self.enemy_image = pygame.transform.scale(self.enemy_image, (70, 70))
        self.player_image = pygame.image.load("trump.jpg")
        self.player_image = pygame.transform.scale(self.player_image, (50, 50))
        self.collectable_image = pygame.image.load("melania.jpg")
        self.collectable_image = pygame.transform.scale(self.collectable_image, (50, 50))
    def on_init(self):

        pygame.init()
        self.font = pygame.font.SysFont("monospace", 32)
        self.display = pygame.display.set_mode([self.windowHeight, self.windowWidth])
        self.player_sprite.add(self.player)
        room = Room1()
        self.rooms.append(room)
        room = Room2()
        self.rooms.append(room)
        room = Room3()
        self.rooms.append(room)
        self.current_room = self.rooms[self.current_room_no]
        pygame.display.set_caption('SAVE MELANIA')
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self.display.fill((226, 222, 227))
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
        self.display.fill((250, 0, 0))
        game_over = self.font.render("GAME OVER - Your score is: " + str(self.score), 1, (0, 0, 0))
        restart = self.font.render("Press Space Bar to restart", 1, (0, 0, 0))
        quit = self.font.render("Press Esc to quit", 1, (0, 0, 0))

        self.display.blit(game_over, (230, 225))
        self.display.blit(restart, (240, 255))
        self.display.blit(quit, (245, 285))
        pygame.display.update()
        self.is_end_game = True

    def on_cleanup(self):
        pygame.quit()

    def game_complete(self):
        self.display.fill((0, 255, 127))
        game_complete = self.font.render("YOU BEAT KIM JONG UN! - Your score is: " + str(self.score), 1, (0, 0, 0))
        restart = self.font.render("Press Space Bar to restart", 1, (0, 0, 0))
        quit = self.font.render("Press Esc to quit", 1, (0, 0, 0))

        self.display.blit(game_complete, (150, 225))
        self.display.blit(restart, (240, 255))
        self.display.blit(quit, (270, 285))
        pygame.display.update()
        self.game_is_complete = True
        self.is_end_game = True


    def on_execute(self):
        if self.on_init():
            self._running = False

        self.on_render()
        while self._running:

            pygame.event.pump()
            self.on_render()
            keys = pygame.key.get_pressed()
            pygame.display.update()
            if not self.is_end_game or self.game_is_complete:
                self.player_sprite.draw(self.display)
                self.player_sprite.update()
                self.current_room.wall_list.draw(self.display)
                self.current_room.entrance_list.draw(self.display)
                self.current_room.enemy_list.draw(self.display)
                self.current_room.collectable_list.draw(self.display)
                self.current_room.exit_list.draw(self.display)
                self.display.blit(self.player_image, self.player.rect)
                score_text = self.font.render("SCORE : " + str(self.score), 1, (0, 0, 0))
                self.display.blit(score_text, (25, 550))

                for enemy in self.current_room.enemy_list:
                    self.display.blit(self.enemy_image, enemy.rect)
                    if enemy.rect.y > 500:
                        enemy.rect.y = -3
                        if pygame.sprite.groupcollide(self.player_sprite,
                                                      self.current_room.enemy_list,
                                                      False,
                                                      False):
                            self.end_game()
                    if enemy.rect.y < 100:
                        self.increment = 3
                    enemy.rect.y += self.increment

                for collectable in self.current_room.collectable_list:
                    self.display.blit(self.collectable_image, collectable.rect)

                pygame.display.update()

                if pygame.sprite.groupcollide(self.player_sprite,
                                              self.current_room.collectable_list,
                                              False,
                                              True):
                    self.score += 100
                    print('Your score is: ', self.score)

                if pygame.sprite.groupcollide(self.player_sprite,
                                              self.current_room.enemy_list,
                                              False,
                                              False):
                    self.end_game()

                if pygame.sprite.groupcollide(self.player_sprite,
                                              self.current_room.exit_list,
                                              False,
                                              False):
                    self.game_complete()

                self.clock.tick(self.FPS)
                pygame.display.update()

                if keys[K_RIGHT]:
                    if pygame.sprite.groupcollide(self.player_sprite,
                                                  self.current_room.entrance_list,
                                                  False,
                                                  False):
                        self.current_room_no += 1
                        self.on_init()
                        self.player.reset_position(self.current_room_no)
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
            else:
                if keys[K_ESCAPE]:
                    self._running = False
                if keys[K_SPACE]:
                    os.execl(sys.executable, *([sys.executable] + sys.argv))
                if self.game_is_complete:
                    self.game_complete()
                else:
                    self.end_game()

        self.on_cleanup()
