from random import randint
import pygame
import random

class Game:
    def __init__(self):
        """
        Initializes the game
        """
        pygame.init()
        self.size = (500, 500)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('StarFLARE Dodge')
        self.clock = pygame.time.Clock()

        self.balls = pygame.sprite.Group()  # Group for all dodgeballs, better organization
        self.player = Player(self.size[0], self.size[1])  # Create the player sprite
        self.all_sprites = pygame.sprite.Group(self.player)  # Group for all sprites (player + dodgeballs)
        self.score = 0
        self.running = True

    def spawn_ball(self):
        """
        spawns a new ball randomly at the top of the screen
        """
        if random.random() < 0.10:  # 10% chance to spawn a new ball every frame
            new_ball = Dodgeball()
            self.balls.add(new_ball)  # Add the new ball to the ball group
            self.all_sprites.add(new_ball)

    def check_collision(self):
        """
        checks for collision between the falling balls and the player (rocket)
        """
        for ball in self.balls:
            if pygame.sprite.spritecollide(self.player, [ball], False):
                # If a collision is detected, call the game over method
                self.game_over()

    def game_over(self):
        """
        Handle game over state
        """
        self.running = False  # Stop the game
        print(f"Game Over! Final Score: {self.score}")

        # Display the "You Died" message in the middle of the screen
        font = pygame.font.SysFont("ComicSans", 36)
        txt = font.render('Game Over.', True, "red")
        self.screen.blit(txt, (self.size[0] // 2 - txt.get_width() // 2, self.size[1] // 2 - 50))  # Center text

        # Display the final score message
        score_txt = font.render(f"Final Score: {self.score}", True, "white")
        self.screen.blit(score_txt,(self.size[0] // 2 - score_txt.get_width() // 2, self.size[1] // 2 + 10))  # Center text

        pygame.display.update()
        pygame.time.wait(1000)

    def draw_objects(self):
        """
        Draws the objects on the screen this includes all the sprites and the score
        """
        self.screen.fill((0, 0, 0))  # this sets the screen to black
        self.all_sprites.draw(self.screen)  # all sprites are drawn

        font = pygame.font.SysFont(None, 36)  # Font object for displaying the score
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))  # Render the score text
        self.screen.blit(score_text, (10, 10))  # Display the score in the top-left corner

    def restart(self):
        """
        restarts the game and also resets the clock
        :return:
        """
        self.score = 0
        self.balls.empty()  # Remove all the balls
        self.all_sprites.empty()  # Remove all sprites
        self.player = Player(self.size[0], self.size[1])  # Recreate the player sprite
        self.all_sprites.add(self.player)

    def run(self):
        """
        This is the main loop of the game, this runs the game
        """
        while self.running:
            self.clock.tick(60) #game will run at a rate of 60 frames per second

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.left_right()  # moves the player left or right based on user's input

            self.spawn_ball()

            for ball in self.balls:
                ball.move_down()

            self.check_collision()
            self.draw_objects()

            pygame.display.update()

            if not self.running:
                self.game_over()

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        """
        Initializes the player's (rocket)
        """
        super().__init__()
        self.image = pygame.Surface((50, 60))  # Create a surface for the player
        self.image.fill((0, 255, 0))  # sets the player's color to green
        self.rect = self.image.get_rect()  # used for positioning the sprite on the screen and for collision detection
        self.rect.center = (width // 2, height - 60)
        self.rect.bottom = height
        self.speed = 5

    def left_right(self):
        """
        moves left and right, using the left and right arrows, based on the user's input
        :return:
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.rect.x = max(0, min(self.rect.x, 500 - self.rect.width))  # this makes sure the player stays within the boundary

class Dodgeball(pygame.sprite.Sprite):
    def __init__(self):
        """
        Represents the falling red balls that the player needs to dodge
        """
        super().__init__()
        self.size = 17
        self.image = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)  # Create a surface for the ball and makes the rectangle surrounding the ball transparent
        pygame.draw.circle(self.image, (255, 0, 0), (self.size, self.size), self.size)  # Draws a red circle
        self.rect = self.image.get_rect()  # used for positioning the sprite on the screen and for collision
        self.rect.x = randint(0, 500 - self.rect.width)  # Random x position at the top of the screen
        self.rect.y = 0
        self.speed = randint(5, 7)

    def move_down(self):
        """
        moves the falling balls downward and removes the balls once it reaches the bottom of the screen
        :return:
        """
        self.rect.y += self.speed
        if self.rect.y > 500:  # Remove the ball if it goes past the bottom of the screen
            self.kill()

if __name__ == "__main__":
    game = Game()
    game.run()
