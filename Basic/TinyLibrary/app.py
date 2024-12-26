class Library:
    def __init__(self, Libname, listOfBooks):
        self.Libname = Libname
        self.listOfBooks = listOfBooks
        CONST 

    def displayAvailableBooks(self):
        print("Here the List of Available Books")
        for each in self.listOfBooks:
            print(each)

    def getBook(self, requestBook):
        if requestBook in self.listOfBooks:
            self.listOfBooks.remove(requestBook)
            print(f"Congrats, you can take your {requestBook} book")
        else:
            print(f"Sorry...! Requested book is not available in {self.Libname} Library")

    def restoreBook(self,returnBook):
        self.listOfBooks.append(returnBook)
        print(f"Thanks for returning {returnBook} book")


class Student:
    def requestBook(self):
        print("Enter Book Name which you would like to borrow")
        self.book = input("-->")
        return self.book

    def returnBook(self):
        print("Enter Book Name which you would like to return")
        self.book = input("-->")
        return self.book

libName = input("Please Enter your Library Name: ")
print(f"Welcome to the {libName} Library")
library = Library(libName, ["A-Book", "B-Book", "C-Book", "D-Book", "E-Book"])
student = Student()


while True:
    print()
    print(f"{libName} Library offers you 4 Options")
    print('''
    Enter 1 to Display all available books
    Enter 2 to request for a book
    Enter 3 to return a book
    Enter 4 to exit
    ''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        library.displayAvailableBooks()
    elif choice == 2:
        req = student.requestBook()
        library.getBook(req)
    elif choice == 3:
        library.getBook(student.returnBook())
    elif choice == 4:
        break
    else:
        continue

