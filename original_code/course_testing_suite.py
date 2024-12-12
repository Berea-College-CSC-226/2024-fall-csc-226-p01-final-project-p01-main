####################################################
# Name: Besher Kitaz
# username: kitazb
#
# CSC: 226
#
####################################################
#
# testing suite for course module
# Inspired by: https://docs.google.com/document/d/1ww0ajH0ahH8wBKCp3uY6fe_THjE8BJZ_3iYgnOO8ovg/edit?tab=t.0#heading=h.qg98s23ap4mh
#
#
####################################################

from courses import *
import sqlite3


con = sqlite3.connect('registration.db')
cursor = con.cursor()


def test_init(name, crn):
    """
    initialize the database for tests
    :param name: name of the course
    :param crn: crn of the course
    :return: name, crn, id
    """
    # Add a row in the table to use for testing; to be deleted later in every test function
    add_query = "INSERT INTO Courses (name, crn) VALUES (?, ?)"
    cursor.execute(add_query, (name, crn))
    cursor.execute("SELECT * FROM Courses ORDER BY id DESC LIMIT 1;")
    name, crn, id = cursor.fetchone()
    con.commit()
    return name, crn, id


def test_retrieve_data(name, crn):
    """
     test retrieve data function
     :param name: name of the user
     :param crn: crn of the user
     :return:
     """
    name, crn, id = test_init( name, crn)
    course = Course(id)
    data = course.retrieve_data()
    assert course.key == id
    assert len(data) == 3
    assert type(data) == tuple
    assert type(data[0]) == str
    assert type(data[1]) == int
    assert type(data[2]) == int
    cursor.execute("DELETE FROM Courses WHERE id = ?;", (id,))
    con.commit()

def test_create_course(name, crn):
    """
    testing for create course function
    :param name: name of the course
    :param crn: crn for the course
    :return:
    """
    course = create_course(name, crn)
    assert course.crn == crn
    assert course.name == name
    assert type(course) == Course
    cursor.execute("DELETE FROM Courses WHERE id = ?;", (course.key,))
    con.commit()

test_retrieve_data('math', 1111)
test_retrieve_data('English', 1112)
test_retrieve_data('Physics', 1113)

test_create_course('math', 1111)
test_create_course('English', 1112)
test_create_course('Physics', 1113)


print("All tests passed for courses")
con.close()

