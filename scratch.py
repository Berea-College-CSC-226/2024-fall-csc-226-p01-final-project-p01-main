import sqlite3

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

def creat_users_table():
    """
    Creates a table to set us the database - Should be only used once duing the lifetime of project
    :return: none
    """
    con = sqlite3.connect("registration.db")
    cursor = con.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Users (
        name CHAR NOT NULL,
        PIN INTEGER NOT NULL,
        id INTEGER PRIMARY KEY AUTOINCREMENT
    );
    '''

    cursor.execute(create_table_query)
    con.commit()


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