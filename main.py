import os
import cv2
import json
import pygame
import face_recognition as fr
import numpy as np

DEFAULT_IMAGE_FOLDER = os.path.join(os.getcwd(), "face-recognition-master")
DATABASE_FILE = os.path.join(os.getcwd(), "face_song_mapping.json")


class ImageHandler:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def prompt_file_path(self):
        file_name = input("Enter the image file name (e.g., obama.jpg): ")
        file_path = os.path.join(self.folder_path, file_name)
        print(f"Using path: {file_path}")
        return file_path

    @staticmethod
    def validate_file_path(file_path):
        if not os.path.exists(file_path):
            return False
        if not file_path.lower().endswith((".jpg", ".jpeg", ".png")):
            return False
        return True

    @staticmethod
    def handle_invalid_file_path():
        print("Invalid file path. Please enter a valid image file.")

    def load_image(self, file_path):
        if not self.validate_file_path(file_path):
            raise ValueError(f"Invalid image file path: {file_path}")
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Image at {file_path} could not be loaded.")
        return image


class FaceRecognition:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.encoded_faces = self.get_encoded_faces()

    def get_encoded_faces(self):
        encoded = {}
        for dirpath, _, filenames in os.walk(self.image_folder):
            for f in filenames:
                if f.lower().endswith((".jpg", ".png")):
                    face = fr.load_image_file(os.path.join(dirpath, f))
                    encoding = fr.face_encodings(face)
                    if encoding:
                        encoded[f.split(".")[0]] = encoding[0]
        return encoded

    def process_image_for_recognition(self, image):
        faces_encoded = list(self.encoded_faces.values())
        known_face_names = list(self.encoded_faces.keys())

        face_locations = fr.face_locations(image)
        face_encodings = fr.face_encodings(image, face_locations)

        recognized_faces = []
        for face_encoding in face_encodings:
            matches = fr.compare_faces(faces_encoded, face_encoding)
            name = "Unknown"  # Default to Unknown if no match

            # Use the closest match if any match exists
            face_distances = fr.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:  # If there is a match, use the name
                name = known_face_names[best_match_index]

            recognized_faces.append(name)

        # Annotate the image with rectangles and names
        for (top, right, bottom, left), name in zip(face_locations, recognized_faces):
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(image, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        # Show the image
        cv2.imshow('Recognized Faces', image)
        cv2.waitKey(0)  # Wait until a key is pressed
        cv2.destroyAllWindows()  # Close the window after key press

        return recognized_faces


class MusicPlayer:
    @staticmethod
    def play_song(song_path):
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
    def __init__(self, file_path):
        self.file_path = file_path
        self.database = self.load_database()

    def load_database(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Database file not found. Creating a new one.")
            return {}

    def save_database(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.database, file, indent=4)

    def add_face_song_mapping(self, face_path, song_path):
        self.database[face_path] = song_path
        self.save_database()


class FaceSongMapping:
    def __init__(self, database_file, image_folder):
        self.database_manager = DatabaseManager(database_file)
        self.face_recognition = FaceRecognition(image_folder)
        self.image_handler = ImageHandler(image_folder)

    def add_new_mapping(self):
        new_face = input("Enter the path to the new face image: ")
        new_song = input("Enter the path to the corresponding song: ")
        self.database_manager.add_face_song_mapping(new_face, new_song)
        print("New mapping added successfully.")

    def play_matching_song(self, recognized_faces):
        for face_name in recognized_faces:
            if face_name in self.database_manager.database:
                print(f"Playing song for {face_name}: {self.database_manager.database[face_name]}")
                MusicPlayer.play_song(self.database_manager.database[face_name])
            else:
                print(f"No song associated with {face_name}.")


def main():
    face_song_mapping = FaceSongMapping(DATABASE_FILE, DEFAULT_IMAGE_FOLDER)

    while True:
        file_path = face_song_mapping.image_handler.prompt_file_path()
        if face_song_mapping.image_handler.validate_file_path(file_path):
            break
        face_song_mapping.image_handler.handle_invalid_file_path()

    image = face_song_mapping.image_handler.load_image(file_path)
    recognized_faces = face_song_mapping.face_recognition.process_image_for_recognition(image)

    face_song_mapping.play_matching_song(recognized_faces)

    if input("Do you want to add a new face-song mapping? (y/n): ").lower() == 'y':
        face_song_mapping.add_new_mapping()


if __name__ == "__main__":
    main()
