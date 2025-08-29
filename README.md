# Activity 1: Design Your Own Class
## Overview
This assignment demonstrates Object-Oriented Programming (OOP) concepts in Python by creating a Book class.
The program shows how to:
- Define a class with attributes and methods.
- Use constructors to initialize objects with unique values.
- Implement inheritance for specialized book types.
- Demonstrate polymorphism (same method, different behavior).
- Explore encapsulation with private attributes and getters/setters.
## Parent Class: Book
Attributes: title, author, pages
Methods:
book_info() → returns basic book details
read() → simulates reading the book
## Child Class: EBook (inherits Book)
Additional Attribute: file_size (MB)
Overrides:
book_info() → includes file size
read() → reading on a device
## Child Class: PrintedBook (inherits Book)
Additional Attribute: cover_type (e.g., Hardcover, Paperback)
Overrides:
book_info() → includes cover type
read() → reading a physical book
## Encapsulation Example
Private Attribute: __rating
Getter & Setter methods to safely update book ratings

# Activity 2: Polymorphism Challenge
## Overview
This activity demonstrates the concept of Polymorphism in Python using animals.
Polymorphism allows different classes to define methods with the same name but with different behaviors.
In this example, all animals share the same method move(), but each animal defines its own unique movement style.

## Class Structure
- Parent Class: Animal
Defines a base method move() (intended to be overridden).
- Child Classes
Dog → runs
Bird → flies in the sky
Fish → swims in the river
