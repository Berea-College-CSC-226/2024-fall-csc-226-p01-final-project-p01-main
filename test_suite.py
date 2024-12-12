from project import *
import sys

from inspect import getframeinfo, stack
from project import Book

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class Book:
    def __init__(self, ISBN, title, author, genre, published_date, total_pages):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.genre = genre
        self.published_date = published_date
        self.total_pages = total_pages
        self.status = "Available"

    def get_info(self):
        return (self.ISBN, self.title, self.author, self.genre, self.published_date, self.total_pages)

    def update_status(self, status):
        self.status = status

class LibraryCatalog:
    def __init__(self, catalog_file):
        self.catalog_file = catalog_file
        self.books = []

    def search_by_author(self, author_name):
        return [book for book in self.books if book.author == author_name]


class LibraryApp:
    def __init__(self, catalog):
        self.catalog = catalog

    def display_books(self, books):
        for book in books:
            print("Book: " + book.title + "by " + book.author)


#tests here

def test_book_init():
    book = Book(**{
        "ISBN": 9780061120084,
        "author": "Harper Lee",
        "genre": "Fiction",
        "published_date": 1960,
        "title": "To Kill a Mockingbird",
        "total_pages": 324
    })
    did_pass = (book.ISBN == 9780061120084 and book.title == "To Kill a Mockingbird")
    unittest(did_pass)


#run test
test_book_init()

