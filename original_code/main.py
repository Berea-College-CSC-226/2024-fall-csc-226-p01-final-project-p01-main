from flask import Flask
import sqlite3

class User:
    def __init__(self):
        self.name = self.retrieve_name()
        self.pin = self.retrieve_pin()
        self.con = sqlite3.connect("registration.db")
        self.cursor = self.con.cursor()


    def retrieve_name(self):
        self.cursor()
        return ""

    def retrieve_pin(self):
        return ""

    def add_course(self):
        pass

    def remove_course(self):
        pass

    def retrieve_course(self):
        pass
app = Flask(__name__)

def creat_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        pin INTEGER NOT NULL,
    )
    '''