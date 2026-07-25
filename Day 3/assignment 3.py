class Library:
    def __init__(self):
        self.books = ["Python", "AI", "Java"]

    def show(self):
        print("Books:", self.books)

    def issue(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "Issued")
        else:
            print("Book Not Found")

    def return_book(self, book):
        self.books.append(book)
        print(book, "Returned")

lib = Library()

lib.show()
lib.issue("Python")
lib.return_book("Python")
lib.show()
