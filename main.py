import random
import pygame
import sys
from jump_platform_spawner import JumpPlatformSpawner
from player import Player
from jump_platform import JumpPlatform

pygame.init()

screen = pygame.display.set_mode((600, 900), pygame.RESIZABLE)

pygame.display.set_caption('DoOdLe JuMpE ReMaKe')

player = Player(400, 250, screen)

jump_platform_spawner = JumpPlatformSpawner(player, screen)

jump_platform_spawner.spawn_main_jump_platforms()

background = pygame.image.load('images/background.jpg').convert()
background_rect = (0, 0, 1920, 1080)

clock = pygame.time.Clock()
FPS = 60

while_activity = True

while while_activity:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            while_activity = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                while_activity = False

    screen.blit(background, background_rect)

    jump_platform_spawner.update()
    player.update(jump_platform_spawner.platforms)

    jump_platform_spawner.draw()
    player.draw(screen)

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
sys.exit()
