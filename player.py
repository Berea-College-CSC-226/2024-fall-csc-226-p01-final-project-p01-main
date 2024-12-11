import pygame

class Player:
    def __init__(self, image_path, x, y, scale=(50, 100)):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jump_strength = 10
        self.on_ground = False

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.move(self.speed, 0)
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def move(self, dx, dy):
        """Move each axis separately. Note that this doesn't include collision handling."""
        self.rect.x += dx
        self.rect.y += dy

        # Simulate ground check
        if self.rect.bottom >= 600:  # Assuming 600 is the ground level
            self.rect.bottom = 600
            self.velocity.y = 0
            self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.velocity.y = -self.jump_strength
            self.on_ground = False

    def update(self, platforms):
        # Apply gravity
        self.velocity.y += 1  # Gravity effect
        if self.velocity.y > 10:
            self.velocity.y = 10

        # Update position based on velocity
        self.rect.y += self.velocity.y
        self.handle_keys()

        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.on_ground = True

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))