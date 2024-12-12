

from flask import *
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

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Renders a form and sends it to the server"""

    # Still not complete
    if request.method == 'POST':
        name = request.form['name']
        pin = request.form['pin']
        crn = request.form['pin']
        id = request.args.get('id')
        # Process form data to database here
        #user = User(id)
        #user.add_course_through_crn(crn)
        return f"Form submitted! Name: {name}, PIN: {pin}"

    if request.method == 'GET':
        return render_template('student_form.html')


def retrieve_course_id_through_CRN(self, crn, testing=False):
    """
    Gets the od pf
    :param crn: course registration number
    :param testing: whether we are using the function for testing
    :return:
    """
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()

    # For testing
    if testing:
        crn = '1111'

    sql_query = "SELECT * FROM Courses WHERE crn = ?"
    cur.execute(sql_query, (crn,))
    course = cur.fetchall()[0]
    id = course[2]
    user = User(id)
    self.con.close()


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


