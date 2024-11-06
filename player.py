import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen: pygame.Surface):
        self.image = pygame.image.load('images/player.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))

        self.BASE_SPEED = 20
        self.real_speed = 0
        self.move_speed = 10

        self.jump_pressed = False  # Флаг для отслеживания нажатия "W" или "UP"

        self.screen = screen

    def jump(self):
        if not self.jump_pressed:  # Если кнопка не удерживается
            self.real_speed = self.BASE_SPEED  # Прыжок
            self.jump_pressed = True  # Установить флаг, чтобы заблокировать удержание

    def update(self):
        keys = pygame.key.get_pressed()

        # Обработка движения влево и вправо
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.centerx -= self.move_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.centerx += self.move_speed

        # Обработка прыжка (движение вверх) с блокировкой удерживания
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not self.jump_pressed:  # Если кнопка не удерживается
                self.real_speed = self.BASE_SPEED  # Прыжок
                self.jump_pressed = True  # Установить флаг, чтобы заблокировать удержание
        else:
            self.jump_pressed = False  # Сбросить флаг, когда кнопка отпущена

        # Обновление вертикального положения
        if self.real_speed > -self.BASE_SPEED:
            self.real_speed -= 1
        self.rect.centery -= self.real_speed

        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
        
        if self.rect.centerx < 0:
            self.rect.centerx = self.screen.get_width()

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)
