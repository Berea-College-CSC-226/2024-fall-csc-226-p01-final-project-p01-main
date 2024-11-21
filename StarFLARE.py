import pygame
import random
import tkinter as tk

class GUI:
    def __init__(self, width, height):
        """
        Initializes the GUI, creates the window for the game
        """
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("StarFLARE Dodge")  # Set window title
        self.width = width
        self.height = height

        self.screen.fill((0, 0, 0)) #sets the screen color to black

    def button(self):
        """
        draws a button on the window, and checks if the button was clicked or not
        """


class Game:
    def __init__(self, windowtext="Exploring Tkinter"):
        """
        Initializes the game, which also includes the two other classes
        """

        self.root = tk.Tk()
        self.root.minsize(width=500, height=300)
        self.root.maxsize(width=500, height=300)
        self.root.title(windowtext)

        self.width = 600
        self.height = 600
        self.rocket_width = 200
        self.rocket_height = 200
        self.falling_balls_radius = 10
        self.PURPLE = (128, 0, 128)
        self.BROWN = (165, 42, 42)
        self.GREEN = (0, 255, 0)



    def spawn_ball(self):
        """
        spawns a new ball randomly at the top of the screen
        """





    def check_collision(self):
        """
        checks for collision between the falling balls and the rocket
        """

    def draw_objects(self):
        """
        draws the objects on the screen this includes all the random balls, the score, and the rocket
        """




    def main_loop(self):
        """
        the main loop that runs the game
        """




    def game_over(self):
        """
        "Game Over" is shown when a collision is detected between the falling random and the rocket.
        """





    def restart(self):
        """
        restarts the game and also resets the clock
        :return:
        """





class player:
    def __init__(self):
        """
        Initializes the player's (rocket)
        """



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



class Dodgeball:
    def __init__(self):
        """
        Initializes the random falling balls
        """




    def move_down(self):
        """
        moves the falling balls downward
        :return:
        """


    def draw_dodgeballs(self):
        """
        draws the dodgeballs on the screen
        :return:
        """




    def off_screen(self):
        """
        checks if dodgeballs are off the screen
        :return:
        """




def main():
    """
    creates the game and keeps it running
    """






if __name__ == "__main__":
     main()
