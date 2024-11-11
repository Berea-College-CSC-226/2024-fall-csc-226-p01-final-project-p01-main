from flask import Flask
import sqlite3

class User:
    def __init__(self):
        self.name = self.retrieve_name()
        self.pin = self.retrieve_pin()

    def retrieve_name(self):
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