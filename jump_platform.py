import pygame

class JumpPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.image = pygame.image.load('images/jump_platform.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))