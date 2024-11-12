import sqlite3
from flask import Flask, render_template, request


def creat_users_table():
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

class User:

    def __init__(self, key):
        self.con = sqlite3.connect("registration.db")
        self.cursor = self.con.cursor()
        self.key = key
        self.name = self.retrieve_data()[0]
        self.pin = self.retrieve_data()[1]
        self.close_connection()


    def retrieve_data(self):
        self.cursor.execute("SELECT * FROM Users WHERE id = ?", (self.key,))
        self.data = self.cursor.fetchone() # Retrieves name, pin and id
        return self.data


    def add_course(self):
        pass

    def remove_course(self):
        pass

    def retrieve_course(self):
        self.cursor.execute("SELECT courses FROM Users WHERE id = ?", (self.key,))
        courses = self.cursor.fetchone()[0]
        return courses


    def close_connection(self):
        self.con.close()


def create_student(name, pin):

    con = sqlite3.connect("registration.db")
    cursor = con.cursor()
    sql_query = "INSERT INTO Users (name, pin) VALUES (?, ?)"
    cursor.execute(sql_query, (name, pin))
    con.commit()
    cursor.execute("SELECT * FROM Users ORDER BY id DESC LIMIT 1;")
    name, pin, id = cursor.fetchone()
    user = User(id)

    return user


u1 = create_student("Besher", "1223")

app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        pin = request.form['pin']
        # Process form data to database here

        print(name, pin) # For testing; to be removed

        return f"Form submitted! Name: {name}, PIN: {pin}"

    return render_template('student_form.html')

app.run(debug=True)
