import pygame
from consts import IS_DEBUG, PLATFORM_JUMP_FORCE
from player import Player


class JumpPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, player: Player):
        self.player = player

        self.image = pygame.image.load('images/jump_platform.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if self.player.rect.colliderect(self.rect) and self.player.speed < 0:
            pygame.mixer.Sound("sounds/jump.mp3").play()
            self.player.jump(PLATFORM_JUMP_FORCE)

    def draw(self, screen):
        if IS_DEBUG:
            pygame.draw.rect(screen, (222, 138, 255), self.rect)
        screen.blit(self.image, self.rect.center)

    def move_y(self, diff):
        self.rect.centery += diff
