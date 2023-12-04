# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def printname(self):
        print(self.firstName, self.lastName)


x = Person("E o", "Prix")
x.printname()


# Create a child class
class Child(Person):  # this class has all that is in "Person class, either it's just a "pass
    pass


person = Person("Zé", "Caba bão")
person.printname()


# adding __init__ to
class Student(Person):  # The child's __init__() function overrides the inheritance of the parent's __init__() function
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        # super().__init__(fname, lname) # It inher... the methods, is the same as line up
        self.graduationYear = year

    # add methods
    def welcome(self):
        print("Welcome, ", self.firstName, self.lastName, "to the class of", self.graduationYear)

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of
# the parent method will be overridden.


y = Student("Kchorro", "AuAu", 2021)
y.printname()
print(y.graduationYear)
y.welcome()
