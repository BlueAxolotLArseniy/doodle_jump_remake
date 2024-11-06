import pygame
import sys
from player import Player

pygame.init()

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

pygame.display.set_caption('DoOdLe JuMpE ReMaKe')

player = Player(400, 250)

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
    
    player.update()
    player.draw(screen)
    
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
sys.exit()