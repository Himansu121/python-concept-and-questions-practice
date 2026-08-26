# Constructor with parameters
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("John", 30)
# p1.display()
p2 = Person("Jane", 25)
# p2.display()

# Constructor without parameters
class Student:
    def __init__(self):
        self.name = "John"
        self.age = 30

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student()
s1.display()


# Constructor with default parameters
class Employee:
    def __init__(self, name="John", age=30):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

e1 = Employee()
e1.display()