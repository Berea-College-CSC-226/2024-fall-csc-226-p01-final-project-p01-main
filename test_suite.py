from inspect import getframeinfo, stack
from main import *

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = f"Test at line {linenum} ok."
    else:
        msg = f"Test at line {linenum} FAILED."
    print(msg)

def face_recognition_test_suite():
    """
    Test suite for the face recognition system.
    :return: None
    """
    print("Testing get_encoded_faces()")
    unittest(type(get_encoded_faces()) is dict)  # Test if it returns a dictionary
    unittest(len(get_encoded_faces()) > 0)  # Assuming at least one face is encoded in './faces'

    print("\nTesting process_image_for_recognition()")
    try:
        # Case 1: Valid image with known faces
        test_image_valid = load_image("./test_known_faces.jpg")  # Replace with an image containing known faces
        result_valid = process_image_for_recognition(test_image_valid)
        unittest(type(result_valid) is list)
        unittest("Unknown" not in result_valid and len(result_valid) > 0)  # Should not contain "Unknown"

        # Case 2: Valid image with no known faces
        test_image_unknown = load_image("./test_unknown_faces.jpg")  # Replace with an image with no known faces
        result_unknown = process_image_for_recognition(test_image_unknown)
        unittest(type(result_unknown) is list)
        unittest("Unknown" in result_unknown or len(result_unknown) > 0)  # Should return at least "Unknown"

        # Case 3: Image file that doesn't exist
        try:
            invalid_image = load_image("./nonexistent.jpg")
            unittest(False)  # If no exception is raised, the test fails
        except ValueError:
            unittest(True)  # Expected behavior: raises ValueError

        # Case 4: Invalid file type
        try:
            invalid_file = load_image("./invalid_file.txt")  # Replace with an actual invalid file type
            unittest(False)  # If no exception is raised, the test fails
        except ValueError:
            unittest(True)  # Expected behavior: raises ValueError

    except Exception as e:
        print(f"Error during tests: {e}")
        unittest(False)

def database_test_suite():
    """
    Test suite for the database functions.
    :return: None
    """
    print("\nTesting load_database()")
    database = load_database()
    unittest(type(database) is dict)  # Test if it returns a dictionary

    print("\nTesting save_database() and add_face_song_mapping()")
    try:
        test_database = {}
        add_face_song_mapping(test_database, "test_face.jpg", "test_song.mp3")
        unittest("test_face.jpg" in test_database)
        unittest(test_database["test_face.jpg"] == "test_song.mp3")
    except Exception as e:
        print(f"Error during tests: {e}")
        unittest(False)

def main():
    print("Starting Face Recognition Test Suite")
    face_recognition_test_suite()
    print("\nStarting Database Test Suite")
    database_test_suite()

main()