class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__available = True

    def issue_book(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def is_available(self):
        return self.__available

    def __str__(self):
        status = "Available" if self.__available else "Issued"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []

    def issue(self, book):
        self.issued_books.append(book)

    def return_book(self, book):
        if book in self.issued_books:
            self.issued_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    
    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully")

    # Member Management
    def add_member(self, member):
        self.members.append(member)
        print("Member Added Successfully")

    
    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available")
        else:
            for book in self.books:
                print(book)

    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book Found:")
                print(book)
                return book
        print("Book Not Found")
        return None

    
    def issue_book(self, member_id, title):
        member = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            print("Member Not Found")
            return

        book = self.search_book(title)

        if book:
            if book.issue_book():
                member.issue(book)
                print("Book Issued Successfully")
            else:
                print("Book Already Issued")

    
    def return_book(self, member_id, title):
        for m in self.members:
            if m.member_id == member_id:
                for b in m.issued_books:
                    if b.title.lower() == title.lower():
                        b.return_book()
                        m.return_book(b)
                        print("Book Returned Successfully")
                        return
        print("Book Not Found")




library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Search Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Book Title: ")
        author = input("Author: ")
        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        member_id = input("Member ID: ")
        name = input("Member Name: ")
        member = Member(member_id, name)
        library.add_member(member)

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        title = input("Enter Book Title: ")
        library.search_book(title)

    elif choice == "5":
        member_id = input("Member ID: ")
        title = input("Book Title: ")
        library.issue_book(member_id, title)

    elif choice == "6":
        member_id = input("Member ID: ")
        title = input("Book Title: ")
        library.return_book(member_id, title)

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")