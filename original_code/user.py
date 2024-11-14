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
        self.cursor.execute("SELECT * FROM Users WHERE id = ?", (self.key,))
        self.data = self.cursor.fetchone() # Retrieves name, pin and id
        return self.data


    def add_course(self):
        """
        Add a course to the course list in the database
        :return: none
        """
        pass

    def remove_course(self):
        """
        Add a course to the course list in the database
        :return: none
        """
        pass

    def retrieve_course(self):
        """
        Get courses form the data bases
        :return:
        """
        # Implementation is to be changed
        self.cursor.execute("SELECT courses FROM Users WHERE id = ?", (self.key,))
        courses = self.cursor.fetchone()[0]
        return courses


    def close_connection(self):
        """
        Closes connection to the database
        :return:
        """
        self.con.close()


def creat_users_table():
    """
    Creates a table to set us the database - Should be only used once duing the lifetime of project
    :return: none
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    create_table_query = '''
    CREATE TABLE Users (
        name CHAR NOT NULL,
        PIN INTEGER NOT NULL,
        id INTEGER PRIMARY KEY AUTOINCREMENT
    );
    '''

    cursor.execute(create_table_query)
    con.commit()


def create_student(name, pin):
    """
    Create a student in the database and returns as a User object
    :param name: name of the student
    :param pin: pin of the student
    :return:
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
    Returns a list of all students
    :return: users: a list of all students
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

