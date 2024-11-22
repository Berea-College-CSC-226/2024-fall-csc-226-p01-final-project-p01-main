######################################################################
# Author: Aliaksandr Melnichenka, Denys Zhytkov        TODO: Change this to your names
# Username: melnichenkaa_zhytkovd
#
# Assignment: P01: Final Project
#
#
# Purpose: Learn about classes, inheritance, and Pygame
######################################################################
# Acknowledgements:
#
#
# MIT Licence
####################################################################################

# import pygame

import web_application
from xml.dom import minidom


class ImageProcessor():
    """
    A class to process the image.
    """
    def __init__(self, svg_content):
        self.svg_content = svg_content 
    def process_image(self):
        paths = []
        content = self.svg_content.lower()
        # print(content)

        while '<path' in content:
            path_start = content.find('<path')
            path_end = content.find('>', path_start) + 1

            path_element = content[path_start:path_end]
            paths.append(path_element)

            # Update content to remove the processed path
            content = content[path_end:]

        return paths


def main():
    """
    Main function to run the web application.
    """
    app = web_application.SVGApp()
    # print(app.config['UPLOAD_FOLDER'])
    app.run()

if __name__ == '__main__':
    main()