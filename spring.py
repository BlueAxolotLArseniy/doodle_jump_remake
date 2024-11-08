
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
        self.jump_force = 1.3

    def update(self):
        if self.player.rect.colliderect(self.rect) and self.player.real_speed <= -20:
            pygame.mixer.Sound("sounds/spring_jump.mp3").play()
            self.player.jump(self.jump_force)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.spring_image, self.spring_image_rect.center)

    def move_y(self, diff):
        super().move_y(diff)
        self.spring_image_rect.centery += diff
