####################################################
# Name: Besher Kitaz
# username: kitazb
#
# CSC: 226
#
####################################################
#
# testing suite for user module
# Inspired by: https://docs.google.com/document/d/1ww0ajH0ahH8wBKCp3uY6fe_THjE8BJZ_3iYgnOO8ovg/edit?tab=t.0#heading=h.qg98s23ap4mh
#
#
####################################################


from user import *
import sqlite3


con = sqlite3.connect('registration.db')
cursor = con.cursor()


def test_init(name, PIN):
    """
    initialize the database for tests
    :param name: name of the user
    :param PIN: PIN of the user
    :return: name, PIN, id
    """

    # Add a row in the table to use for testing; to be deleted later in every test function
    add_query = "INSERT INTO Users (name, PIN) VALUES (?, ?)"
    cursor.execute(add_query, (name, PIN))
    cursor.execute("SELECT * FROM Users ORDER BY id DESC LIMIT 1;")
    name, PIN, id = cursor.fetchone()
    con.commit()
    return name, PIN, id


def test_retrieve_data(name, pin):
    """
    test retrieve data function
    :param name: name of the user
    :param pin: pin of the user
    :return:
    """
    name, crn, pin = test_init( name, pin)
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
    """
    tests the create user function
    :param name: name of the user
    :param pin: pin of the user
    :return:
    """
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


print("All tests passed for users")
con.close()

