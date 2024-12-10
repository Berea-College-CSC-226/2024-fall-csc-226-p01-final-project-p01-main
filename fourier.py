from svgpathtools import svg2paths
import numpy as np
import matplotlib.pyplot as plt

class Fourier():
    def __init__(self, file_path, coefficient_slider):
        self.file_path = file_path
        self.N = coefficient_slider
        self.fourier_data = []

    def process_paths(self):
        paths, attributes = svg2paths(self.file_path)
        all_points = []

        for path in paths:
            if len(path) == 0:
                continue

            num_samples = 1000
            t = np.linspace(0, 1, num_samples)
            points = []
            for ti in t:
                points.append(path.point(ti))
            points = np.array(points)
            points = np.column_stack((points.real, points.imag))
            all_points.append(points)

        for points in all_points:
            complex_points = points[:, 0] + 1j * points[:, 1]
            n, coefficients = self.compute_fourier_coefficients(complex_points, self.N)
            self.fourier_data.append((n, coefficients))

    def plot_fourier(self):

        plt.figure(figsize=(8, 8))
        for n, coefficients in self.fourier_data:
            reconstructed = self.reconstruct_path(n, coefficients, 1000)
            plt.plot(reconstructed.real, reconstructed.imag)

        plt.axis('equal')
        plt.title('Image Reconstructed Using Fourier Series')
        plt.show()

    def compute_fourier_coefficients(self, points, N):
            N = int(N)
            T = len(points)
            n = np.arange(-N, N + 1)
            coefficients = []

            for k in n:
                c = (1 / T) * np.sum(points * np.exp(-2j * np.pi * k * np.arange(T) / T))
                coefficients.append(c)
            return n, np.array(coefficients)

    def reconstruct_path(self, n, coefficients, num_points):
            T = num_points
            t = np.linspace(0, 1, T)
            reconstructed = np.zeros(T, dtype=complex)

            for k, c in zip(n, coefficients):
                reconstructed += c * np.exp(2j * np.pi * k * t)

            return reconstructed