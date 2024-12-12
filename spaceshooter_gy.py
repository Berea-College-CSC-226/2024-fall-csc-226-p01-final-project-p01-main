import pygame
import random
import time

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
        self.boss_surf = pygame.Surface((150, 100))  # Placeholder boss sprite
        self.boss_surf.fill("#0000FF")  # Blue for boss

        # Initialize game objects
        self.player_rect = pygame.Rect(self.size[0] // 2, self.size[1] - 70, 50, 50)
        self.bullets = []  # Bullets fired by the player
        self.enemies = []  # Enemy ships
        self.boss = None  # Current boss
        self.boss_health = 0  # Boss health
        self.boss_direction = 1  # Boss movement direction (1 = right, -1 = left)
        self.spawn_timer = 0  # Timer to spawn enemies
        self.score = 0  # Player score
        self.health = 3  # Player health
        self.speed_multiplier = 1.0  # Speed multiplier for difficulty progression
        self.time_limit = 120  # Time limit in seconds (2 minutes)
        self.start_time = time.time()
        self.score_goal = 50  # Points required to win the game

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

    def spawn_boss(self):
        """
        Spawns a boss at the top of the screen.
        """
        self.boss = pygame.Rect(self.size[0] // 2 - 75, 50, 150, 100)
        self.boss_health = 10  # Boss requires 10 hits to be defeated

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

    def move_boss(self):
        """
        Moves the boss left and right at the top of the screen.
        """
        if self.boss:
            self.boss.move_ip(5 * self.boss_direction, 0)
            # Reverse direction if the boss hits screen edges
            if self.boss.left <= 0 or self.boss.right >= self.size[0]:
                self.boss_direction *= -1

    def detect_collisions(self):
        """
        Handles collisions between bullets, enemies, the boss, and the player.
        """
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.colliderect(enemy):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1
                    break

            if self.boss and bullet.colliderect(self.boss):
                self.bullets.remove(bullet)
                self.boss_health -= 1
                if self.boss_health <= 0:
                    self.score += 20  # Boss gives a large score boost
                    self.boss = None  # Remove the boss

        for enemy in self.enemies[:]:
            if enemy.colliderect(self.player_rect):
                self.enemies.remove(enemy)
                self.health -= 1

        if self.boss and self.boss.colliderect(self.player_rect):
            self.health -= 1
            self.boss = None  # Remove the boss on collision

    def render_hud(self):
        """
        Renders the player's score, health, boss health, and remaining time on the screen.
        """
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, "white")
        health_text = font.render(f"Health: {self.health}", True, "white")
        time_remaining = max(0, self.time_limit - int(time.time() - self.start_time))
        timer_text = font.render(f"Time Left: {time_remaining}s", True, "white")
        goal_text = font.render(f"Goal: {self.score}/{self.score_goal}", True, "white")
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(health_text, (10, 50))
        self.screen.blit(timer_text, (10, 90))
        self.screen.blit(goal_text, (10, 130))
        if self.boss:
            boss_health_text = font.render(f"Boss Health: {self.boss_health}", True, "red")
            self.screen.blit(boss_health_text, (10, 170))

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

            # Spawn a boss every 20 points
            if self.score > 0 and self.score % 20 == 0 and not self.boss:
                self.spawn_boss()

            # Check if player reached score goal
            if self.score >= self.score_goal:
                self.screen.fill(self.bg_color)
                self.display_message(f"You Win! Final Score: {self.score}", color="green")
                self.running = False

            # Check time limit
            if time.time() - self.start_time >= self.time_limit:
                self.screen.fill(self.bg_color)
                self.display_message(f"Time's Up! Final Score: {self.score}", color="yellow")
                self.running = False

            # Update game objects
            self.move_bullets()
            self.move_enemies()
            self.move_boss()
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
            if self.boss:
                self.screen.blit(self.boss_surf, self.boss)
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
