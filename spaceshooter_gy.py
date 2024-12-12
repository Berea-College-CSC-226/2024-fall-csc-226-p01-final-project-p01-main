import pygame
import random
import time


class Game:
    def __init__(self):
        """
        Initialize the Space Shooter game.
        """
        # Set the screen size (width, height)
        self.size = 800, 600

        # Boolean to control whether the game is running
        self.running = True

        # Initialize pygame
        pygame.init()

        # Create the game window
        self.screen = pygame.display.set_mode(self.size)

        # Set the title of the window
        pygame.display.set_caption("Space Shooter")

        # Create a clock to control game speed
        self.clock = pygame.time.Clock()

        # Background color (black)
        self.bg_color = "#000000"

        # Load player, bullet, enemy, and boss assets (simple colored rectangles)
        self.player_surf = pygame.Surface((50, 50))
        self.player_surf.fill("#FFFFFF")  # Player is white

        self.bullet_surf = pygame.Surface((10, 20))
        self.bullet_surf.fill("#FFFFFF")  # Bullets are white

        self.enemy_surf = pygame.Surface((50, 50))
        self.enemy_surf.fill("#FF0000")  # Enemies are red

        self.boss_surf = pygame.Surface((150, 100))
        self.boss_surf.fill("#0000FF")  # Boss is blue

        # Initialize player position
        self.player_rect = pygame.Rect(self.size[0] // 2, self.size[1] - 70, 50, 50)

        # Lists to hold game objects (bullets, enemies)
        self.bullets = []
        self.enemies = []

        # Boss attributes
        self.boss = None  # No boss initially
        self.boss_health = 0
        self.boss_direction = 1  # Boss moves left and right

        # Timers and game settings
        self.spawn_timer = 0  # Timer to control enemy spawning
        self.score = 0  # Player score
        self.health = 3  # Player health (number of hits allowed)
        self.speed_multiplier = 1.0  # Game speed (increases as score increases)
        self.time_limit = 120  # Total game time in seconds (2 minutes)
        self.start_time = time.time()  # Record the game start time
        self.score_goal = 50  # Points required to win

    def display_message(self, message, color="white"):
        """
        Displays a message in the center of the screen.
        """
        font = pygame.font.SysFont("ComicSansMS", 48)  # Font for the message
        text_surface = font.render(message, True, color)  # Create the text surface
        text_rect = text_surface.get_rect(center=(self.size[0] // 2, self.size[1] // 2))  # Center the text
        self.screen.blit(text_surface, text_rect)  # Draw the text on the screen
        pygame.display.update()  # Update the display
        pygame.time.delay(2000)  # Pause for 2 seconds

    def spawn_enemy(self):
        """
        Creates a new enemy at a random position at the top of the screen.
        """
        x = random.randint(0, self.size[0] - 50)  # Random x-coordinate
        self.enemies.append(pygame.Rect(x, -50, 50, 50))  # Add new enemy to the list

    def spawn_boss(self):
        """
        Creates a boss at the top of the screen.
        """
        self.boss = pygame.Rect(self.size[0] // 2 - 75, 50, 150, 100)  # Boss starts centered
        self.boss_health = 10  # Boss requires 10 hits to defeat

    def move_bullets(self):
        """
        Moves bullets upward and removes them if they go off-screen.
        """
        for bullet in self.bullets[:]:
            bullet.move_ip(0, -7 * self.speed_multiplier)  # Move bullet up
            if bullet.top <= 0:  # If bullet is off-screen
                self.bullets.remove(bullet)

    def move_enemies(self):
        """
        Moves enemies downward and removes them if they go off-screen.
        """
        for enemy in self.enemies[:]:
            enemy.move_ip(0, 3 * self.speed_multiplier)  # Move enemy down
            if enemy.top >= self.size[1]:  # If enemy is off-screen
                self.enemies.remove(enemy)

    def move_boss(self):
        """
        Moves the boss left and right across the screen.
        """
        if self.boss:
            self.boss.move_ip(5 * self.boss_direction, 0)  # Move boss horizontally
            # Change direction if the boss hits the screen edges
            if self.boss.left <= 0 or self.boss.right >= self.size[0]:
                self.boss_direction *= -1

    def detect_collisions(self):
        """
        Checks for collisions between bullets, enemies, boss, and the player.
        """
        # Check for bullet collisions with enemies
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.colliderect(enemy):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1  # Increase score
                    break

            # Check for bullet collisions with the boss
            if self.boss and bullet.colliderect(self.boss):
                self.bullets.remove(bullet)
                self.boss_health -= 1
                if self.boss_health <= 0:  # Boss defeated
                    self.score += 20  # Large score boost
                    self.boss = None

        # Check for enemy collisions with the player
        for enemy in self.enemies[:]:
            if enemy.colliderect(self.player_rect):
                self.enemies.remove(enemy)
                self.health -= 1  # Player loses health

        # Check for boss collisions with the player
        if self.boss and self.boss.colliderect(self.player_rect):
            self.health -= 1
            self.boss = None  # Remove boss on collision

    def render_hud(self):
        """
        Displays player's score, health, boss health, and remaining time.
        """
        font = pygame.font.SysFont(None, 36)  # Font for HUD
        # Render score, health, timer, and goal
        score_text = font.render(f"Score: {self.score}", True, "white")
        health_text = font.render(f"Health: {self.health}", True, "white")
        time_remaining = max(0, self.time_limit - int(time.time() - self.start_time))  # Time left
        timer_text = font.render(f"Time Left: {time_remaining}s", True, "white")
        goal_text = font.render(f"Goal: {self.score}/{self.score_goal}", True, "white")
        # Draw HUD elements on the screen
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(health_text, (10, 50))
        self.screen.blit(timer_text, (10, 90))
        self.screen.blit(goal_text, (10, 130))
        # Display boss health if the boss is active
        if self.boss:
            boss_health_text = font.render(f"Boss Health: {self.boss_health}", True, "red")
            self.screen.blit(boss_health_text, (10, 170))

    def increase_difficulty(self):
        """
        Gradually increases game speed based on the player's score.
        """
        self.speed_multiplier = 1.0 + (self.score // 10) * 0.1  # Speed increases every 10 points

    def run(self):
        """
        Main game loop: handles input, updates, and rendering.
        """
        while self.running:
            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit the game
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Fire a bullet
                        bullet = pygame.Rect(self.player_rect.centerx - 5, self.player_rect.top, 10, 20)
                        self.bullets.append(bullet)

            # Move player with arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player_rect.left > 0:
                self.player_rect.move_ip(-5, 0)
            if keys[pygame.K_RIGHT] and self.player_rect.right < self.size[0]:
                self.player_rect.move_ip(5, 0)

            # Spawn enemies periodically
            self.spawn_timer += 1
            if self.spawn_timer > max(50 - self.score // 10, 20):  # Adjust spawn rate as score increases
                self.spawn_enemy()
                self.spawn_timer = 0

            # Spawn a boss every 20 points
            if self.score > 0 and self.score % 20 == 0 and not self.boss:
                self.spawn_boss()

            # Check if player reaches score goal
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
            self.increase_difficulty()

            # End game if player health reaches zero
            if self.health <= 0:
                self.screen.fill(self.bg_color)
                self.display_message("Game Over", color="red")
                self.running = False

            # Redraw everything on the screen
            self.screen.fill(self.bg_color)
            self.screen.blit(self.player_surf, self.player_rect)  # Draw the player
            for bullet in self.bullets:
                self.screen.blit(self.bullet_surf, bullet)  # Draw each bullet
            for enemy in self.enemies:
                self.screen.blit(self.enemy_surf, enemy)  # Draw each enemy
            if self.boss:
                self.screen.blit(self.boss_surf, self.boss)  # Draw the boss
            self.render_hud()  # Display the HUD

            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit to 60 frames per second

        pygame.quit()


def main():
    """
    Starts the Space Shooter game.
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
