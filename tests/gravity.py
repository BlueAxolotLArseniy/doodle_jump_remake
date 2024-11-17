import pygame
import sys
import threading

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Example")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Параметры игрока
player_pos = pygame.Vector2(400, 300)
player_velocity_y = 0
player_jump_power = -1.0
gravity = 0.001
ground_y = HEIGHT - 50  # Уровень земли
player_on_ground = False

# Основной игровой цикл
clock = pygame.time.Clock()

screen.fill(WHITE)


def draw_game():
    rect = (player_pos.x, player_pos.y, 50, 50)
    prev_rect = rect
    while True:
        if prev_rect:
            pygame.draw.rect(screen, WHITE, prev_rect)
        rect = (player_pos.x, player_pos.y, 50, 50)
        pygame.draw.rect(screen, BLUE, rect)
        prev_rect = rect
        clock.tick(60)


# Creating threads for update and draw
draw_thread = threading.Thread(target=draw_game)
draw_thread.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка прыжка
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_on_ground:
                player_velocity_y = player_jump_power
                player_on_ground = False

    # Применение гравитации
    if not player_on_ground:
        player_velocity_y += gravity  # Увеличиваем скорость падения

    # Обновление позиции игрока
    player_pos.y += player_velocity_y

    # Проверка столкновения с землей
    if player_pos.y >= ground_y:
        player_pos.y = ground_y
        player_velocity_y = 0
        player_on_ground = True

    # Обновление экрана
    pygame.display.flip()
    clock.tick(10000)
