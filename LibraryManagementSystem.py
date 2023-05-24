

while True:
    print("-"*100)
    print(".................................Welcome To The CenterPoint Library.................................")
    print("-"*100)


    while True:
        username = input("Enter Username : ")
        if username == "mann":
            password = input("Enter Password : ")
            if password == "1234" :
                print("Login Sucessful")
                break
            else:
                print("Enter Correct Password")
        else:
            print("Enter Correct Username")


    print("-"*40)
    print(username)
    print("-"*40)

    class Library:
        def __init__(self):
            self.books = {'math': 20, 'science' : 25, 'Hindi' : 25 ,'English' : 20}
            self.borrowed_books = {}

        def display_menu(self):
            print("""
            Press 1 to View Available Books
            Press 2 to Add New Books
            Press 3 to Borrow Books
            Press 4 to View Current Holding Books
            Press 5 to Return Book
            Press 0 to Exit
            """)

        def display_available_books(self):
            print("Available Books:")
            print("-"*40)
            for book, count in self.books.items():
                print(f"{book}: {count}")
            print("-"*40)

        def add_book(self, book, count):
            if book in self.books:
                self.books[book] += count
            else:
                self.books[book] = count
            print("-"*40)
            print(f"Added {count} {book}(s) to the library.")
            print("-"*40)

        def borrow_book(self, book, person):
            if book in self.books and self.books[book] > 0:
                self.books[book] -= 1
                self.borrowed_books[book] = person
                print("-"*40)
                print(f"{person} borrowed {book}.")
                print("-"*40)
            else:
                print("-"*40)
                print(f"{book} is not available.")
                print("-"*40)

        def display_borrowed_books(self):
            print("-"*40)
            print("Current Holding Books:")
            print("-"*40)
            if self.borrowed_books:
                for book, person in self.borrowed_books.items():
                    print("-"*40)
                    print(f"{book} - Borrowed by: {person}")
                    print("-"*40)
            else:
                print("-"*40)
                print("No books are currently being held.")
                print("-"*40)

        def return_book(self, book):
            if book in self.borrowed_books:
                self.books[book] += 1
                person = self.borrowed_books.pop(book)
                print("-"*40)
                print(f"{book} returned by {person}.")
                print("-"*40)
            else:
                print("-"*40)
                print(f"{book} was not borrowed.")
                print("-"*40)

        def run(self):
            while True:
                self.display_menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.display_available_books()
                elif choice == '2':
                    book = input("Enter the name of the book: ")
                    count = int(input("Enter the number of books to add: "))
                    self.add_book(book, count)
                elif choice == '3':
                    book = input("Enter the name of the book to borrow: ")
                    person = input("Enter the name of the borrower: ")
                    self.borrow_book(book, person)
                elif choice == '4':
                    self.display_borrowed_books()
                elif choice == '5':
                    book = input("Enter the name of the book to return: ")
                    self.return_book(book)
                elif choice == '0':
                    print("-"*40)
                    print("Thank You For Visit US",username)
                    print("-"*40)
                    break
                else:
                    print("Invalid choice. Please try again.")

    library = Library()
    library.run()
