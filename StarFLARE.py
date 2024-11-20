import pygame
import random
import tkinter as tk

class DodgeBalls:
    def __init__(self):
        """
        Initializes the game, it sets up the width and height of the falling balls and the rocket.
        It also sets up the falling balls' radius. Sets up screen, colors and the variables needed in the game.
        """
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





    def move_rocket(self):
        """
        Moves the rocket based on the user's input, only the left and right arrows on the keyboard work.
        """



    def falling_balls(self):
        """
        the balls that were spawned at the top are going down the screen in a straight line
        """




    def check_collision(self):
        """
        checks for collision between the falling balls and the rocket, and if a collision occurs, then game over. If a collision doesn't
        occur, then the game keeps going on until a collision occurs.
        """




    def game_loop(self):
        """
        main game loop, keeps the game running
        """



    def game_over(self):
        """
        "Game Over" is displayed when the game is over, waits for the user to click either start over or quit.
        """





def main():
    """
    creates the game and keeps it running
    """






if __name__ == "__main__":
     main()
