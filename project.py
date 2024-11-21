######################################################################
# Author: Galina Pokitko
# Username: pokitkog
#
# Purpose: ????
#
# CHANGE THIS "A GUI widget is a graphical component such as a button, text label as shown below.
# GUI widgets also exist to make drop-down menus and scroll bars, display images, etc...
# Tkinter gives you the ability to create GUI Windows containing widgets.
# This program is a simple exploration."
#######################################################################
# Acknowledgements: ?????
#
####################################################################################
import tkinter as tk
import sqlite3

con = sqlite3.connect("project.db")
cur = con.cursor()


# res = cur.execute("SELECT FirstName FROM User")
# print(res.fetchall())
# res2 = cur.execute("SELECT * FROM User")
# print(res2.fetchall())
#
# res3 = cur.execute("SELECT LastName FROM User")
# print(res3.fetchall())

for row in cur.execute("SELECT LastName, FirstName FROM User ORDER BY LastName"):
    print(row)

for row in cur.execute("SELECT LastName, LastName FROM User ORDER BY LastName"):
    print(row)

#SELECT year, title FROM movie ORDER BY year


class LibraryCatalog:
    def __init__(self, file_path, windowtext="Library Catalog"):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """

        self.root = tk.Tk()  # Create the root window where all widgets go
        self.root.minsize(width=250, height=100)  # Sets the window's minimum size
        self.root.maxsize(width=300, height=150)  # Sets the window's maximum size
        self.root.title(windowtext)  # Sets root window title

        #TO-DO:  self.file_path to store the file path for loading and saving data



    def add_book(self, book):
        pass

    def search_by_author(self, author_name):
        pass

    def search_by_genre(self, genre_name):
        pass

    def recommend_book(self, genre=None):
        pass

    def load_catalog(self):
        pass

    def save_catalog(self):
        pass


class Book:
    def __init__(self, title, author, genre, status):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """

    def update_status(self, new_status):
        pass

    def get_info(self):
        pass


class LibraryApp:
    def __init__(self, catalog):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """


    def display_books(self, books):
        pass

    def search_books(self):
        pass

    def add_book_gui(self):
        pass

    def recommend_book_gui(self):
        pass

    def save_and_exit(self):
        pass




def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    pass


if __name__ == "__main__":
    main()
