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

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

class Config:
    """
    Configuration for the Flask app.
    """
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'svg'}
    DEBUG = True

class SVGApp:
    """
    A class-based Flask application.
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        os.makedirs(self.app.config['UPLOAD_FOLDER'], exist_ok=True)
        self.add_routes()

    def allowed_file(self, filename):
        """
        Check if the file extension is allowed.
        """
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.app.config['ALLOWED_EXTENSIONS']

    def add_routes(self):
        """
        Define routes for the application.
        """
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/upload', 'upload_file', self.upload_file, methods=['POST'])
        self.app.add_url_rule('/uploads/<filename>', 'display_file', self.display_file)
        self.app.add_url_rule('/files/<filename>', 'serve_file', self.serve_file)

    def index(self):
        """
        Render the home page.
        """
        return render_template('index.html')

    def upload_file(self):
        """
        Handle file upload.
        """
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('display_file', filename=filename))
        return "Invalid file type", 400

    def display_file(self, filename):
        """
        Display the uploaded file.
        """
        return render_template('display.html', filename=filename)

    def serve_file(self, filename):
        """
        Serve the file from the upload folder.
        """
        return send_from_directory(self.app.config['UPLOAD_FOLDER'], filename)

    def run(self):
        self.app.run()



# class Process_image():
#     """
#     A class-based processing of the image to the <paths> tags .
#     """




if __name__ == '__main__':
    app = SVGApp()
    app.run()
