import heapq

class Book:
    def __init__(self, title, value=10):
        self.title = title
        self.value = value
        self.is_borrowed = False
        self.borrower = None

    def __str__(self):
        status = f"Borrowed by {self.borrower}" if self.is_borrowed else "Available"
        return f"TITLE: {self.title:15} | VAL: ${self.value:<3} | STATUS: {status}"

class Library:
    def __init__(self):
        self.books = {}
        self.repair_heap = []

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
            damage = int(input("Enter damage level(1-10) or 0 for none: "))
            if damage != 0 :
                heapq.heappush(self.repair_heap, (11-damage, book.title))
        else:
            print("Error: Return failed.")

    def process_repair(self):
        if self.repair_heap:
            priority, title = heapq.heappop(self.repair_heap)
            print(f"REPAIRING: '{title}' (Priority Level: {priority})")
        else:
            print("No books need repair.")

    def greedy_donation(self, donation_list, capacity):
        donation_list.sort(key=lambda x: x.value, reverse=True)
        for i in range(min(len(donation_list), capacity)):
            self.add(donation_list[i])
            print(f"Accepted: {donation_list[i].title} (${donation_list[i].value})")

lib = Library()
lib.add(Book("abc",40))
lib.add(Book("123",60))

while True:
    print("1. Show All Book Status")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Repair Next Book")
    print("5. Accept Best Donations")
    print("6. Exit")

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
        lib.process_repair()
    elif choice == "5":
        incoming = [Book("Gold Book", 100), Book("Dirt", 1)]
        lib.greedy_donation(incoming, 1)
    elif choice == "6":
        break