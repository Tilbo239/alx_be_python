# from library_system import Book, EBook, PrintBook, Library
from book_class import Book

def main():
    # # Create a Library instance
    # my_library = Library()

    # # Create instances of each type of book
    # classic_book = Book("Pride and Prejudice", "Jane Austen")
    # digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    # paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # # Add books to the library
    # my_library.add_book(classic_book)
    # my_library.add_book(digital_novel)
    # my_library.add_book(paper_novel)

    # # List all books in the library
    # my_library.list_books()

    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)

    print(repr(my_book))

    del my_book
if __name__ == "__main__":
    main()