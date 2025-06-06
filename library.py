class Library:
    def __init__(self, book_list):
        self.books = book_list
        self.borrowed_books = []

    def available_books(self):
        """Generator to yield available books one by one"""
        for book in self.books:
            if book not in self.borrowed_books:
                yield book

    def borrow_book(self, book_name):
        """Method to borrow a book"""
        if book_name in self.books and book_name not in self.borrowed_books:
            self.borrowed_books.append(book_name)
            print(f"✅ You have borrowed: {book_name}")
        else:
            print(f"❌ Sorry, '{book_name}' is not available or already borrowed.")

    def return_book(self, book_name):
        """Method to return a book"""
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            print(f"📥 You have returned: {book_name}")
        else:
            print(f"⚠️ You didn’t borrow '{book_name}'.")

class BorrowSession:
    """Custom iterator to borrow books from a given list"""
    def __init__(self, library):
        self.library = library
        self.book_generator = library.available_books()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.book_generator)


# --------- MAIN PROGRAM ---------
if __name__ == "__main__":
    # Initial book list
    my_books = ["1984", "The Alchemist", "Python Basics", "Data Structures", "AI for Beginners"]

    # Create library object
    my_library = Library(my_books)

    print("\n📚 Available Books:")
    for book in my_library.available_books():
        print(f" - {book}")

    print("\n📖 Starting borrow session...")
    session = BorrowSession(my_library)

    try:
        while True:
            next_book = next(session)
            print(f"\n👉 Next available: {next_book}")
            user_input = input("Do you want to borrow this book? (yes/no): ").strip().lower()
            if user_input == "yes":
                my_library.borrow_book(next_book)
    except StopIteration:
        print("\n✅ All books reviewed. No more available books.")

    print("\n📚 Final Available Books:")
    for book in my_library.available_books():
        print(f" - {book}")
