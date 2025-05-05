#  Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

from math import e


class Student:
    def __init__(self, name, marks):
        self.name = name        # 'self' refers to the instance variable
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage
student1 = Student("Ali", 85)
student1.display()


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # Class variable to store number of objects

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()

# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):        # Public method
        print(f"{self.brand} car has started.")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Car Brand:", my_car.brand)

# Call public method
my_car.start()

# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    # Class variable
    bank_name = "xyz Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    # Class method to change bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")


# Creating instances
acc1 = Bank("ALI")
acc2 = Bank("REHAN")

# Displaying initial bank name
print("Before changing bank name:")
acc1.display()
acc2.display()

# Changing the bank name using class method
Bank.change_bank_name("AL HABIB Bank")

# Displaying updated bank name
print("\nAfter changing bank name:")
acc1.display()
acc2.display()

# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
# Using the static method without creating an instance
result = MathUtils.add(5, 10)
print("Sum:", result)

# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")


# Creating an instance
log : Logger= Logger()
print("Logger object is in use.")


# Deleting the instance explicitly (optional – usually handled by garbage collector)
del log

# You can also wait until the script ends, and Python will destroy the object automatically


# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected (by convention)
        self.__ssn = ssn          # Private (name mangled)

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)


# Creating an instance
emp = Employee("Aurangzaib", 50000, "123-45-6789")

# Accessing variables
print("Accessing public variable:")
print(emp.name)  

print("\nAccessing protected variable:")
print(emp._salary)  

print("\nAccessing private variable:")
try:
    print(emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError:
    print("Error: AttributeError occurred")

# print("\nAccessing private variable using name mangling:")
# print(emp._Employee__ssn)  # ✅ Works, but not recommended


# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of Person
        self.subject = subject

    def display(self):
        return f"Name: {self.name}, Subject: {self.subject}"

# Example usage
t = Teacher("Miss Sara", "Math")
print(t.display())  # Output: Name: Miss Sara, Subject: Math


# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # Abstract method, must be implemented by subclass


# Subclass that implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Creating an object of Rectangle
rect = Rectangle(5, 4)
print("Area of rectangle:", rect.area())

# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable
        self.breed = breed    # Instance variable

    def bark(self):
        print(f"{self.name} says: Woof woof!")


# Creating an instance of Dog
dog1 = Dog("Tiger", "Golden Retriever")

# Calling the instance method
dog1.bark()

# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method 
# increment_book_count() to increase the count when a new book is added.

class Book:
    # Class variable to keep track of total number of books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment book count whenever a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print("Total books:", Book.get_total_books()) 

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method 
# celsius_to_fahrenheit(c)
# that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")

# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "Engine started."

class Vehicle:
    def __init__(self, engine):
        self.engine = engine  # Composition: Vehicle "has an" Engine

    def start_vehicle(self):
        return self.engine.start()  # Accessing Engine method through Vehicle

# Example usage
my_engine = Engine()
my_vehicle = Vehicle(my_engine)

print(my_vehicle.start_vehicle())

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class EmployeeDetails:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: using existing Employee object

    def show_department_info(self):
        return f"Department: {self.department_name}, {self.employee.get_details()}"

# Example usage
emp = EmployeeDetails("Aurangzaib")
dept = Department("QA", emp)

print(dept.show_department_info())  

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "Show from A"

class B(A):
    def show1(self):
        return "Show from B"

class C(A):
    def show2(self):
        return "Show from C"

class D(B, C):  # Diamond Inheritance
    pass

# Example usage
obj = D()
print(obj.show())  # Output: Show from B

# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Applying the decorator
@log_function_call
def say_hello():
    print("Hello!")

# Example usage
say_hello()

# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

import types

# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = types.MethodType(greet, cls)
    return cls

# Applying the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Ali")
print(p.greet())  # Output: Hello from Decorator!

# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(1000)
print("Initial price:", p.price)  # Output: 1000

p.price = 1500
print("Updated price:", p.price)  # Output: 1500

del p.price  # Output: Deleting price...


# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example usage
m = Multiplier(5)

# Test with callable()
print("Is m callable?", callable(m))  # Output: True

# Call the object like a function
result = m(10)
print("Result of m(10):", result)  # Output: 50

# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        return "Age is valid."

# Example usage with try...except
try:
    age = int(input("Enter your age: "))
    print(check_age(age))
except InvalidAgeError as error:
    print(f"Error: {error}")
except ValueError:
    print("Please enter a valid number for age.")



# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

# Once you are done submit this form ASAP:

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # The __iter__ method returns the iterator object itself
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration when countdown reaches 0
        self.current -= 1
        return self.current + 1

# Example usage
countdown = Countdown(5)
for number in countdown:
    print(number)



















