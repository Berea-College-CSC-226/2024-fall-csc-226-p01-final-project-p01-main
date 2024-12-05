
import sqlite3
from courses import Course
from user import User
from courses import retrieve_course_through_CRN

class StudentCourses:
    def __init__(self):
        pass


def create_user_courses_table():
    """
    Creates a table with foreign keys for many-to-many relationship medium table
    :return:
    """

    query = """CREATE TABLE User_Courses (
            user_id INTEGER,
            course_id INTEGER,
            PRIMARY KEY (user_id,course_id),
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    ) """


