# from library_system import Book, EBook, PrintBook, Library
# from polymorphism_demo import Shape, Rectangle, Circle
from  class_static_methods_demo import Calculator

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

    # my_book = Book("1984", "George Orwell", 1949)
    # print(my_book)

    # print(repr(my_book))

    # del my_book

    # shapes = [Rectangle(10, 5), Circle(7)]

    # for shape in shapes:
    #     print(f"The area of {shape.__class__.__name__} is: {shape.area()}")

    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    
if __name__ == "__main__":
    main()