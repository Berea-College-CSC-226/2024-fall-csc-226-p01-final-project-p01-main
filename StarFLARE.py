from random import randint

import pygame
import random

class GUI:
    def __init__(self, width = 500, height = 500):
        """
        Initializes the GUI, creates the window for the game
        """
        pygame.init()
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('StarFLARE Dodge')
        self.clock = pygame.time.Clock()

        self.balls = []
        self.player = Player(self.size[0], self.size[1])
        self.score = 0
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def button(self):
        """
        draws a button on the window, and checks if the button was clicked or not
        """
        pass

    def off_screen(self):
        """
        checks if dodgeballs are off the screen
        :return:
        """
        pass

    def game_over(self):
        """
        "Game Over" is shown when a collision is detected between the falling random and the rocket.
        """
        pass

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

        self.balls = []
        self.player = Player(self.size[0], self.size[1])
        self.score = 0
        self.running = True
        self.ball = Dodgeball()

    def spawn_ball(self):
        """
        spawns a new ball randomly at the top of the screen
        """
        if random.random() < -5:  # 2% chance to spawn a new ball every frame
            new_ball = Dodgeball(50, 60)
            self.balls.append(new_ball)

    def check_collision(self):
        """
        checks for collision between the falling balls and the rocket
        """
        pass

    def draw_objects(self):
        """
        draws the objects on the screen this includes all the random balls, the score, and the rocket
        """
        self.screen.fill((0, 0, 0)) #this sets the screen to black
        for ball in self.balls:
            ball.draw(self.screen)
        self.player.draw_rocket(self.screen)

        #for displaying the screen

    def restart(self ):
        """
        restarts the game and also resets the clock
        :return:
        """
        pass

    def run(self):
        while self.running:
            self.clock.tick(90)  # Limit the frame rate to 60 FPS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Move the player
            self.player.left_right()

            # Spawn a new ball every 2 seconds
            # if random.random() < 0.02:  # Randomly spawn balls
            #     self.spawn_ball()

            self.check_collision()
            self.draw_objects()

            self.ball.draw(self.screen)
            self.ball.move_down()
            pygame.display.update()

class Player:
    def __init__(self, width, height):
        """
        Initializes the player's (rocket)
        """
        self.x = width // 2
        self.y = height - 60
        self.speed = 5

    def left_right(self):
        """
        moves left and right, using the left and right arrows, based on the user's input
        :return:
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.x = max(0, min(self.x, 500 - 50))  #so the rocket don't go out of bound

    def draw_rocket(self, screen):
        """
        draws the rocket on the screen
        :return:
        """
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 50, 60))

class Dodgeball:
    def __init__(self):
        """
        Initializes the random falling balls
        """
        self.y = 0
        self.speed = 1
        self.size = 15

    def move_down(self):
        """
        moves the falling balls downward
        :return:
        """
        #top left is 0,0
        #when move left, x is increasing, moving down decreases y value
        self.y += self.speed

    def draw(self, screen):
        """
        draws the dodgeballs on the screen
        :return:
        """

        pygame.draw.circle(screen, (255, 0, 0), (randint(0, 500), self.y), self.size) #red falling balls

if __name__ == "__main__":
    game = Game()
    game.run()