import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('player_foto.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*0.2, self.image.get_height()*0.2))
        self.rect = self.image.get_rect(center=(x, y))
        self.BASESPEED = 5
        self.real_speed = 0
        self.movespeed = 10
    def update(self):
        keys = pygame.key.get_pressed()
        if self.real_speed > -self.BASESPEED: self.real_speed -= 1
        if keys[pygame.K_a]: self.x -= self.movespeed
        if keys[pygame.K_d]: self.x += self.movespeed
        if keys[pygame.K_w]:
            self.real_speed = self.BASESPEED
        self.y -= self.real_speed
    def draw(self, sc):
        sc.blit(self.image, (self.x, self.y))