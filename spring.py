
import random
import pygame
from consts import IS_DEBUG, SPRING_JUMP_FORCE
from jump_platform import JumpPlatform
from player import Player


class SpringPlatform(JumpPlatform):
    def __init__(self, x, y, player: Player):
        super().__init__(x, y, player)
        self.spring_image = pygame.image.load("images/spring.png")
        rand_x = random.randint(x, x+self.rect.width)
        self.spring_image_rect = self.spring_image.get_rect(topleft=(rand_x, y-self.spring_image.get_rect().height))

    def update(self):
        if self.player.rect.colliderect(self.rect) and self.player.speed < 0:
            pygame.mixer.Sound("sounds/spring_jump.mp3").play()
            self.player.jump(SPRING_JUMP_FORCE)

    def draw(self, screen):
        super().draw(screen)
        if IS_DEBUG:
            pygame.draw.rect(screen, (176, 255, 251), self.spring_image_rect)
        screen.blit(self.spring_image, self.spring_image_rect.topleft)

    def move_y(self, diff):
        super().move_y(diff)
        self.spring_image_rect.y += diff
