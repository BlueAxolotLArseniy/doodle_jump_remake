import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.image = pygame.image.load('images/player_foto.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        
        self.BASESPEED = 20
        self.real_speed = 0
        self.movespeed = 10
        
        self.jump_pressed = False  # Флаг для отслеживания нажатия "W" или "UP"

    def update(self):
        keys = pygame.key.get_pressed()

        # Обработка движения влево и вправо
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.movespeed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.movespeed

        # Обработка прыжка (движение вверх) с блокировкой удерживания
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not self.jump_pressed:  # Если кнопка не удерживается
                self.real_speed = self.BASESPEED  # Прыжок
                self.jump_pressed = True  # Установить флаг, чтобы заблокировать удержание
        else:
            self.jump_pressed = False  # Сбросить флаг, когда кнопка отпущена

        # Обновление вертикального положения
        if self.real_speed > -self.BASESPEED:
            self.real_speed -= 1
        self.y -= self.real_speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))