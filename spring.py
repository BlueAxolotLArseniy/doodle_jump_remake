
import random
import pygame
from jump_platform import JumpPlatform
from player import Player


class SpringPlatform(JumpPlatform):
    def __init__(self, x, y, player: Player):
        super().__init__(x, y, player)
        self.spring_image = pygame.image.load("images/spring.png")
        rand_x = random.randint(x+3, x+67)
        self.spring_image_rect = self.spring_image.get_rect(center=(rand_x, y-20))
        self.jump_force = 1.47

    def update(self):
        #this code, works is too strange. We don`t know but it work :)
        player_rect = pygame.Rect(self.player.rect.centerx, self.player.rect.centery,
                                  self.player.rect.width, self.player.rect.height)
        if player_rect.colliderect(self.rect) and self.player.real_speed < 0:
            pygame.mixer.Sound("sounds/spring_jump.mp3").play()
            self.player.jump(self.jump_force)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.spring_image, self.spring_image_rect.center)

    def move_y(self, diff):
        super().move_y(diff)
        self.spring_image_rect.centery += diff
