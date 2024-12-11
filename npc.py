import pygame

class NPC:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.speed = 2

    def update(self, player):
        # Simple AI to follow the player horizontally
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        # Add vertical following if needed:
        # if self.rect.y < player.rect.y:
        #     self.rect.y += self.speed
        # elif self.rect.y > player.rect.y:
        #     self.rect.y -= self.speed

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))