import pygame
from player import Player
from npc import NPC
from platform import Platform
from camera import Camera
from obstacle import Obstacle

class GameManager:
    def __init__(self):
        self.camera = Camera(1600, 1200)
        self.player = Player("GameImage/tacocat.png", 100, 400)
        self.npc = NPC("GameImage/fashiondemon.png", 700, 400)
        self.background = pygame.image.load("GameImage/background.png").convert()

        # Platforms
        self.platforms = [
            Platform(100, 500, 300, 20, "GameImage/platform_image.png"),
            Platform(500, 400, 200, 20, "GameImage/platform_image.png"),
            Platform(800, 300, 200, 20, "GameImage/platform_image.png"),
            Platform(1100, 200, 250, 20, "GameImage/platform_image.png"),
        ]

        # Obstacles
        self.obstacles = [
            Obstacle((300, 480), size=(30, 20), damage=10),
            Obstacle((600, 380), size=(20, 20), damage=15),
        ]

    def update(self):
        self.player.update(self.platforms, self.obstacles)
        self.npc.update(self.player)
        self.camera.update(self.player)

    def draw(self, screen):
        # Draw scrolling background
        for x in range(-1, 2):
            screen.blit(self.background, (x * self.background.get_width() + self.camera.camera.x % self.background.get_width(), 0))

        # Draw platforms
        for platform in self.platforms:
            platform.draw(screen, self.camera)

        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw(screen, self.camera)

        # Draw player and NPC
        self.player.draw(screen, self.camera)
        self.npc.draw(screen, self.camera)