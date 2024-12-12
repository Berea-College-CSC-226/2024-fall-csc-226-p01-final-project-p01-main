
from user import *
import sqlite3


con = sqlite3.connect('registration.db')
cursor = con.cursor()


def test_init(name, PIN):
    add_query = "INSERT INTO Users (name, PIN) VALUES (?, ?)"
    cursor.execute(add_query, (name, PIN))
    cursor.execute("SELECT * FROM Users ORDER BY id DESC LIMIT 1;")
    name, PIN, id = cursor.fetchone()
    con.commit()
    return name, PIN, id


def test_retrieve_data(name, crn):
    name, crn, id = test_init( name, crn)
    user = User(id)
    data = user.retrieve_data()
    assert user.key == id
    assert len(data) == 3
    assert type(data) == tuple
    assert type(data[0]) == str
    assert type(data[1]) == int
    assert type(data[2]) == int
    cursor.execute("DELETE FROM Users WHERE id = ?;", (id,))
    con.commit()


def test_create_user(name, pin):
    user = create_student(name, pin)
    assert user.pin == pin
    assert user.name == name
    assert type(user) == User
    cursor.execute("DELETE FROM Users WHERE id = ?;", (user.key,))
    con.commit()


test_retrieve_data('Sam', 1111)
test_retrieve_data('Max', 1112)
test_retrieve_data('Alex', 1113)

test_create_user('John', 1111)
test_create_user('Scott', 1112)
test_create_user('James', 1113)


print("All tests passed for courses")
con.close()

