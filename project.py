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

#define connection and cursor
con = sqlite3.connect("project.db")
cur = con.cursor()



res = cur.execute("SELECT * FROM books")
print(res.fetchall())

# res2 = cur.execute("SELECT * FROM User")
# print(res2.fetchall())
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

        self.books = []  # store Book objects
        self.file_path = file_path

    def add_book(self, book):
        """
        adds a book to the catalog
        :param book: book object to add
        """

        self.books.append(book)

    def search_by_author(self, author_name):
        """
        searches for book by the author's name
        :param author_name: author's name to search
        :return: list of books by author
        """

        return [book for book in self.books if author_name.lower() in book.author.lower()]

    def search_by_genre(self, genre_name):
        """
        searches for book by genre
        :param genre_name: genre to search
        :return: list of books by genre
        """

        return [book for book in self.books if genre_name.lower() in book.genre.lower()]


class Book:
    def __init__(self, title, author, genre, status="Unread"):
        """
        Initializes Book instance with title, author, genre, and status

        :param title: title of book
        :param author: author of book
        :param genre: genre of book
        :param status: reading status of book (default is 'unread')

        """

        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def update_status(self, new_status):
        """
        Updates status of book from 'Unread' to 'Read'
        :param new_status: new status of book
        """
        self.status = new_status

    def get_info(self):
        """
        returns formatted string with book info
        :return: string with book details
        """
        return "'" + self.title + "' by " + self.author + " (Genre: " + self.genre + ", Status: " + self.status + ")"


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

        tk.Button(self.root, text="Add Book", command=self.add_book_gui).pack(pady=5)
        tk.Button(self.root, text="Search Books", command=self.search_books).pack(pady=5)
        tk.Button(self.root, text="Recommend Book", command=self.recommend_book_gui).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.save_and_exit).pack(pady=5)

    def add_book_gui(self):
        """
        opens a window to add a new book
        """

        add_window = tk.Toplevel(self.root)
        add_window.title("Add a New Book")

        tk.Label(add_window, text="Title").pack()
        title_entry = tk.Entry(add_window)
        title_entry.pack()

        tk.Label(add_window, text="Author").pack()
        author_entry = tk.Entry(add_window)
        author_entry.pack()

        tk.Label(add_window, text="Genre").pack()
        genre_entry = tk.Entry(add_window)
        genre_entry.pack()

        def submit():
            title = title_entry.get()
            author = author_entry.get()
            genre = genre_entry.get()
            if title and author and genre:
                book = Book(title, author, genre)
                self.catalog.add_book(book)
                tk.Label(add_window, text="Book added successfully!")

        tk.Button(add_window, text="Add", command=submit).pack()

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
            self.display_books(results)

        tk.Button(search_window, text="Search", command=perform_search).pack()

    def display_books(self, books):
        """
        displays list of books
        :param books: list of Book objects
        """
        display_window = tk.Toplevel(self.root)
        display_window.title("Search Results")

        for book in books:
            tk.Label(display_window, text=book.get_info()).pack()

    def save_and_exit(self):
        """
        exits app
        """

        self.root.quit()


def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    pass


if __name__ == "__main__":
    main()
