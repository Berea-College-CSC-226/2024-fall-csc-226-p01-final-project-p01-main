import pygame
import random

class Game:
    def __init__(self):
        """
        Initialize the Space Shooter game.
        """
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()
        self.bg_color = "#000000"  # Black background

        # Load assets
        self.player_surf = pygame.Surface((50, 50))  # Placeholder player sprite
        self.player_surf.fill("#FFFFFF")  # White for player
        self.bullet_surf = pygame.Surface((10, 20))  # Placeholder bullet sprite
        self.bullet_surf.fill("#FFFFFF")  # White for bullets
        self.enemy_surf = pygame.Surface((50, 50))  # Placeholder enemy sprite
        self.enemy_surf.fill("#FF0000")  # Red for enemies

        # Initialize game objects
        self.player_rect = pygame.Rect(self.size[0] // 2, self.size[1] - 70, 50, 50)
        self.bullets = []  # Bullets fired by the player
        self.enemies = []  # Enemy ships
        self.spawn_timer = 0  # Timer to spawn enemies
        self.score = 0  # Player score
        self.health = 3  # Player health
        self.speed_multiplier = 1.0  # Speed multiplier for difficulty progression

    def display_message(self, message, color="white"):
        """
        Displays a message on the screen.

        :param message: The message to display
        :param color: The color of the text
        """
        font = pygame.font.SysFont("ComicSansMS", 48)
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)

    def spawn_enemy(self):
        """
        Spawns a new enemy at a random position at the top of the screen.
        """
        x = random.randint(0, self.size[0] - 50)
        self.enemies.append(pygame.Rect(x, -50, 50, 50))

    def move_bullets(self):
        """
        Moves bullets upward and removes bullets off-screen.
        """
        for bullet in self.bullets[:]:
            bullet.move_ip(0, -7 * self.speed_multiplier)
            if bullet.top <= 0:
                self.bullets.remove(bullet)

    def move_enemies(self):
        """
        Moves enemies downward and removes enemies off-screen.
        """
        for enemy in self.enemies[:]:
            enemy.move_ip(0, 3 * self.speed_multiplier)
            if enemy.top >= self.size[1]:
                self.enemies.remove(enemy)

    def detect_collisions(self):
        """
        Handles collisions between bullets, enemies, and the player.
        """
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.colliderect(enemy):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1
                    break

        for enemy in self.enemies[:]:
            if enemy.colliderect(self.player_rect):
                self.enemies.remove(enemy)
                self.health -= 1

    def render_hud(self):
        """
        Renders the player's score and health on the screen.
        """
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, "white")
        health_text = font.render(f"Health: {self.health}", True, "white")
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(health_text, (10, 50))

    def increase_difficulty(self):
        """
        Increases the game speed multiplier based on the score.
        """
        self.speed_multiplier = 1.0 + (self.score // 10) * 0.1

    def run(self):
        """
        Main game loop.
        """
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Fire a bullet
                        bullet = pygame.Rect(self.player_rect.centerx - 5, self.player_rect.top, 10, 20)
                        self.bullets.append(bullet)

            # Handle player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player_rect.left > 0:
                self.player_rect.move_ip(-5, 0)
            if keys[pygame.K_RIGHT] and self.player_rect.right < self.size[0]:
                self.player_rect.move_ip(5, 0)

            # Spawn enemies periodically
            self.spawn_timer += 1
            if self.spawn_timer > max(50 - self.score // 10, 20):  # Decrease spawn interval with score
                self.spawn_enemy()
                self.spawn_timer = 0

            # Update game objects
            self.move_bullets()
            self.move_enemies()
            self.detect_collisions()
            self.increase_difficulty()  # Adjust game speed

            # End game if health is zero
            if self.health <= 0:
                self.screen.fill(self.bg_color)
                self.display_message("Game Over", color="red")
                self.running = False

            # Redraw screen
            self.screen.fill(self.bg_color)
            self.screen.blit(self.player_surf, self.player_rect)
            for bullet in self.bullets:
                self.screen.blit(self.bullet_surf, bullet)
            for enemy in self.enemies:
                self.screen.blit(self.enemy_surf, enemy)
            self.render_hud()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

def main():
    """
    Starts the Space Shooter game.
    """
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
 