####################################################
# Name: Besher Kitaz
# username: kitazb
#
# CSC: 226
#
####################################################
#
#
# Inspired by: https://docs.google.com/document/d/1ww0ajH0ahH8wBKCp3uY6fe_THjE8BJZ_3iYgnOO8ovg/edit?tab=t.0#heading=h.qg98s23ap4mh
#
#
####################################################


import sqlite3
from types import NoneType

from werkzeug.exceptions import NotFound


class User:

    def __init__(self, key):
        """
        Creates an Object that relates to a record in the Users database.
        :param key: The key or id of the user in the database
        """
        self.con = sqlite3.connect("registration.db")
        self.cursor = self.con.cursor()
        self.key = key
        self.name = self.retrieve_data()[0] # Retrieves the name form the database
        self.pin = self.retrieve_data()[1] # Retrieves the PIN number form the database
        self.close_connection()


    def retrieve_data(self):
        """
        Retrieves the data from the database for the user
        :return: A Tuple of the user data from the record
        """
        self.create_connection()
        self.cursor.execute("SELECT * FROM Users WHERE id = ?", (self.key,))
        self.data = self.cursor.fetchone() # Retrieves name, pin and id
        self.close_connection()
        return self.data

    def retrieve_courses(self, user_id):
        """
        Retrieves a list of courses for a specific user from the database
        :param user_id: The ID of the user
        :return: a list of courses
        """
        con = sqlite3.connect("registration.db")
        cursor = con.cursor()

        sql_query = """
        SELECT Courses.name
        FROM Courses
        JOIN User_Courses ON Courses.id = User_Courses.course_id
        JOIN Users ON Users.id = User_Courses.user_id
        WHERE Users.id = ?
        """

        cursor.execute(sql_query, (user_id,))
        courses = cursor.fetchall()
        return courses


    def close_connection(self):
        """
        Closes connection to the database
        :return:
        """
        self.con.close()


    def create_connection(self):
        self.con = sqlite3.connect("registration.db")
        self.cur = self.con.cursor()

    def add_course_through_crn(self, crn):
        """
        Adds a course to a student through CRN and the id of the student
        :param crn:
        :return:
        """
        con = sqlite3.connect('registration.db')
        cur = con.cursor()
        # Retrieve Course id using CRN:
        retrieve_query = "SELECT id FROM Courses WHERE crn = ?"

        cur.execute(retrieve_query, (crn,))
        course_id = cur.fetchone()[0]


        query = "INSERT INTO User_Courses (user_id, course_id) VALUES (?, ?);"
        cur.execute(query, (self.key, course_id))
        con.commit()
        con.close()



def create_student(name, pin):
    """
    Create a student in the database and returns as a User object
    :param name: name of the student
    :param pin: pin of the student
    :return: A User object
    """
    # Create connection to the database
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()

    # Insert the data in the base and commit changes
    sql_query = "INSERT INTO Users (name, pin) VALUES (?, ?)"
    cursor.execute(sql_query, (name, pin))
    con.commit()

    # Retreive the data (the last inserted) to return as an object
    cursor.execute("SELECT * FROM Users ORDER BY id DESC LIMIT 1;")
    name, pin, id = cursor.fetchone()

    # Create an object with the data
    user = User(id)
    con.close()
    return user


def students_list():
    """
    Gets a list of users from the database
    :return: a list of users
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    sql_query = "SELECT * FROM Users ORDER BY id;"
    cursor.execute(sql_query)
    users = cursor.fetchall()
    con.close()
    return users


def delete_all():
    """
    Clear the database - for development purposes
    :return:
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    sql_query = "DELETE FROM Users"
    cursor.execute(sql_query)
    con.commit()
    con.close()


if __name__ == "__main__":
    create_student("Besher", 111)
    create_student("Joshua", 112)
    create_student("Jose", 113)

