from datetime import datetime
import pygame
import sys
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from jump_platform_spawner import JumpPlatformSpawner
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption('DoOdLe JuMpE ReMaKe')

player = Player(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, screen)

jump_platform_spawner = JumpPlatformSpawner(player, screen)

jump_platform_spawner.spawn_main_jump_platforms()

background = pygame.image.load('images/background.jpg').convert()
background_rect = (0, 0, 1920, 1080)

clock = pygame.time.Clock()

FPS = 1000
DRAW_FPS = 60

while_activity = True

last_draw_time = datetime.now()


while while_activity:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            while_activity = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                while_activity = False

    jump_platform_spawner.update()
    player.update(jump_platform_spawner.platforms)

    clock.tick(FPS)

    if (datetime.now() - last_draw_time).total_seconds() > (1.0 / DRAW_FPS):
        screen.blit(background, background_rect)
        jump_platform_spawner.draw()
        player.draw(screen)
        pygame.display.update()
        last_draw_time = datetime.now()


pygame.quit()
sys.exit()
