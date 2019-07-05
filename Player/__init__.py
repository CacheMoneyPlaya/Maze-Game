import pygame


class Player(pygame.sprite.Sprite):

    GREEN = (0, 255, 0)

    WIDTH = 175
    HEIGHT = 100
    x = 100
    y = 100
    speed = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (self.WIDTH / 2, self.HEIGHT/2)

    def right(self, sprite1, sprite2, sprite3):
        if pygame.sprite.groupcollide(sprite1, sprite2, False, False) \
                or pygame.sprite.groupcollide(sprite1, sprite3, False, False):
            return True
        if pygame.sprite.groupcollide(sprite1, sprite2, False, False) \
                or pygame.sprite.groupcollide(sprite1, sprite3, False, False):
            return True
        else:
            self.rect.x += self.speed
            return False

    def left(self, sprite1, sprite2, sprite3):
        if pygame.sprite.groupcollide(sprite1, sprite2, False, False) \
                or pygame.sprite.groupcollide(sprite1, sprite3, False, False):
            return True
        else:
            self.rect.x += -self.speed
            return False

    def up(self, sprite1, sprite2, sprite3):
        if pygame.sprite.groupcollide(sprite1, sprite2, False, False) \
                or pygame.sprite.groupcollide(sprite1, sprite3, False, False):
            return True
        else:
            self.rect.y += -self.speed
            return False

    def down(self, sprite1, sprite2, sprite3):
        if pygame.sprite.groupcollide(sprite1, sprite2, False, False) \
                or pygame.sprite.groupcollide(sprite1, sprite3, False, False):
            return True
        else:
            self.rect.y += self.speed
            return False

    def reset_position(self, room_no):
        if room_no == 1:
            self.rect.x = 40
            self.rect.y = 300
        if room_no == 2:
            self.rect.x = 40
            self.rect.y = 300
        if room_no == 3:
            self.rect.x = 40
            self.rect.y = 40

