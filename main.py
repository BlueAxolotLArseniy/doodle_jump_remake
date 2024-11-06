import pygame
import sys
from player import Player
from jump_platform import JumpPlatform

pygame.init()

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

pygame.display.set_caption('DoOdLe JuMpE ReMaKe')

player = Player(400, 250, screen)
jump_platform = JumpPlatform(700, 250, player)

all_objects = [jump_platform]

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
                
    screen.fill((140, 27, 168))
    
    player.update(all_objects)
    player.draw(screen)

    jump_platform.update()
    jump_platform.draw(screen)
    
    clock.tick(FPS)
    pygame.display.update()

    print(player.rect)

pygame.quit()
sys.exit()