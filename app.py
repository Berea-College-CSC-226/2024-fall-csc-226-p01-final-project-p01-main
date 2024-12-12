######################################################################
# Author: Aliaksandr Melnichenka, Denys Zhytkov
# Username: melnichenkaa_zhytkovd
#
# Assignment: P01: Final Project
#
#
# Purpose: Learn about classes, inheritance, CustomTKinter
######################################################################
# Acknowledgements:
#   But what is a Fourier series? From heat flow to drawing with circles | DE4 - https://youtu.be/r6sGWTCMz2k?feature=shared
#   But what is the Fourier Transform? A visual introduction - https://youtu.be/spUNpyF58BY?feature=shared
#   Coding Challenge #130.1: Drawing with Fourier Transform and Epicycles - https://youtu.be/MY4luNgGfms?feature=shared
#
#
# MIT Licence
####################################################################################

import customtkinter as ctk
from tkinter import filedialog
import fourier


class App(ctk.CTk):
    def __init__(self):
        """
        Class for handling interface of our program.
        """
        super().__init__()


    def create_interface(self):
        """
        Creates a window 400x300 with an upload button, slider, and two labels.
        :return: none
        """
        self.title("SVG Fourier Reconstruction")                # name of the window
        self.geometry("400x300")                                # size of the window

        self.upload_button = ctk.CTkButton(self, text="Upload Image", command=self.upload_and_process_image)            # creates CustomTKinter button
        self.upload_button.pack(pady=20)

        self.coefficient_slider = ctk.CTkSlider(self, from_=1, to=100, orientation='horizontal', command=self.update_coefficient_label) # creates CustomTKinter slider
        self.coefficient_slider.set(50)
        self.coefficient_slider.pack(pady=20)

        self.coefficient_label = ctk.CTkLabel(self, text=f"Fourier Coefficients: {int(self.coefficient_slider.get())}") # creates CustomTKinter label
        self.coefficient_label.pack()

        self.processing_label = ctk.CTkLabel(self, text="")                                                             # creates CustomTKinter label
        self.processing_label.pack()


    def upload_and_process_image(self):
        """
        Called if user presses upload_button. Gets file from the user, checks if it is okay.
        Then, creates Fourier class object, which performs all the calculations and creates a plot with a new picture.
        :return:
        """
        file_path = filedialog.askopenfilename(filetypes=[("SVG files", "*.svg")])  # ask user to choose a svg file

        if not file_path:
            self.processing_label.configure(text="")                            # updates label, if the file is empty
            return

        self.processing_label.configure(text="Processing image...")
        self.update_idletasks()                                                 # update the GUI to show the label

        self.img = fourier.Fourier(file_path, self.coefficient_slider.get())    # create an object Fourier
        self.img.process_paths()                                                # calculate frequencies and coefficients using fourier series formula
        self.img.plot_fourier()                                                 # create a plot with a reconstructed picture


    def update_coefficient_label(self, value):
        """
        When user changes coefficient_slider, this function updates label to the number that user chose
        :param value: integer that user chose on the slider
        :return:
        """
        self.coefficient_label.configure(text=f"Fourier Coefficients: {int(float(value))}")         # updates label


def main():
    """
    Creates an object of the class App() and runs the interface until user closes it.
    :return: none
    """
    app = App()                 # create an App object
    app.create_interface()      # create a GUI interface
    app.mainloop()              # run an infinite interface loop


if __name__ == "__main__":
    main()




