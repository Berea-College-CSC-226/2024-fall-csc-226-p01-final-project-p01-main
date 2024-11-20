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


class Course:

    def __init__(self, key):
        """
        Creates an Object that relates to a record in the Users database.
        :param key: The key or id of the user in the database
        """
        self.con = sqlite3.connect("registration.db")
        self.cursor = self.con.cursor()
        self.key = key
        self.name = self.retrieve_data()[0]  # Retrieves the name form the database
        self.crn = self.retrieve_data()[1] # Retrieves the crn form the database
        self.close_connection()


    def retrieve_data(self):
        """
        Retrieves the data from the database for the user
        :return: A Tuple of the user data from the record
        """
        print(self.key, "In retrieve data")
        self.cursor.execute("SELECT * FROM Courses WHERE id = ?", (self.key,))
        self.data = self.cursor.fetchone() # Retrieves name, crn and id
        return self.data


    def close_connection(self):
        """
        Closes connection to the database
        :return:
        """
        self.con.close()


def creat_courses_table():
    """
    Creates a table to set us the database - Should be only used once duing the lifetime of project
    :return: none
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    create_table_query = '''
    CREATE TABLE Courses (
        name CHAR NOT NULL,
        CRN INTEGER NOT NULL,
        id INTEGER PRIMARY KEY AUTOINCREMENT
    );
    '''

    cursor.execute(create_table_query)
    con.commit()


def course_list():
    """
    Returns a list of all students
    :return: users: a list of all students
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    sql_query = "SELECT * FROM Courses ORDER BY id;"
    cursor.execute(sql_query)
    users = cursor.fetchall()
    con.close()
    return users


def delete_all():
    """
    Clear the table - for development purposes
    :return:
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    delete_query = "DELETE FROM Courses"
    cursor.execute(delete_query)
    con.commit()
    con.close()

def create_course(name, crn):
    """
    Create a course in the database and returns as a Course object
    :param name: name of the course
    :param crn: crn of the course
    :return: a Course Object
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    add_query = "INSERT INTO Courses (name, crn) VALUES (?, ?)"
    cursor.execute(add_query, (name, crn))
    con.commit()
    cursor.execute("SELECT * FROM Courses ORDER BY id DESC LIMIT 1;")
    name, crn, id = cursor.fetchone()
    print(id, "in create course")
    course = Course(id)
    con.commit()
    con.close()
    return course


print(course_list())