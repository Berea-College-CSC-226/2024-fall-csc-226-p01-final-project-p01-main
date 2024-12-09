from inspect import getframeinfo, stack
from unittest.mock import patch
from main import *

def unittest(did_pass):
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    msg = f"Test at line {linenum} {'ok' if did_pass else 'FAILED'}."
    print(msg)

def face_recognition_test_suite():
    print("Testing get_encoded_faces()")
    unittest(type(get_encoded_faces()) is dict)

    print("\nTesting process_image_for_recognition()")
    try:
        test_image_valid = load_image("./test_known_faces.jpg")
        result_valid = process_image_for_recognition(test_image_valid)
        unittest(type(result_valid) is list)

        test_image_unknown = load_image("./test_unknown_faces.jpg")
        result_unknown = process_image_for_recognition(test_image_unknown)
        unittest("Unknown" in result_unknown)

        try:
            invalid_image = load_image("./nonexistent.jpg")
            unittest(False)
        except ValueError:
            unittest(True)

        try:
            invalid_file = load_image("./invalid_file.txt")
            unittest(False)
        except ValueError:
            unittest(True)

    except Exception as e:
        print(f"Error during tests: {e}")
        unittest(False)

def database_test_suite():
    print("\nTesting load_database()")
    database = load_database()
    unittest(type(database) is dict)

    print("\nTesting save_database() and add_face_song_mapping()")
    test_database = {}
    add_face_song_mapping(test_database, "test_face.jpg", "test_song.mp3")
    unittest("test_face.jpg" in test_database)
    unittest(test_database["test_face.jpg"] == "test_song.mp3")

def file_path_test_suite():
    print("\nTesting validate_file_path()")
    unittest(validate_file_path("./test_image.jpg") is False)

def main():
    print("Starting Test Suites")
    face_recognition_test_suite()
    database_test_suite()
    file_path_test_suite()

if __name__ == "__main__":
    main()
