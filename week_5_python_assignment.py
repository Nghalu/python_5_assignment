# Parent Class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def read(self):
        print(f"You start reading {self.title}")
       # Child Class: EBook
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # inherit from Book
        self.file_size = file_size  # in MB

    def book_info(self):
        return f"[E-Book] '{self.title}' by {self.author}, {self.pages} pages, {self.file_size}MB file"


    def read(self):
        print(f"You open the eBook {self.title} on your laptop")

# Child Class: PrintedBook
class PrintedBook(Book):
    def __init__(self, title, author, pages, cover_type):
        super().__init__(title, author, pages)
        self.cover_type = cover_type  

    def book_info(self):
        return f"[Printed Book] '{self.title}' by {self.author}, {self.pages} pages, {self.cover_type} cover"

    def read(self):
        print(f"You flip through the printed book {self.title}")

# Create objects
b1 = EBook("Python Basics", "John Smit", 200, 5)
b2 = PrintedBook("Harry Potter", "J.K. Rowling", 350, "Hard")

# Access attributes & methods
print(b1.book_info())
b1.read()

print(b2.book_info())
b2.read()

# Polymorphism: same method (read), different behavior
library = [b1, b2]
for book in library:
    book.read()
       

class Animal:
        def move(self):
          pass   # base method, will be overridden


class Dog(Animal):
       def move(self):
        print("The dog runs")


class Bird(Animal):
     def move(self):
        print("The bird flies in the sky")


class Fish(Animal):
     def move(self):
        print("The fish swims in the river")

animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
 
