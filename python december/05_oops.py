"""
==================================================
PYTHON OOPS — COMPLETE EXPLANATION IN ONE FILE
==================================================

OOPS = Object Oriented Programming System

Main concepts:
1. Class
2. Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
"""

# -----------------------------------------------
# 1. CLASS AND OBJECT
# -----------------------------------------------
# A class is a blueprint
# An object is an instance of a class

class Person:
    # Class variable (shared by all objects)
    species = "Human"

    # Constructor (runs when object is created)
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name}"

# Creating objects
p1 = Person("Alex", 20)
p2 = Person("Sam", 25)

print(p1.greet())
print(p2.name)
print(Person.species)


# -----------------------------------------------
# 2. SELF KEYWORD
# -----------------------------------------------
# self refers to the current object

class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

c = Counter()
c.increase()
print(c.count)


# -----------------------------------------------
# 3. ENCAPSULATION
# -----------------------------------------------
# Binding data and methods together
# Use _ or __ to indicate protected/private

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
# print(acc.__balance)  # ❌ error (private)


# -----------------------------------------------
# 4. INHERITANCE
# -----------------------------------------------
# Child class inherits from parent class

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())


# -----------------------------------------------
# 5. SUPER KEYWORD
# -----------------------------------------------
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car = Car("Toyota", "Corolla")
print(car.brand, car.model)


# -----------------------------------------------
# 6. POLYMORPHISM
# -----------------------------------------------
# Same method name, different behavior

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

animals = [Cat(), Cow()]

for animal in animals:
    print(animal.sound())


# -----------------------------------------------
# 7. METHOD OVERLOADING (SIMULATED)
# -----------------------------------------------
# Python doesn't support true overloading
# We use default arguments instead

class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5))
print(m.add(5, 10))
print(m.add(5, 10, 15))


# -----------------------------------------------
# 8. METHOD OVERRIDING
# -----------------------------------------------
class Parent:
    def show(self):
        return "Parent method"

class Child(Parent):
    def show(self):
        return "Child method"

obj = Child()
print(obj.show())


# -----------------------------------------------
# 9. ABSTRACTION
# -----------------------------------------------
# Hide implementation, show only functionality

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 4 * 4

sq = Square()
print(sq.area())


# -----------------------------------------------
# 10. CLASS METHOD
# -----------------------------------------------
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("XYZ School")
print(Student.school)


# -----------------------------------------------
# 11. STATIC METHOD
# -----------------------------------------------
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(3, 4))


# -----------------------------------------------
# 12. DUNDER (MAGIC) METHODS
# -----------------------------------------------
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book has {self.pages} pages"

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)
print(b1)
print(b1 + b2)


# -----------------------------------------------
# 13. IS-A vs HAS-A RELATIONSHIP
# -----------------------------------------------
# IS-A → Inheritance
# HAS-A → Composition

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # HAS-A

my_car = Car()
print(my_car.engine.start())


# -----------------------------------------------
# 14. OBJECT DELETION
# -----------------------------------------------
class Demo:
    def __del__(self):
        print("Object destroyed")

d = Demo()
del d


# -----------------------------------------------
# SUMMARY
# -----------------------------------------------
"""
✔ Class & Object
✔ Constructor
✔ Encapsulation
✔ Inheritance
✔ Polymorphism
✔ Abstraction
✔ Class & Static methods
✔ Magic methods
✔ Composition
"""

print("All OOPS concepts explained ✅")
