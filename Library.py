from utils.Library import Library
from utils.Book import Book
lib = Library()
lib.add(Book("abc"))
lib.add(Book("123"))

while True:
    print("1. Show All Book Status")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("\nSelect Option: ")

    if choice == "1":
        for b in lib.books.values(): print(b)
    elif choice == "2":
        t = input("Book title: "); n = input("Your name: ")
        lib.borrow(t, n)
    elif choice == "3":
        t = input("Book title: ")
        lib.return_book(t)
    elif choice == "4":
        break