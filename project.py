######################################################################
# Author: Galina Pokitko
# Username: pokitkog
#
# Purpose: Allow the User to explore and search for books in the database
# using a GUI interface.
#
# This program uses Tkinter to create a graphical user interface (GUI)
# that allows users to search for books by author in the catalog. It
# demonstrates the functionality of GUI widgets, including buttons, text
# labels, and other such components.
#######################################################################
# Acknowledgements:
#
# Inspired by Goodreads: https://www.goodreads.com/
# Book databases information: https://www.db2tutorial.com/getting-started/db2-sample-database/
# Sqlite tutorial by Corey Schafer: https://www.youtube.com/watch?v=pd-0G0MigUA&ab_channel=CoreySchafer
# Libraries used: https://docs.python.org/3/library/sqlite3.html#tutorial and https://docs.python.org/3/library/tkinter.html
# Introduction to tkinter with sqlite: https://www.youtube.com/watch?v=gdDI_GhIRGo&ab_channel=CodeFirstwithHala
# Overview of DB Browser: https://datacarpentry.github.io/sql-socialsci/02-db-browser.html
# Retrieving sqlite data: https://stackoverflow.com/questions/63235485/python-tinker-sqlite3-retrieve-data-and-show-on-tkinter-gui
# Importing CSV file to Sqlite DB Browser: https://www.youtube.com/watch?v=TOqI-KiTBKU&ab_channel=Anujshah
# Borrowed some ideas from CodersLegacy for Python SQLite3 with Tkinter GUI: https://www.youtube.com/watch?v=K8RjdrkaxT0&ab_channel=CodersLegacy
# Assisted on project by Scott Heggen
####################################################################################
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

class LibraryCatalog:
    def __init__(self):
        """
        Initializes catalog by loading books from the database
        """
        # define connection and cursor
        con = sqlite3.connect("project.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM books')
        rows = cur.fetchall()

        self.books = [
            Book(title=row[0], total_pages=row[1], published_date=row[2], ISBN=row[3], author=row[4], genre=row[5])
            for row in rows
        ]

    def search_by_author(self, author_name):
        """
        searches for book by the author's name
        :param author_name: author's name to search
        :return: list of books by author
        """

        return [book for book in self.books if book.author == author_name]

    def search_by_genre(self, genre_name):
        """
        searches for book by genre
        :param genre_name: genre to search
        :return: list of books by genre
        """

        return [book for book in self.books if book.genre.lower() == genre_name.lower()]

    def format_search_results (self, results):
        """
        format search results to display them in a more pleasing manner
        :param results: list of book objects
        :return: formatted string with book details
        """
        if not results:
            return "No books found."

        formatted_results = []
        for book in results:
            book_info = "Title: " + str(book.title) + "\n" + \
                        "Author: " + str(book.author) + "\n" + \
                        "Genre: " + str(book.genre) + "\n" + \
                        "Published: " + str(book.published_date) + "\n" + \
                        "Pages: " + str(book.total_pages) + "\n"
            formatted_results.append(book_info)

        return "\n\n".join(formatted_results)

class Book:
    def __init__(self, ISBN, title, author, genre, published_date, total_pages):
        """
        Initializes Book instance with title, author, genre, ISBN, published_date and total_pages
        :param title: title of book
        :param author: author of book
        :param genre: genre of book
        :param status: reading status of book (default is 'unread')
        """

        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.genre = genre
        self.published_date = published_date
        self.total_pages = total_pages

class LibraryApp:
    def __init__(self, catalog):
        """
        Initializes app with a reference to the catalog
        :param catalog
        """
        self.catalog = catalog
        self.root = tk.Tk()
        self.root.title("Library App")
        self.setup_widgets()

    def setup_widgets(self):
        """
        creates basic GUI layout
        """
        tk.Label(self.root, text="Library Catalog", font=("Helvetica", 16)).pack(pady=10)

        #create Treeview widget
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(pady=10)
        self.load_data()

        tk.Button(self.root, text="Search Books", command=self.search_books).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def load_data(self):
        """
        loads the data from sqlite database into a treeview widget
        """

        conn = sqlite3.connect("project.db")
        cursor = conn.cursor()

        #fetch column names and rows
        cursor.execute("PRAGMA table_info(books)")
        columns = [col[1] for col in cursor.fetchall()]
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        self.tree['columns']=columns
        self.tree.column('#0', width=0, stretch=tk.NO)

        for col in columns:
            self.tree.column(col, anchor=tk.CENTER, width=100)
            self.tree.heading(col, text=col.title(), anchor=tk.CENTER)

        for row in rows:
            self.tree.insert("", tk.END, values=row)

        conn.close()

    def search_books(self):
        """
        opens search window to find books by author genre
        """
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Books")

        tk.Label(search_window, text="Search by Author").pack()
        author_entry = tk.Entry(search_window)
        author_entry.pack()

        tk.Label(search_window, text="Search by Genre").pack()
        genre_entry = tk.Entry(search_window)
        genre_entry.pack()

        def perform_search():
            author = author_entry.get()
            genre = genre_entry.get()
            results = []

            if author:
                results.extend(self.catalog.search_by_author(author))
            if genre:
                results.extend(self.catalog.search_by_genre(genre))

            formatted_results = self.catalog.format_search_results(results)
            self.display_books(formatted_results)

        tk.Button(search_window, text="Search", command=perform_search).pack()

    def display_books(self, formatted_results):
        """
        displays list of books
        :param formatted_results: formatted string with book details
        """

        display_window = tk.Toplevel(self.root)
        display_window.title("Search Results")

        #create a text widget that will display formatted multiline results:
        text_widget = tk.Text(display_window, height=20, width=70)
        text_widget.pack(pady=10)

        text_widget.insert(tk.END, formatted_results)
        text_widget.config(state=tk.DISABLED)

def main():
    """
    Creates library catalog and GUI application
    """
    catalog = LibraryCatalog()
    app = LibraryApp(catalog)
    app.root.mainloop()

if __name__ == "__main__":
    main()