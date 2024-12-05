import os
import cv2
import json
import pygame
import face_recognition as fr
import numpy as np

# Subtask I: File Path and Image Validation
def prompt_file_path():
    """Prompt the user to input a file path."""
    return input("Enter the file path to the image: ")

def validate_file_path(file_path):
    """Check if the file path exists and if the file is an image."""
    if not os.path.exists(file_path):
        return False
    if not file_path.lower().endswith((".jpg", ".jpeg", ".png")):
        return False
    return True

def handle_invalid_file_path():
    """Handle the case where the file path is invalid."""
    print("Invalid file path. Please enter a valid image file.")

def load_image(file_path):
    """Load the image using OpenCV."""
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError(f"Image at {file_path} could not be loaded.")
    return image

# Subtask II: Face Recognition and Song Playback
def get_encoded_faces():
    """
    Encodes all the faces stored in the './faces' folder.
    :return: dictionary with names as keys and encoded faces as values
    """
    encoded = {}

    for dirpath, _, filenames in os.walk("./faces"):
        for f in filenames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file(os.path.join(dirpath, f))
                encoding = fr.face_encodings(face)
                if encoding:  # Ensure there is at least one encoding
                    encoded[f.split(".")[0]] = encoding[0]

    return encoded

def process_image_for_recognition(image):
    """Process the input image for facial recognition."""
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    face_locations = fr.face_locations(image)
    face_encodings = fr.face_encodings(image, face_locations)

    recognized_faces = []
    for face_encoding in face_encodings:
        matches = fr.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # Use the closest match if any match exists
        face_distances = fr.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        recognized_faces.append(name)

    # Annotate the image with rectangles and names
    for (top, right, bottom, left), name in zip(face_locations, recognized_faces):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(image, (left, bottom - 25), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('Recognized Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return recognized_faces

def play_song(song_path):
    """Play the song using Pygame."""
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

# Subtask III: Database Management
def load_database(file_path="face_song_mapping.json"):
    """Load the face-song mapping database."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Database file not found. Creating a new one.")
        return {}

def save_database(database, file_path="face_song_mapping.json"):
    """Save the face-song mapping database."""
    with open(file_path, 'w') as file:
        json.dump(database, file, indent=4)

def add_face_song_mapping(database, face_path, song_path):
    """Add a new face-song mapping to the database."""
    database[face_path] = song_path
    save_database(database)

def main():
    """Main function to execute the project workflow."""
    database = load_database()

    # Step 1: Get file path and validate
    while True:
        file_path = prompt_file_path()
        if validate_file_path(file_path):
            break
        handle_invalid_file_path()

    # Step 2: Load image and process face recognition
    image = load_image(file_path)
    recognized_faces = process_image_for_recognition(image)

    # Step 3: Handle recognized faces
    for face_name in recognized_faces:
        if face_name in database:
            print(f"Playing song for {face_name}: {database[face_name]}")
            play_song(database[face_name])
        else:
            print(f"No song associated with {face_name}.")

    # Step 4: Option to add new mapping
    add_new_mapping = input("Do you want to add a new face-song mapping? (y/n): ").lower()
    if add_new_mapping == 'y':
        new_face = input("Enter the path to the new face image: ")
        new_song = input("Enter the path to the corresponding song: ")
        add_face_song_mapping(database, new_face, new_song)
        print("New mapping added successfully.")

if __name__ == "__main__":
    main()
