
class Book:
    def __init__(self, title, author, ISBN, available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available_copies = available_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("borrowed successfully")
            return True
        else:
            print(" is not available")
            return False

    def return_book(self):
        self.available_copies += 1
        print(' returned successfully')

    def display_info(self):
        print('the title name is:', self.title,
          'the author name is:', self.author,
          'the isbn is:', self.ISBN,
          'the available copies is:', self.available_copies)

class Member:
    def __init__(self, member_id):
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)

    def display_borrowed_books(self):
       return self.borrowed_books

class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
        
    def add_book(self, book):
        self.books.append(book)
        return book.title

    def add_member(self, member):
        self.members.append(member)
        return member.member_id

    def issue_book(self, book, member):
        member.borrow_book(book)

    def receive_book(self, book, member):
        member.return_book(book)

    def display_available_books(self):
        print("Available books:")
        for book in self.books:
            print(f"{book.title} - Copies: {book.available_copies}")

        

book1 = Book("Python 101", "John Doe", "ISBN123", 3)
book2 = Book("Data Science", "Jane Smith", "ISBN456", 2)


member1 = Member("M001")
member1.borrow_book(book1)
member1.borrow_book(book2)

member1.display_borrowed_books()

member1.return_book(book1)
member1.display_borrowed_books()
book1.display_info()
book2.display_info()

l=Library()
book1 = Book("shantnu", "Author Name", "ISBN001", 1)
print(l.add_book(book1))

print(l.display_available_books())