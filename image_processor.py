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

import tkinter as tk
from tkinter import filedialog
from xml.dom import minidom
import svg.path


class ImageProcessor():
    """
    A class to process the image.
    """
    def __init__(self, svg_content):
        self.svg_content = svg_content

    def parse_svg(self, convert_lines=True, convert_polylines=True, convert_polygons=True, return_svg_attributes=False):
        """
        Converts SVG content into a list of Path objects and their attributes.

        Args:
            convert_lines (bool): Whether to convert Line elements to Paths
            convert_polylines (bool): Whether to convert Polyline elements to Paths
            convert_polygons (bool): Whether to convert Polygon elements to Paths
            return_svg_attributes (bool): Whether to return SVG root attributes

        Returns:
            tuple: (paths_list, attributes_list, svg_attributes if requested)
        """
        paths = []
        attributes = []
        svg_attributes = {}

        # Parse SVG content
        doc = minidom.parseString(self.svg_content)

        # Get SVG root attributes if requested
        if return_svg_attributes:
            svg_elem = doc.getElementsByTagName('svg')[0]
            svg_attributes = dict(svg_elem.attributes.items())

        # Process path elements
        path_elements = doc.getElementsByTagName('path')
        for path in path_elements:
            paths.append(path.getAttribute('d'))
            attributes.append(dict(path.attributes.items()))

        # Process other elements if requested
        if convert_lines:
            lines = doc.getElementsByTagName('line')
            for line in lines:
                x1 = float(line.getAttribute('x1'))
                y1 = float(line.getAttribute('y1'))
                x2 = float(line.getAttribute('x2'))
                y2 = float(line.getAttribute('y2'))
                path_data = f'M {x1},{y1} L {x2},{y2}'
                paths.append(path_data)
                attributes.append(dict(line.attributes.items()))

        # Clean up
        doc.unlink()

        if return_svg_attributes:
            return paths, attributes, svg_attributes
        return paths, attributes


def select_file(result_label):
    """
    Handle file selection and processing
    """
    file_path = filedialog.askopenfilename(
        title="Select SVG file",
        filetypes=[("SVG files", "*.svg")]
    )

    if file_path:
        with open(file_path, 'r') as file:
            svg_content = file.read()
            processor = ImageProcessor(svg_content)
            paths, attributes = processor.parse_svg()
            result_label.config(text=f"Processed {len(paths)} paths from {file_path}")
            for path in paths:
                segments = convert_svg_path_data(path)

                print(segments)

def convert_svg_path_data(path_data):
    from svg.path import parse_path
    path = parse_path(path_data)
    return list(path)

def main():
    """
    Main function to create GUI window with file upload button
    """
    root = tk.Tk()
    root.title("SVG Path Processor")
    root.geometry("800x400")  # Set window size

    # Create and pack a frame to hold widgets
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True)

    # Create label for instructions
    label = tk.Label(frame, text="Click the button to select an SVG file")
    label.pack(pady=10)

    # Create result label
    result_label = tk.Label(frame, text="", wraplength=350)
    result_label.pack(pady=10)

    # Create upload button
    upload_button = tk.Button(
        frame,
        text="Select SVG File",
        command=lambda: select_file(result_label)
    )
    upload_button.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()