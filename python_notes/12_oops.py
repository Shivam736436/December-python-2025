# -----------------------------------------
# 1. Class and Object
# -----------------------------------------
class Person:
    pass  # empty class

p1 = Person()
print("Object created:", p1, "\n")

# -----------------------------------------
# 2. Constructor (__init__)
# -----------------------------------------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 20)
s2 = Student("Sara", 22)
print("Student 1:", s1.name, s1.age)
print("Student 2:", s2.name, s2.age, "\n")

# -----------------------------------------
# 3. Instance methods
# -----------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("John", 25)
p.greet()
print("\n")

# -----------------------------------------
# 4. Update & delete attributes
# -----------------------------------------
p.age = 26
print("Updated age:", p.age)
del p.age
print("Deleted age attribute\n")

# -----------------------------------------
# 5. Class variables
# -----------------------------------------
class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

d1 = Dog("Buddy")
d2 = Dog("Rocky")
print(d1.name, d1.species)
print(d2.name, d2.species)
print("Class variable:", Dog.species, "\n")

# -----------------------------------------
# 6. Class methods & Static methods
# -----------------------------------------
class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    # Instance method
    def area(self):
        return Circle.pi * self.radius ** 2

    # Class method
    @classmethod
    def change_pi(cls, new_pi):
        cls.pi = new_pi

    # Static method
    @staticmethod
    def greet():
        print("Hello! This is a Circle class.")

c1 = Circle(5)
print("Area:", c1.area())
Circle.change_pi(3.14)
print("Area after changing pi:", c1.area())
Circle.greet()
print("\n")

# -----------------------------------------
# 7. Inheritance
# -----------------------------------------
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):  # single inheritance
    def bark(self):
        print("Barking...")

d = Dog()
d.eat()   # inherited method
d.bark()  # own method
print("\n")

# -----------------------------------------
# 8. Encapsulation (private variables)
# -----------------------------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_balance()
# print(acc.__balance)  # ❌ Error
print("\n")

# -----------------------------------------
# 9. Polymorphism
# -----------------------------------------
class Cat:
    def speak(self):
        print("Meow!")

class Dog:
    def speak(self):
        print("Bark!")

def animal_sound(animal):
    animal.speak()

c = Cat()
d = Dog()
animal_sound(c)
animal_sound(d)
print("\n")

# -----------------------------------------
# 10. Multiple Inheritance
# -----------------------------------------
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

ch = Child()
ch.skills()  # In multiple inheritance, first parent in list is taken
