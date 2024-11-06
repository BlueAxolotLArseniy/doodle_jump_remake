import random

import pygame
from jump_platform import JumpPlatform
from player import Player


class JumpPlatformSpawner:
    def __init__(self, player: Player, screen: pygame.Surface):
        self.player = player
        self.screen = screen
        self.platforms: list[JumpPlatform] = []

    def new_platform(self):
        pass

    def spawn_main_jump_platforms(self):
        for y in range(50, -2050, -200):
            platform = JumpPlatform(
                x=random.randint(20, self.screen.get_width()-20),
                y=y,
                player=self.player
            )
            self.platforms.append(platform)
    
    def update(self):
        for platform in self.platforms:
            platform.update()
            
    def draw(self):
        for platform in self.platforms:
            platform.draw(self.screen)