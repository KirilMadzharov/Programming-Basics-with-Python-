"""
Annie goes to her hometown after a very long period outside the country.
On her way home, she sees her grandmother's old library and remembers her favorite book.
Help Annie by writing a program in which she enters the book (text) she is looking for.
Until Annie finds her favorite book or checks out all the books in the library,
the program must read each time on a new line the name of each subsequent
book (text) she checks out. The books in the library are out of stock once you get
the "No More Books" text.

• If it does not find the requested book to be printed on two lines:
 "The book you are looking for is not here!"
 "You checked {number} books."
• If he finds his book, one line is printed:
 "You checked {number} books and found it."
"""


book_title = input()
book_from_shelf = input()

checked_books = 0

while book_title != book_from_shelf:
    if book_from_shelf == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break

    checked_books += 1
    book_from_shelf = input()

else:
    print(f"You checked {checked_books} books and found it.")
