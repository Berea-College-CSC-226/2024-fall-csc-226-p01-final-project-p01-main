######################################################################
# Author: Eber Seco Lima
# Username: secolimae
#
# Assignment: P01: Final Project
#
# Purpose: To implement a face-song mapping system. It combines facial recognition with music
# playback functionality, allowing a system to recognize faces from an image, play corresponding
# songs based on the recognized faces, and manage face-song associations in a database.
#
######################################################################
# Acknowledgements:
#   Original Author: Tech with Tim, Code Snail
#   Ideas from: https://www.youtube.com/watch?v=D5xqcGk6LEc
#   - https://www.theinsaneapp.com/2021/06/list-of-python-projects-with-source-code-and-tutorials.html
#   - https://github.com/techwithtim/Face-Recognition
#   - https://stackoverflow.com/questions/6356749/music-analysis-and-visualization
#   - https://chatgpt.com/share/675c592f-da38-8009-97c5-5656af5b1fd2
#   - https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
#   - https://docs.opencv.org/4.x/da/d60/tutorial_face_main.html
#   - https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html
#   - https://docs.python.org/3/library/os.path.html
#   - https://chatgpt.com/share/675c5a0c-afa0-8009-8124-541c47018304
#   - https://stackoverflow.com/questions/63805195/what-is-static-method-in-python
#   - https://www.geeksforgeeks.org/os-walk-python/
#   - https://www.javatpoint.com/os-walk-in-python
#   - https://face-recognition.readthedocs.io/en/latest/face_recognition.html
#   - https://face-recognition.readthedocs.io/en/latest/readme.html#features
#   - https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py
#   - https://chatgpt.com/share/675c607e-6a40-800c-97a3-e8485f161c20
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import os
import cv2
import json
import pygame
import face_recognition as fr
import numpy as np

# File paths to folders
DEFAULT_IMAGE_FOLDER = os.path.join(os.getcwd(), "face-recognition-master")
DATABASE_FILE = os.path.join(os.getcwd(), "face_song_mapping.json")

class ImageHandler:
    """Handles image-related operations such as loading and validating files."""

    def __init__(self, folder_path):
        """Initializes the ImageHandler with a folder path.

        Args:
            folder_path (str): Path to the folder containing images.
        """
        self.folder_path = folder_path

    def prompt_file_path(self):
        """Prompts the user to enter an image file name and constructs its path.

        Returns:
            str: Full path of the specified image file.
        """
        file_name = input("Enter the image file name (e.g., test.jpg): ")
        file_path = os.path.join(self.folder_path, file_name)
        print(f"Using path: {file_path}")
        return file_path

    @staticmethod
    # This @staticmethod decorator allow methods to not take self as its first argument, making it
    # independent of the class instance. It can be called directly on the class itself or through an
    # instance, but it does not need an instance to be called.
    def validate_file_path(file_path):
        """Validates if the given file path exists and has a supported extension.

        Args:
            file_path (str): Path to the image file.

        Returns:
            bool: True if the file path is valid, False otherwise.
        """
        if not os.path.exists(file_path):
            return False
        if not file_path.lower().endswith((".jpg", ".jpeg", ".png")):
            return False
        return True

    @staticmethod
    def handle_invalid_file_path():
        """Displays an error message for an invalid file path."""
        print("Invalid file path. Please enter a valid image file.")

    def load_image(self, file_path):
        """Loads an image from a specified file path.

        Args:
            file_path (str): Path to the image file.

        Returns:
            numpy.ndarray: Loaded image.

        Raises:
            ValueError: If the image file path is invalid or the image cannot be loaded.
        """
        if not self.validate_file_path(file_path):
            raise ValueError(f"Invalid image file path: {file_path}")
        image = cv2.imread(file_path) # Reads the image from the given path
        if image is None:
            raise ValueError(f"Image at {file_path} could not be loaded.")
        return image


