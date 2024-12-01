


class StudentCourses:
    def __init__(self):
        pass

from courses import retrieve_course_through_CRN
from user import User

import sqlite3

def add_course_to_student_through_CRN(student_id, crn):
    con = sqlite3.connect('registration.db')
    cur = con.cursor()

    course = retrieve_course_through_CRN(crn)

    query = "INSERT INTO StudentCourses (student_id, course_id) VALUES (?, ?);"
    cur.execute(query, (student_id, course.id))

    con.commit()
    con.close()