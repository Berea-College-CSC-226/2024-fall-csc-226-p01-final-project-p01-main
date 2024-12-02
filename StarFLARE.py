import pygame
import random
import tkinter as tk

class GUI:
    def __init__(self, width, height):
        """
        Initializes the GUI, creates the window for the game
        """

        # self.game = Game()
        # self.root = tk.Tk()  # Create the root window where all widgets go
        # self.root.minsize(width=500, height=300)  # Sets the window's minimum size
        # self.root.maxsize(width=500, height=300)  # Sets the window's maximum size
        # self.root.title(windowtext)
        # # self.screen = screen

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("StarFLARE Dodge")
        self.width = width
        self.height = height

        self.screen.fill((0, 0, 0)) #sets the screen color to black

    def button(self):
        """
        draws a button on the window, and checks if the button was clicked or not
        """

        button =



    def off_screen(self):
        """
        checks if dodgeballs are off the screen
        :return:
        """





    def game_over(self):
        """
        "Game Over" is shown when a collision is detected between the falling random and the rocket.
        """





class Game:
    def __init__(self, windowtext="Exploring Tkinter"):
        """
        Initializes the game
        """

        #self.ball = Dodgeball()
        self.balls = []
        self.player = player()
        self.score = 0
        self.running = True


    def spawn_ball(self):
        """
        spawns a new ball randomly at the top of the screen
        """
        x_position = random.randint(0, 300)   #spawns balls randomly on top of the screen
        self.balls.append(Dodgeball(x_position, 0))


    def check_collision(self):
        """
        checks for collision between the falling balls and the rocket
        """

        for ball in self.balls:
            if ball


    def draw_objects(self):
        """
        draws the objects on the screen this includes all the random balls, the score, and the rocket
        """
        self.screen.fill((0, 0, 0)) #this sets the screen to black
        for ball in self.balls:
            ball.draw(self.screen)
        self.player.draw_rocket(self.screen)

        #for displaying the screen





    def main_loop(self):
        """
        the main loop that runs the game
        """

        while self.running:
            self.clock.tick(100)  # the number represents how fast the balls will fall
            self.score += 1




    def restart(self):
        """
        restarts the game and also resets the clock
        :return:
        """
        self.score = 0
        self.player = player(self.width, self.height)  # Reset the player
        self.balls = []
        self.running = True  # restart the game loop
        self.main_loop()


class player:
    def __init__(self, width, height):
        """
        Initializes the player's (rocket)
        """
        self.x = width // 2
        self.y = height - 60
        self.speed = 5 #rocket's speed


    def left_right(self):
        """
        moves left and right, using the left and right arrows, based on the user's input
        :return:
        """




    def draw_rocket(self):
        """
        draws the rocket on the screen
        :return:
        """

        pygame.draw.rect()



class Dodgeball:
    def __init__(self):
        """
        Initializes the random falling balls
        """

        self.x = random.randint(0, 300)
        self.speed = 5
        self.size = 15



    def move_down(self):
        """
        moves the falling balls downward
        :return:
        """



    def draw(self):
        """
        draws the dodgeballs on the screen
        :return:
        """





def main():
    """
    creates the game and keeps it running.
    """

    gui = GUI()
    gui.game
    gui.game_over
    gui.button
    gui.off_screen


if __name__ == "__main__":
     main()