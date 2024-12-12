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

# data1 = cur.execute('SELECT * FROM books')
# print(data1.fetchall())

#ALT to lines 22/23
# res = cur.execute("SELECT * FROM books")
# print(res.fetchall())

#res2 = cur.execute("SELECT * FROM User")
#print(res2.fetchall())
#
# res3 = cur.execute("SELECT LastName FROM User")
# print(res3.fetchall())

# for row in cur.execute("SELECT LastName, FirstName FROM User ORDER BY LastName"):
#     print(row)
#
# for row in cur.execute("SELECT LastName, LastName FROM User ORDER BY LastName"):
#     print(row)



class LibraryCatalog:
    def __init__(self, file_path, windowtext="Library Catalog"):
        """
        Initializes catalog with optional file path for saving and loading
        :param windowtext: The text at the top of the window title
        :file_path: file path for catalog storage
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




        self.file_path = file_path #what is this used for in my code?????? CHECKKKK

    # def add_book(self, book):
    #     """
    #     adds a book to the catalog
    #     :param book: book object to add
    #     """
    #
    #     self.books.append(book)

    def search_by_author(self, author_name):
        """
        searches for book by the author's name
        :param author_name: author's name to search
        :return: list of books by author
        """
        # for book in self.books:
        #     if book[4] == author_name:
        #         return book
        #     else:
        #         return "Not Found"

        #print("Books in catalog:", [book.author for book in self.books])
        return [book for book in self.books if book.author == author_name]

    # def search_by_genre(self, genre_name):
    #     """
    #     searches for book by genre
    #     :param genre_name: genre to search
    #     :return: list of books by genre
    #     """
    #
    #     return [book for book in self.books if genre_name.lower() in book.genre.lower()]


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

    def get_info(self):
        """
        returns formatted string with book info
        :return: string with book details
        """
        return self.ISBN, self.title, self.author, self.genre, self.published_date, self.total_pages


    def update_status(self, new_status):
        """
        Updates status of book from 'Unread' to 'Read'
        :param new_status: new status of book
        """
        self.status = new_status


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
        self.tree = ttk.Treeview(self.root)


    #use this code for next step:
    # root = Tk()
    # table = ttk.Treeview(root)
    # table['columns'] = ('column1', 'column2', ...)
    # table.column('#0', width=100, anchor=CENTER)
    # table.heading('#0', text='ID')
    # for col in table['columns']:
    #     table.column(col, width=100, anchor=CENTER)
    #     table.heading(col, text=col.title())
    # for item in data:
    #     table.insert('', 'end', text=item[0], values=item[1:])
    # table.pack()
    # root.mainloop()

    def setup_widgets(self):
        """
        creates basic GUI layout
        """

        tk.Label(self.root, text="Library Catalog", font=("Helvetica", 16)).pack(pady=10)

        #create Treeview widget
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(pady=10)

        self.load_data() #FIXXXXX

        #tk.Button(self.root, text="Add Book", command=self.add_book_gui).pack(pady=5)
        tk.Button(self.root, text="Search Books", command=self.search_books).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.save_and_exit).pack(pady=5)

    # def add_book_gui(self):
    #     """
    #     opens a window to add a new book
    #     """
    #
    #     add_window = tk.Toplevel(self.root)
    #     add_window.title("Add a New Book")
    #
    #     tk.Label(add_window, text="Title").pack()
    #     title_entry = tk.Entry(add_window)
    #     title_entry.pack()
    #
    #     tk.Label(add_window, text="Author").pack()
    #     author_entry = tk.Entry(add_window)
    #     author_entry.pack()
    #
    #     tk.Label(add_window, text="Genre").pack()
    #     genre_entry = tk.Entry(add_window)
    #     genre_entry.pack()
    #
    #     def submit():
    #         title = title_entry.get()
    #         author = author_entry.get()
    #         genre = genre_entry.get()
    #         if title and author and genre:
    #             book = Book(title, author, genre)
    #             self.catalog.add_book(book)
    #             tk.Label(add_window, text="Book added successfully!")
    #
    #     tk.Button(add_window, text="Add", command=submit).pack()


    def load_data(self):
        """
        loads the data from sqlite database into a treeview widget
        """

        conn = sqlite3.connect("project.db")
        cursor = conn.cursor()

        #fetch data!!!!
        cursor.execute("PRAGMA table_info(books)")
        columns = [col[1] for col in cursor.fetchall()]
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        self.tree['columns']=columns
        self.tree.column('#0', width=0, stretch=tk.NO)

        for col in columns:
            self.tree.column(col, anchor=tk.CENTER, width=100)
            self.tree.heading(col, text=col.title(), anchor=tk.CENTER)

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

        # tk.Label(search_window, text="Search by Genre").pack()
        # genre_entry = tk.Entry(search_window)
        # genre_entry.pack()

        def perform_search():
            author = author_entry.get()
            #genre = genre_entry.get()
            results = self.catalog.search_by_author(author)
            # if author:
            #     results.extend(self.catalog.search_by_author(author))
            # # if genre:
            #     results.extend(self.catalog.search_by_genre(genre))
            self.display_books(results)

        tk.Button(search_window, text="Search", command=perform_search).pack()

    def display_books(self, results):
        """
        displays list of books
        :param results: list of Book objects
        """

        display_window = tk.Toplevel(self.root)
        display_window.title("Search Results")

        if not results:
            tk.Label(display_window, text="No books found.").pack()
        else:
            for book in results:
                tk.Label(display_window, text=book.get_info()).pack()

    def save_and_exit(self):
        """
        exits app
        """

        self.root.quit()

def main():
    """
    Creates library catalog and GUI application
    """

    file_path = "catalog_data.json" #NOT CURRENTLY USED YET

    catalog = LibraryCatalog(file_path)

    #preloaded books (for testing):
    # catalog.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
    # catalog.add_book(Book( "1984", "George Orwell", "Dystopian"))
    # catalog.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Classic"))

    #initializes and runs library app:
    app = LibraryApp(catalog)
    app.root.mainloop()



if __name__ == "__main__":
    main()
