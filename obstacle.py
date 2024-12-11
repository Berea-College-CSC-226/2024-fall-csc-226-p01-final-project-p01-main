import pygame

class Obstacle:
    def __init__(self, position, size, damage):
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.damage = damage  # The damage this obstacle deals when collided with

    def collide(self, player):
        """
        Check if there is a collision with the player.
        """
        return self.rect.colliderect(player.rect)

    def draw(self, screen, camera):
        """
        Draw the obstacle on the screen, adjusted by the camera.
        """
        pygame.draw.rect(screen, (255, 0, 0), camera.apply(self.rect))  # Draw in red for visibility