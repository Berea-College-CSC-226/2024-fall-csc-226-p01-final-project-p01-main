import pygame

class Platform:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path).convert_alpha() if image_path else None

    def draw(self, screen, camera):
        """
        Draws the platform using the given camera to adjust the position.
        """
        if self.image:
            # If an image is specified, use it for the platform
            screen.blit(self.image, camera.apply(self.rect))
        else:
            # Otherwise draw a basic colored rectangle
            pygame.draw.rect(screen, (100, 100, 100), camera.apply(self.rect))  # Default color grey