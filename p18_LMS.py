# Advance Library Management System


class Library:

    def __init__(self):
        self.books = []
        self.book_id = 1

    # Add Book
    def add_book(self, book_name, author):
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                print("Book already exists.")
                return

        book = {"id": self.book_id,"name": book_name,"author": author,"issued_to": None}

        self.books.append(book)
        print(f"Book '{book_name}' added successfully.")

        self.book_id += 1

    # Show Available Books
    def show_books(self):
        available = [book for book in self.books if book["issued_to"] is None]

        if not available:
            print("No available books.")
            return

        print("\n--- Available Books ---")

        for book in available:
            print(f"ID: {book['id']} | "f"Name: {book['name']} | "f"Author: {book['author']}")

    # Issue Book
    def issue_book(self, book_id, user_name):

        for book in self.books:
            if book["id"] == book_id:

                if book["issued_to"] is not None:
                    print("Book is already issued.")
                    return

                book["issued_to"] = user_name

                print(f"'{book['name']}' issued successfully "f"to {user_name}.")
                return

        print("Invalid Book ID.")

    # Return Book
    def return_book(self, book_id):

        for book in self.books:
            if book["id"] == book_id:

                if book["issued_to"] is None:
                    print("This book is not issued.")
                    return

                print(
                    f"'{book['name']}' returned successfully "f"by {book['issued_to']}.")

                book["issued_to"] = None
                return

        print("Invalid Book ID.")

    # Search Book
    def search_book(self, book_name):

        found = False

        for book in self.books:
            if book_name.lower() in book["name"].lower():
                status = ("Available" if book["issued_to"] is None else f"Issued to {book['issued_to']}")
                print(f"ID: {book['id']} | " f"Name: {book['name']} | "f"Author: {book['author']} | "f"Status: {status}")
                found = True

        if not found:
            print("Book not found.")

    # Delete Book
    def delete_book(self, book_id):

        for book in self.books:
            if book["id"] == book_id:

                if book["issued_to"] is not None:
                    print("Cannot delete an issued book.")
                    return
                self.books.remove(book)
                print("Book deleted successfully.")
                return

        print("Invalid Book ID.")

    # Show Issued Books
    def show_issued_books(self):
        issued = [book for book in self.books if book["issued_to"] is not None]
        if not issued:
            print("No books currently issued.")
            return

        print("\n--- Issued Books ---")

        for book in issued:
            print(f"ID: {book['id']} | "f"Name: {book['name']} | "f"Issued To: {book['issued_to']}")

    # Total Books
    def total_books(self):
        print("Total Books:", len(self.books))


# Main Program

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Show Available Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Delete Book")
    print("7. Show Issued Books")
    print("8. Total Books")
    print("9. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            name = input("Enter book name: ").strip()
            author = input("Enter author name: ").strip()
            if not name or not author:
                print("Book name and author are required.")
            else:
                library.add_book(name, author)
        elif choice == "2":
            library.show_books()
        elif choice == "3":
            book_id = int(input("Enter Book ID: "))
            user = input("Enter user name: ").strip()
            if user:
                library.issue_book(book_id, user)
            else:
                print("User name cannot be empty.")
        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            library.return_book(book_id)
        elif choice == "5":
            name = input("Enter book name to search: ").strip()
            library.search_book(name)
        elif choice == "6":
            book_id = int(input("Enter Book ID to delete: "))
            library.delete_book(book_id)
        elif choice == "7":
            library.show_issued_books()
        elif choice == "8":
            library.total_books()
        elif choice == "9":
            print("Thank you for using Library Management System.")
            break
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Please enter a valid numeric Book ID.")
