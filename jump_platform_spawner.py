import random

import pygame
from jump_platform import JumpPlatform
from player import Player
from spring import SpringPlatform


class JumpPlatformSpawner:
    def __init__(self, player: Player, screen: pygame.Surface):
        self.player = player
        self.screen = screen
        self.platforms: list[JumpPlatform] = []

    def spawn_main_jump_platforms(self):
        for y in range(50, -700, -150):
            platform = JumpPlatform(
                x=random.randint(20, self.screen.get_width()-70),
                y=y,
                player=self.player
            )
            self.platforms.append(platform)

    def update(self):
        for platform in self.platforms:
            platform.update()
        if self.platforms[0].rect.centery >= self.screen.get_height()+50:
            self.platforms.pop(0)
        if self.platforms[-1].rect.centery > -550:
            self.spawn_platform()

    def spawn_platform(self):
        rand_x = random.randint(20, self.screen.get_width()-20)
        y = -700
        if random.randint(1, 7) == 1:
            self.platforms.append(SpringPlatform(x=rand_x, y=y, player=self.player))
        else:
            self.platforms.append(JumpPlatform(x=rand_x, y=y, player=self.player))

    def draw(self):
        for platform in self.platforms:
            platform.draw(self.screen)
