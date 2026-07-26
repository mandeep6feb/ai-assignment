class Library:
    def __init__(self):
        self.books = {}
        self.members = []

    def add_book(self, book):
        self.books[book] = "Available"
        print(f"{book} added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print(f"{member} registered successfully.")

    def issue_book(self, book, member):
        if member not in self.members:
            print("Member not found.")
        elif book not in self.books:
            print("Book not found.")
        elif self.books[book] == "Issued":
            print("Book already issued.")
        else:
            self.books[book] = "Issued"
            print(f"{book} issued to {member}.")

    def return_book(self, book):
        if book in self.books and self.books[book] == "Issued":
            self.books[book] = "Available"
            print(f"{book} returned successfully.")
        else:
            print("Book was not issued.")

    def search_book(self, book):
        if book in self.books:
            print(f"{book} - {self.books[book]}")
        else:
            print("Book not found.")

    def show_books(self):
        print("\nBooks in Library:")
        for book, status in self.books.items():
            print(f"{book} : {status}")


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Show Books")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book(input("Enter book name: "))
    elif choice == "2":
        library.add_member(input("Enter member name: "))
    elif choice == "3":
        book = input("Enter book name: ")
        member = input("Enter member name: ")
        library.issue_book(book, member)
    elif choice == "4":
        library.return_book(input("Enter book name: "))
    elif choice == "5":
        library.search_book(input("Enter book name: "))
    elif choice == "6":
        library.show_books()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")