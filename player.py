import pygame
from consts import IS_DEBUG, PLAYER_BASE_SPEED, PLAYER_FALL_SPEED, PLAYER_MOVE_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen: pygame.Surface):
        self.original_image = pygame.image.load('images/player.png').convert()
        self.original_image.set_colorkey((255, 255, 255))
        self.flipped_image = pygame.transform.flip(self.original_image, True, False)
        self.image = self.original_image

        self.rect = self.original_image.get_rect()

        self.speed = 0

        self.jump_pressed = False  # Флаг для отслеживания нажатия "W" или "UP"

        self.screen = screen

    def jump(self, jump_force: float):
        if not self.jump_pressed:  # Если кнопка не удерживается
            self.speed = PLAYER_BASE_SPEED * jump_force  # Прыжок
            self.jump_pressed = True  # Установить флаг, чтобы заблокировать удержание

    def update(self, all_objects: list):
        keys = pygame.key.get_pressed()

        # Обработка движения влево и вправо
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.centerx -= PLAYER_MOVE_SPEED
            self.image = self.flipped_image
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.centerx += PLAYER_MOVE_SPEED
            self.image = self.original_image

        # Обработка прыжка (движение вверх) с блокировкой удерживания
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not self.jump_pressed:
                self.speed = PLAYER_BASE_SPEED
                self.jump_pressed = True
        else:
            self.jump_pressed = False

        # Обновление вертикального положения
        if self.speed > -PLAYER_BASE_SPEED:
            self.speed -= PLAYER_FALL_SPEED
        self.rect.centery -= self.speed

        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0

        if self.rect.centerx < 0:
            self.rect.centerx = self.screen.get_width()

        target_y = self.screen.get_height() // 3
        if self.rect.centery < target_y:
            self.rect.centery = target_y
            for obj in all_objects:
                if self.speed > 0:
                    obj.move_y(self.speed)
                    self.rect.centery += target_y - self.rect.centery

        # print(self.real_speed)

    def draw(self, screen):
        if IS_DEBUG:
            pygame.draw.rect(screen, (180, 198, 250), self.rect)
        screen.blit(self.image, self.rect.topleft)
