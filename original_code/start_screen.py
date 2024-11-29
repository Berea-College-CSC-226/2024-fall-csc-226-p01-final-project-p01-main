######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose:
#
from tkinter import PhotoImage

#######################################################################
# Acknowledgements:
#
#
#
####################################################################################

import pygame, tkinter as tk


#create two buttons. Play and Quit

class Start_Screen:
    def __init__(self, windowtext=""):
        """
        Creates the window
        :param: Name of the window
        """
        self.root = tk.Tk()
        self.root.minsize(width=600, height=800)
        self.root.maxsize(width=600, height=800)
        self.root.title(windowtext)

        #for background img
        #bkg_image = PhotoImage(file = "")

        self.Button1 = None
        self.Button2 = None


    def create_button1(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the start button that opens the game
        :return:
        """

    def create_button2(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the quit button that closes the window
        :return:
        """


    def button_handler1(self):
        """

        :return:
        """

    def button_handler2(self):
        """

        :return:
        """



def main():
    """
    Runs the program and creates the window
    :return:
    """


    pass

if __name__ == "__main__":
    main()
#Play opens game.py

#quit closes window

#visual graphic for title + bkg



