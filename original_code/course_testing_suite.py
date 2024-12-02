import os
from courses import *
import sqlite3

# Had to get some help from ChatGPT for the nest three lines


def test_create_course():
    course = create_course("Math 101", 12345)
    assert course.name == "Math 101"
    assert course.crn == 12345
    assert course.key == 1
    assert type(course) == Course
    print("test_create_course passed.")


def test_course_list():
    delete_all()
    create_course("Math 101", 12345)
    create_course("Science 101", 67890)
    courses = course_list()
    assert len(courses) == 2
    assert courses[0][0] == "Math 101"
    assert courses[1][0] == "Science 101"
    print("test_course_list passed.")


def test_delete_all():
    delete_all()
    create_course("Math 101", 12345)
    create_course("Science 101", 67890)
    delete_all()
    courses = course_list()
    assert len(courses) == 0
    print("test_delete_all passed.")


def test_retrieve_data():
    delete_all()
    course = create_course("Math 101", 12345)
    data = course.retrieve_data()
    assert data[0] == "Math 101"
    assert data[1] == 12345
    print("test_retrieve_data passed.")



# Run the tests
if __name__ == "__main__":
    test_create_course()
    test_course_list()
    test_delete_all()
    test_retrieve_data()

    print("All tests passed.")