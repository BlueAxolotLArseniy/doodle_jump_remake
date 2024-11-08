import pygame
from player import Player


class JumpPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, player: Player):
        self.player = player

        self.image = pygame.image.load('images/jump_platform.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if self.player.rect.colliderect(self.rect) and self.player.real_speed <= -20:
            pygame.mixer.Sound("sounds/jump.mp3").play()
            self.player.jump()

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

    def move_y(self, diff):
        self.rect.centery += diff
