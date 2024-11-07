
import pygame
from jump_platform import JumpPlatform
from player import Player


class SpringPlatform(JumpPlatform):
    def __init__(self, x, y, player: Player):
        self.spring_image = pygame.image.load("images/spring.png")
        self.spring_image_rect = self.spring_image.get_rect(center=(x, y-20))
        self.jump_force = 2.0
        super().__init__(x, y, player)

    def update(self):
        if self.player.rect.colliderect(self.rect) and self.player.real_speed <= -20:
            self.player.jump(self.jump_force)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.spring_image, self.spring_image_rect.center)

    def move_y(self, diff):
        super().move_y(diff)
        self.spring_image_rect.centery += diff
