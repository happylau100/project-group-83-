class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False
        self.borrower = None

    def __str__(self):
        status = f"Borrowed by {self.borrower}" if self.is_borrowed else "Available"
        return f"TITLE: {self.title:15} | STATUS: {status}"
