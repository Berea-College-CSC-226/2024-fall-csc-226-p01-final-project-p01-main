
from courses import *
import sqlite3


con = sqlite3.connect('registration.db')
cursor = con.cursor()


def test_init(name, crn):
    add_query = "INSERT INTO Courses (name, crn) VALUES (?, ?)"
    cursor.execute(add_query, (name, crn))
    cursor.execute("SELECT * FROM Courses ORDER BY id DESC LIMIT 1;")
    name, crn, id = cursor.fetchone()
    con.commit()
    return name, crn, id


def test_retrieve_data(name, crn):
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

