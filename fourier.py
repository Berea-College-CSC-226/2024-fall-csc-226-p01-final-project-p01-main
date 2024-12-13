######################################################################
# Author: Aliaksandr Melnichenka, Denys Zhytkov
# Username: melnichenkaa_zhytkovd
#
# Assignment: P01: Final Project
#
#
# Purpose: Learn about classes, inheritance, TKinter
######################################################################
# Acknowledgements:
#   But what is a Fourier series? From heat flow to drawing with circles | DE4 - https://youtu.be/r6sGWTCMz2k?feature=shared
#   But what is the Fourier Transform? A visual introduction - https://youtu.be/spUNpyF58BY?feature=shared
#   Coding Challenge #130.1: Drawing with Fourier Transform and Epicycles - https://youtu.be/MY4luNgGfms?feature=shared
#
#
# MIT Licence
####################################################################################


from svgpathtools import svg2paths
import numpy as np
import matplotlib.pyplot as plt


class Fourier():
    def __init__(self, file_path, coefficient_slider):
        """
        Class for calculating fourier series coefficients and putting it on the graph

        :param file_path: svg file, which contains all the needed paths
        :param coefficient_slider: value of the coefficient slider at the moment of uploading the picture
        """
        self.file_path = file_path
        self.N = coefficient_slider
        self.fourier_data = []


    def process_paths(self):
        """
        This function processes paths from the svg file with the help of compute_fourier_coefficients() and
        reconstruct_path() functions. The final goal is to create an array with fourier coefficients and corresponding frequencies

        :return: none
        """
        paths, attributes = svg2paths(self.file_path)       # function svg2paths parses svg file into paths and attributes, and returns them in a dictionary
        all_points = []

        for path in paths:                                  # go through each path in the dictionary
            if len(path) == 0:
                continue                                    # if path is empty, skip it

            num_samples = 1000
            t = np.linspace(0, 1, num_samples)           # we use function linspace from the numpy library to generate evenly spaced num_samples points between 0 and 1
            points = []
            for ti in t:                                                                    # go through each generated number
                points.append(path.point(ti))                                               # compute the complex point (x + yi)
            points = np.array(points)                                                       # we create a numpy array to allow easier array manipulation
            points = np.column_stack((points.real, points.imag))                            # separates real and imaginary parts of the complex number
            all_points.append(points)

        for points in all_points:                                                           # go through all points in the all_points array
            complex_points = points[:, 0] + 1j * points[:, 1]                               # convert points back to the complex numbers
            n, coefficients = self.compute_fourier_coefficients(complex_points, self.N)     # call compute_fourier_coefficients function which returns a tuple
            self.fourier_data.append((n, coefficients))                                     # store results


    def plot_fourier(self):
        """
        Using array self.fourier_data reconstructs the path into spacial domain and plots it using the matplotlib.pyplot

        :return: none
        """
        plt.figure(figsize=(8, 8))                                        # create new figure for the plot 8 by 8
        for n, coefficients in self.fourier_data:                         # go through each frequency and coefficient in fourier_data
            reconstructed = self.reconstruct_path(n, coefficients, 1000)  # calls reconstruct_path() to reconstruct fourier coefficients into spacial domain
            plt.plot(reconstructed.real, reconstructed.imag)        # draws the picture using real and imaginary numbers

        plt.axis('equal')
        plt.title('Image Reconstructed Using Fourier Series')
        plt.show()                                                        # shows the plot on the screen


    def compute_fourier_coefficients(self, points, N):
        """
        Computes fourier coefficients using fourier transform formula for an each

        :param points: points which consist of real and imaginary part
        :param N: number on the coefficient slider during the picture uploading
        :return: tuple of frequency and numpy array of coefficients
        """
        N = int(N)                          # ensures that number on the coefficient slider will be an integer
        T = len(points)                     # gets the total number of points
        n = np.arange(-N, N + 1)            # creates an array of frequencies from -N to N+1
        coefficients = []

        for k in n:                                                                     # begins a loop to go through each frequency
            c = (1 / T) * np.sum(points * np.exp(-2j * np.pi * k * np.arange(T) / T))   # Fourier transform formula for a frequency k
            coefficients.append(c)
        return n, np.array(coefficients)


    def reconstruct_path(self, n, coefficients, num_points):
        """
        Takes fourier coefficients and reconstructs them into array with real and imaginary numbers

        :param n: frequencies
        :param coefficients: fourier coefficients
        :param num_points: total number of points
        :return: an array where real part  represents x and imaginary - y
        """
        T = num_points
        t = np.linspace(0, 1, T)                    # creates an array of T intervals between 0 and 1
        reconstructed = np.zeros(T, dtype=complex)             # creates a zero-filled array of lenght T

        for k, c in zip(n, coefficients):                       # go through frequencies and coefficients
            reconstructed += c * np.exp(2j * np.pi * k * t)     # reconstructs path from the fourier frequencies and complex number coefficients

        return reconstructed