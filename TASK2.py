class Library:
    def __init__(self):
        self.books = {}

    def add(self, book):
        self.books[book.title.lower()] = book

    def borrow(self, title, user_name):
        book = self.books.get(title.lower())
        if book and not book.is_borrowed:
            book.is_borrowed = True
            book.borrower = user_name
            print(f"Success: {user_name} took '{book.title}'.")
        else:
            print("Error: Book unavailable.")

    def return_book(self, title):
        book = self.books.get(title.lower())
        if book and book.is_borrowed:
            book.is_borrowed = False
            book.borrower = None
        else:
            print("Error: Return failed.")