class FaceRecognition:
    """Performs face recognition operations on images."""

    def __init__(self, image_folder):
        """Initializes FaceRecognition with a folder of known faces.

        Args:
            image_folder (str): Path to the folder containing face images.
        """
        self.image_folder = image_folder
        self.encoded_faces = self.get_encoded_faces()

    def get_encoded_faces(self):
        """Encodes known face images from the specified folder.

        Returns:
            dict: Dictionary of face names and their encodings.
        """
        encoded = {}
        for dirpath, _, filenames in os.walk(self.image_folder):
            # Iterates over each directory and its files within self.image_folder
            # Skips processing subdirectory names (_ is used as a placeholder).
            # Processes the file names in filenames.
            for f in filenames:
                if f.lower().endswith((".jpg", ".png")):
                    face = fr.load_image_file(os.path.join(dirpath, f))
                    # Combines the directory path dirpath and file name f
                    # Loads the image file from the constructed path into memory.
                    # The loaded image is typically returned as a NumPy array representing pixel
                    # data.
                    encoding = fr.face_encodings(face)
                    if encoding:
                        encoded[f.split(".")[0]] = encoding[0]
        return encoded

    def process_image_for_recognition(self, image):
        """Perform face recognition on an image, identify recognized faces, annotate
        them, and display the results.

        Args:
            image (numpy.ndarray): Image to process.

        Returns:
            list: Names of recognized faces.
        """

        # Match recognized faces with stored names
        faces_encoded = list(self.encoded_faces.values())
        known_face_names = list(self.encoded_faces.keys())

        # Identifies where faces are located in the image and extract numerical
        # representations (encodings) used to compare faces for recognition.
        face_locations = fr.face_locations(image)
        face_encodings = fr.face_encodings(image, face_locations)

        recognized_faces = []
        for face_encoding in face_encodings:
            matches = fr.compare_faces(faces_encoded, face_encoding)
            name = "Unknown"

            face_distances = fr.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances) # Returns the index of the smallest
            # distance, indicating the closest match.

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            recognized_faces.append(name)

        # This loop iterates over each recognized face and its location
        for (top, right, bottom, left), name in zip(face_locations, recognized_faces):
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2) # Draws rectangle
            cv2.rectangle(image, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        # Opens a window displaying the image with the recognized faces
        cv2.imshow('Recognized Faces', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return recognized_faces


class MusicPlayer:
    """
    Handles music playback using the Pygame library.
    """

    @staticmethod
    def play_song(song_path):
        """
        Plays a song from the given file path.

        Args:
            song_path (str): The path to the song file.
        """
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()

            print("Press 'p' to pause")
            print("Press 'r' to resume")
            print("Press 'v' to adjust volume")
            print("Press 'e' to exit")
            while True:
                command = input("['p', 'r', 'v', 'e'] >>> ")
                if command == 'p':
                    pygame.mixer.music.pause()
                elif command == 'r':
                    pygame.mixer.music.unpause()
                elif command == 'v':
                    volume = float(input("Enter volume (0 to 1): "))
                    pygame.mixer.music.set_volume(volume)
                elif command == 'e':
                    pygame.mixer.music.stop()
                    break
        except Exception as e:
            print(f"Error playing song: {e}")


class DatabaseManager:
    """
    Manages a face-song mapping database stored in a JSON file.
    """

    def __init__(self, file_path):
        """
        Initializes the database manager with the given file path.

        Args:
            file_path (str): The path to the database file.
        """
        self.file_path = file_path
        self.database = self.load_database()

    def load_database(self):
        """
        Loads the database from the JSON file.

        Returns:
            dict: The loaded database.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Database file not found. Creating a new one.")
            return {}

    def save_database(self):
        """
        Saves the current database to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.database, file, indent=4)

    def add_face_song_mapping(self, face_path, song_path):
        """
        Adds a new face-song mapping to the database.

        Args:
            face_path (str): The path to the face image.
            song_path (str): The path to the corresponding song.
        """
        self.database[face_path] = song_path
        self.save_database()


class FaceSongMapping:
    """
    Handles face-song mapping, including database management and song playback.
    """

    def __init__(self, database_file, image_folder):
        """
        Initializes face-song mapping components.

        Args:
            database_file (str): Path to the database file.
            image_folder (str): Path to the image folder.
        """
        self.database_manager = DatabaseManager(database_file)
        self.face_recognition = FaceRecognition(image_folder)
        self.image_handler = ImageHandler(image_folder)

    def add_new_mapping(self):
        """
        Adds a new face-song mapping through user input.
        """
        new_face = input("Enter the path to the new face image (e.g., Scott Heggen): ")
        new_song = input("Enter the path to the corresponding song (e.g., music1.mp3): ")
        face_id = new_face.split(".")[0]  # Extract ID from filename (modify if needed)
        self.database_manager.add_face_song_mapping(face_id, new_song)
        print("New mapping added successfully.")

    def play_matching_song(self, recognized_faces):
        """
        Plays songs corresponding to recognized faces.

        Args:
            recognized_faces (list): List of recognized face IDs.
        """
        for face_id in recognized_faces:
            if face_id in self.database_manager.database:
                relative_song_path = self.database_manager.database[face_id]

                music_folder = os.path.dirname(DATABASE_FILE)
                absolute_song_path = os.path.join(music_folder, "music", relative_song_path)

                try:
                    MusicPlayer.play_song(absolute_song_path)
                    print(f"Playing song for {face_id}: {absolute_song_path}")
                except Exception as e:
                    print(f"Error playing song for {face_id}: {e}")
            else:
                print(f"No song associated with {face_id}.")


def main():
    """
    Initializes and runs the face-song mapping system.
    """
    face_song_mapping = FaceSongMapping(DATABASE_FILE, DEFAULT_IMAGE_FOLDER)

    while True:
        file_path = face_song_mapping.image_handler.prompt_file_path()
        if face_song_mapping.image_handler.validate_file_path(file_path):
            break
        face_song_mapping.image_handler.handle_invalid_file_path()

    # This line loads the image from the file path
    image = face_song_mapping.image_handler.load_image(file_path)
    # Processes the image to detect and recognize faces within the image
    recognized_faces = face_song_mapping.face_recognition.process_image_for_recognition(image)

    # The system plays a song that corresponds to the identified face using the
    # play_matching_song() method.
    face_song_mapping.play_matching_song(recognized_faces)

    if input("Do you want to add a new face-song mapping? (y/n): ").lower() == 'y':
        face_song_mapping.add_new_mapping()


if __name__ == "__main__":
    main()
