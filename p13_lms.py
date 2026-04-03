class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully.")

    def show_books(self):
        if not self.books:
            print("No books available in library.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)

    def issue_book(self, book_name):
        if book_name in self.books:
            # user took book
            self.books.remove(book_name)
            print(f"Book '{book_name}' issued successfully.")
        else:
            print("Book not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' returned successfully.")

library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book \n2. Show Books\n3. Issue Book\n4. Return Book\n5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)
    elif choice == "2":
        library.show_books()
    elif choice == "3":

        book = input("Enter book name to issue: ")
        library.issue_book(book)
    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)
    elif choice == "5":
        print("Thank you for using Library Management System.")
        break
    else:
        print("Invalid choice. Try again.")
