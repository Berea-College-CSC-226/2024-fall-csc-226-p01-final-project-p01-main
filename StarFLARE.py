######################################################################
# Author: Din din
# Username: parn
#
# Assignment: Final Project
#
# Purpose: To show what I learned throughout the semester
#game purpose: my game is going to have asteriods/balls coming down from the screen and the rocket(main piece) is going to have to dodge them, if not you die.
######################################################################
# Acknowledgements:
#
# Dr Heggens: for overall layout, gave me ideas on how my layout should look like
# -told me to change the objects into sprites, so collision can happen
# -Gave me a startup blueprint and I used T11 along with it
#
# ChatGPT: used it to help fix the code for my falling ball issue.
# -I had one ball moving horizontally while moving down, so I used chat to help me fix the code, to where multiple balls are spawned at the top and not just one ball.
# -On line 132, pygame.SRCALPHA is used for transparency around the falling red balls
# -Using pygame.rect is easier to handle sprite positions and collisions
# -helped me display the score in the top left corner of the screen
# https://chatgpt.com/
#
# Tojo: helped me with the inits and also got my screen to work
# -helped me start the dodgeballs moving downwards
#
# pygame documentations: used throughout the game, esp for drawing the objects (player and the red circles)
# -Used it for event handler
# -helped me with this line of code: pygame.time.wait(2000), this exits the game after a second
# -helped me position the player at the bottom of the game, and also helped me spawn the player at the center everytime it spawns
# -helped me with some of the test suites, I saw some codes on the website, but I didn't really undestand
# https://www.pygame.org/docs/
#
# Nauka: Helped me draw the falling balls on the screen and also with the random radiants (I needed the random radiants for the falling balls)
####################################################################################

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

        if pygame.sprite.spritecollide(self.player, self.balls, False):
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
