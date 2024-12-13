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


import cv2
import svgwrite
import fourier


class PhotoCapture:
    def __init__(self, coefficient_slider):
        """
        PhotoCapture class captures, converts and processes a photo from the web-camera

        :param:coefficient_slider - the number which was on the slider in the moment of capturing the photo
        :return: none
        """
        self.coefficient_slider = coefficient_slider

    def capture_and_save_photo(self):
        """
        This method captures photo using webcam, processes it and converts it to svg

        :return: none
        """
        cap = cv2.VideoCapture(0)                   # initialize camera with index 0

        if not cap.isOpened():
            return                                  # return if the camera is not accessible

        ret, frame = cap.read()                     # capture one frame from the camera

        if not ret:
            cap.release()
            return                                      # return if camera failed to capture the frame

        frame = cv2.rotate(frame, cv2.ROTATE_180)       # rotates the frame by 180 degrees

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert it to the grayscale

        edges = cv2.Canny(gray, 100, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   # find contours

        dwg = svgwrite.Drawing('cam.svg', profile='tiny')               # create an svg drawing object

        for contour in contours:                                                # iterate through each contour
            points = []
            for point in contour:                                               # iterate through each point in the contour
                x = float(point[0][0])                                          # extract the x coordinate
                y = float(point[0][1])                                          # extract the y coordinate
                points.append((x, y))                                           # add point in the form of tuple to the list
            dwg.add(dwg.polyline(points, stroke='black', fill='none'))          # add polyline to the SVG

        dwg.save()                                                              # save svg file
        cap.release()

        self.process_svg_file('cam.svg')                                        # process the svg

    def process_svg_file(self, file_path):
        """
        This method creates an object of the Fourier class, processes the given paths and plots the picture.

        :param: file_path is a svg file which contains paths
        :return: none
        """
        img = fourier.Fourier(file_path, self.coefficient_slider.get())
        img.process_paths()
        img.plot_fourier()
