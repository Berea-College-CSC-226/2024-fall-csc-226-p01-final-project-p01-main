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

        :return:
        """
        paths, attributes = svg2paths(self.file_path)       # function svg2paths parses svg file into paths and attributes, and returns them in a dictionary
        all_points = []

        for path in paths:                                  # go through each path in the dictionary
            if len(path) == 0:
                continue                                    # if path is empty, skip it

            num_samples = 1000
            t = np.linspace(0, 1, num_samples)           # we use function linspace from the numpy library to generate evenly spaced num_samples points between 0 and 1
            points = []
            for ti in t:                                            # go through each generated number
                points.append(path.point(ti))                       # compute the complex point (x + yi)
            points = np.array(points)
            points = np.column_stack((points.real, points.imag))
            all_points.append(points)

        for points in all_points:
            complex_points = points[:, 0] + 1j * points[:, 1]
            n, coefficients = self.compute_fourier_coefficients(complex_points, self.N)
            self.fourier_data.append((n, coefficients))

    def plot_fourier(self):
        """

        :return:
        """
        plt.figure(figsize=(8, 8))
        for n, coefficients in self.fourier_data:
            reconstructed = self.reconstruct_path(n, coefficients, 1000)
            plt.plot(reconstructed.real, reconstructed.imag)

        plt.axis('equal')
        plt.title('Image Reconstructed Using Fourier Series')
        plt.show()

    def compute_fourier_coefficients(self, points, N):
        """"

        """
        N = int(N)
        T = len(points)
        n = np.arange(-N, N + 1)
        coefficients = []

        for k in n:
            c = (1 / T) * np.sum(points * np.exp(-2j * np.pi * k * np.arange(T) / T))
            coefficients.append(c)
        return n, np.array(coefficients)

    def reconstruct_path(self, n, coefficients, num_points):
        """

        :param n:
        :param coefficients:
        :param num_points:
        :return:
        """
        T = num_points
        t = np.linspace(0, 1, T)
        reconstructed = np.zeros(T, dtype=complex)

        for k, c in zip(n, coefficients):
            reconstructed += c * np.exp(2j * np.pi * k * t)

        return reconstructed