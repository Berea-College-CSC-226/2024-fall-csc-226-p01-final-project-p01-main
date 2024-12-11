import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, rect):
        """
        Applies the camera's position to the given rectangle.
        This method is used to adjust positions of entities for rendering.
        """
        return rect.move(-self.camera.x, -self.camera.y)

    def update(self, target):
        """
        Updates the camera's position to keep the target in the center of the screen.
        """
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Limit the camera movement to the game world boundaries
        x = max(-(self.width - 800), min(0, x))  # Ensures camera does not go past the game world's right edge
        y = max(-(self.height - 600), min(0, y))  # Ensures camera does not go past the game world's bottom edge

        self.camera = pygame.Rect(x, y, self.width, self.height)