
#return-Exits a function and returns a value to the caller.
#break-Terminates the current loop immediately.
#continue-Skips the current iteration of the loop and goes to the next iteration.
"""
import sys
max_int = sys.maxsize
min_int = -sys.maxsize-1
print(max_int)
print(min_int)
"""

"""                                                           
x = 10
print(x)

x = "Niraj"
print(x)

x, y, z = 10, "Niraj", True
print(x, y, z)
"""

#Types of variables
"""
a = None    #Like Null in other programming languages
b = 23      #int
c = 45.27   #float
d = "Niraj" #str
e = 'Niraj' #str
f = True    #Boolean
g = False   #Boolean
"""

"""
name = "Raj"
print(f'My name is {name}.')
"""

#List
"""
list = ["Niraj", 28, 99.80, True, None]
print(list)
print(list[2])
print(list[-2])
print(list[1:3])
print(list[:3])
print(list[1:4:2])
print(list[::2])
list[0], list[3] = "Sangharsh", False
print(list)
list.append("Writer and Programmer")
print(list)
list.insert(0, "Niraj")
print(list)
list.remove("Sangharsh")
print(list)
list.pop()
print(list)
list.pop(3)
print(list)
"""

"""a = [1, 2, 3]
b = [3, 4, 5]
print(a + b)"""

"""from collections import Counter
list = [1, 4, 5, 3, 2, 6, 5, 4, 4, 3, 1, 2, 1, 2]
x = Counter(list)
print(x)"""

#Tuple
"""
tuple = ("Niraj", 28, 99.80, True, None)
print(tuple)
tuple = "Niraj", 28, 99.80, True, None
print(tuple)
print(tuple[1])
print(tuple[-2])
print(tuple[1:4])
print(tuple[:3])
print(tuple[1:4:2])
print(tuple[::2])

a, b, c = (12, "XYZ", None)
print(a)
print(b)
print(c)
"""

"""
def get_coordinates():
    x = 10
    y = 20
    return x, y
coordinates = get_coordinates()
print(coordinates)

def get_coordinates(x, y):
    return x, y
coordinates = get_coordinates(10, 20)
print(coordinates)
"""

#Range
"""
for i in range(10):
    print(i)
for i in range(3, 9, 2):
    print(i)
for i in range(10, 3, -3):
    print(i)

my_list = list(range(1,16,4))
print(my_list)
"""

#Dict
"""
dict = {
    "Niraj" : 99.80,
    "Sangharsh" : 100,
    "Suraj" : 98.79,
    "Raju" : 67.87
}
print(dict)

#dict = {}
#print(dict)
#dict["Niraj"] = 99.80
#dict["Sangharsh"] = 100
#print(dict)

print(dict["Sangharsh"])
print(dict.get("Sangharsh"))
#print(dict["Samar"])
print(dict.get("Samar"))
print(dict.get("Samar", "Absent"))

dict["Raju"] = 99.36
print(dict)

dict["Vivek"] = 91.56
print(dict)

for key in dict:
    print(key)

for value in dict.values():
    print(value)

for key, values in dict.items():
    print(key, values)

if "Niraj" in dict:
    print("Key_Found")

if 99.36 in dict.values():
    print("Value_Found")

del dict["Niraj"]
print(dict)
"""

#Set
"""
my_set = {1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9}
print(my_set)

my_set = set([1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9]) 
print(my_set)

my_set.add(10)
print(my_set)

my_set.update([11, 11, 12, 13, 13, 13])
print(my_set)

my_set.remove(9)
print(my_set)

#my_set.remove(17)
#print(my_set)

my_set.discard(10)
print(my_set)

my_set.discard(17)
print(my_set)

if 3 in my_set:
    print("3 is in the set")
else:
    print("3 is not in the set")

my_set1 = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}
union_set = my_set1.union(my_set2)
print(union_set)
intersection_set = my_set1.intersection(my_set2)
print(intersection_set)
difference_set = my_set1.difference(my_set2)
print(difference_set)
"""

#Frozen Set
"""
my_frozenset = frozenset([1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9])
print(my_frozenset)

if 3 in my_frozenset:
  print("3 is in the set")
else:
  print("3 is not in the set")

my_frozenset1 = frozenset([1, 2, 3, 4])
my_frozenset2 = frozenset([3, 4, 5, 6])
union_set = my_frozenset1.union(my_frozenset2)
print(union_set)
intersection_set = my_frozenset1.intersection(my_frozenset2)
print(intersection_set)
difference_set = my_frozenset1.difference(my_frozenset2)
print(difference_set)
"""

#String
#Concatenation
"""
a = "Niraj"
b = "Champ"
c = a + b
print(c)

c = "Niraj" + "Champ"
print(c)

print("Niraj" + "Champ")
"""

"""a = "Niraj"

concatenatedString = a * 5
print(concatenatedString)

list_of_strings = [a] * 5
concatenated_string = "".join(list_of_strings)
print(concatenated_string)"""

#Indexing & Slicing
"""
a = "abcdefghijklmnopqrstuvwxyz"
print(a[-9])
print(a[21])
print(a[3:10])
print(a[:10])
print(a[8:])
print(a[::2])
print(a[3:10:2])

print(len(a))
print(a.upper())
print(a.lower())"""

"""
#Strip trims leading and trailing whitespaces.
b = "     Niraj       "
print(b.strip())

#Split converts string into list.
c = "abcde, fghij, klmno, pqrst, uvwxyz"
print(list(c))
print(c.split())
    
#Join converts list into string.
d = ["abcde", "fghij", "klmno", "pqrst", "uvwxyz"]
print(", ".join(d))
print(" ".join(d))
print("".join(d))

e = "My name is Niraj."
print(e.replace("Niraj", "Suraj"))
"""

#Immutability
"""
a = "Niraj"
#a[3] = "z"
print(a.replace("r", "z"))
"""
#TypeError: 'str' object does not support item assignment

#Condition Statements
"""
x = 5
if x >= 10:
    print("Number is greater than or equal to 10.")
elif x <= 5:
    print("Number is smaller than or equal to 5.")
else:
    print("Number is in between 5 and 10.")
"""

#For Loop:
"""
my_string = "Hello, World!"
for char in my_string:
    print(char)

my_list = [1, 2, 3, 4, 5]
for number in my_list:
    print(number)

for i in range(5):
    print(i)
"""

#While Loop
"""
count = 0
while count < 5:
    print(count)
    count += 1

while True:
    user_input = input("Enter a number (type 'Exit' to quit): ")
    if user_input == "exit":
        break
    else:
        print("You entered:", user_input)
"""

#Do While Loop:In Python, there is no built-in "do-while" loop.
"""
while True:
    user_input = input("Enter a number: ")
    print("You entered:", user_input)
    if user_input == "exit":
        break
"""

#Functions
"""
def my_function():
    print("My Function")
    
def greet(name):
    print("Hello, " + name + "!")

def add_numbers(a, b):
    print(a + b)

my_function()   
greet("John")
add_numbers(2, 3) 
"""

#Class
"""
class Person:
    def __init__(self, name, age): #__init__ Method/Constructor 
        self.name = name           #name Attributes
        self.age = age             #age Attributes

    def greet(self):               #greet Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person = Person("Alice", 25)

# Accessing attributes and calling methods
print(person.name)
print(person.age)
person.greet()
"""

#Encapsulation
"""class Car:
    def __init__(self, make, model, year):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute
        self.__year = year  # Private attribute

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

car = Car("Toyota", "Camry", 2022)

print(car.get_make())  # Output: Toyota
print(car.get_model())  # Output: Camry
print(car.get_year())  # Output: 2022

car.set_make("Tata")
car.set_model("Thar")
car.set_year(2023)
print(car.get_make())  #Output: Tata
print(car.get_model())  #Output: Thar
print(car.get_year())  # Output: 2023"""


"""
By using these methods, external code can get the values of the attributes using car.get_make(), car.get_model(), and car.get_year(). 
The set_year() method allows external code to modify the private __year attribute.
"""

"""class Car:
    def __init__(self, make, model, year):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute
        self.__year = year  # Private attribute
    
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year

car = Car("Toyota", "Camry", 2022)
print(car.make)  # Output: Toyota
print(car.model)  # Output: Camry
print(car.year)  # Output: 2022

car.make = "Tata"
car.model = "Thar"
car.year = 2023
print(car.make)  #Output: Tata
print(car.model)  #Output: Thar
print(car.year)  # Output: 2023"""

#Inheritance
#Basic Inheritance
"""
class Animal:
    def sound(self):
        print("Making a sound")

class Dog(Animal):
    def sound(self):
        print("Barking")

class Cat(Animal):
    def sound(self):
        print("Meowing")

dog = Dog()
dog.sound()  # Output: Barking

cat = Cat()
cat.sound()  # Output: Meowing
"""

#Inheritance with Super()
"""
class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        super().sound()  # Call the superclass method
        print("Dog barks.")

dog = Dog()
dog.sound()
"""

"""
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print("Employee ID:", self.employee_id)

emp = Employee("Alice", 123)
emp.display()
"""

#Multiple Inheritance
"""
class Vehicle:
    def display(self):
        print("Vehicle")

class Engine:
    def display(self):
        print("Engine")

class Car(Vehicle, Engine):
    pass

car = Car()
car.display()  # Output: Vehicle
"""

"""When you create an object car of the Car class and call the display() method on it (car.display()), Python looks for the method in 
the class hierarchy from left to right. In this case, it first finds the display() method in the Vehicle class, so that method is 
executed."""

#Polymorphism with Objects
"""
class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()
"""

#Polymorphism with Functions
"""
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
  
    def language(self):
        print("Hindi is the most widely spoken language of India.")
  
    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
  
    def language(self):
        print("English is the primary language of USA.")
  
    def type(self):
        print("USA is a developed country.")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()
  
obj_ind = India()
obj_usa = USA()
  
func(obj_ind)
func(obj_usa)
"""

"""class Animal:
    def move(self):
        print("The animal is moving.")


class Dog(Animal):
    def bark(self):
        print("Woof!")


dog = Dog()
dog.move()  # The animal is moving.
dog.bark()  # Woof!

def move(animal):
    animal.move()

dog = Dog()
move(dog)  # The animal is moving."""

#Compile-time polymorphism (Method overloading)
"""Compile-time polymorphism (or method overloading) is a feature of some programming languages that allows a class to have multiple 
methods with the same name, but with different parameters. The method that is called is determined at compile time, based on the types 
of the arguments that are passed to the method. 
Python does not support compile-time polymorphism. If there are multiple methods with 
the same name in a class or Python script, the method specified in the latter one will override the earlier one. This is called 
method overriding."""

#Java
"""public class Calculator {
    // Method to add two integers
    public int add(int a, int b) {
        return a + b;
    }

    // Method to add three integers
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Method to add two doubles
    public double add(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        int sum1 = calculator.add(2, 3);
        System.out.println("Sum of two integers: " + sum1); // Output: Sum of two integers: 5

        int sum2 = calculator.add(2, 3, 4);
        System.out.println("Sum of three integers: " + sum2); // Output: Sum of three integers: 9

        double sum3 = calculator.add(2.5, 3.7);
        System.out.println("Sum of two doubles: " + sum3); // Output: Sum of two doubles: 6.2
    }
}"""

"""class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Create an instance of the Calculator class
calc = Calculator()

# Call the add method with two arguments
result1 = calc.add(1, 2)
print(result1)  # Output: TypeError: add() missing 1 required positional argument: 'c'

# Call the add method with three arguments
result2 = calc.add(1, 2, 3)
print(result2)  # Output: 6"""

#Alternate methods to acheive method overloading in python
#Default Argument
"""class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
result1 = calc.add(2)          # a=2, b=0, c=0
result2 = calc.add(2, 3)       # a=2, b=3, c=0
result3 = calc.add(2, 3, 4)    # a=2, b=3, c=4
print(result1, result2, result3)"""

#Function Overloading Using Conditionals:
"""class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif b is not None and c is None:
            return a + b
        elif b is not None and c is not None:
            return a + b + c

calc = Calculator()
result1 = calc.add(2)          # 2
result2 = calc.add(2, 3)       # 5
result3 = calc.add(2, 3, 4)    # 9
print(result1, result2, result3)"""

#Variable-Length Argument Lists (*args, **kwargs):Python allows you to use variable-length argument lists to create flexible methods. 
#You can define a method that accepts any number of positional arguments (*args) or keyword arguments (**kwargs) and then handle the 
#arguments accordingly within the method.

#*args (Arbitrary Positional Arguments):The *args syntax is used to pass a variable number of non-keyword (positional) arguments to 
#a function. Inside the function, *args collects these arguments into a tuple, which you can then iterate over or use in various ways.
"""def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result

total = add_numbers(1, 2, 3, 4, 5)
print(total)  # Output: 15"""

"""class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
result1 = calc.add(2)          # 2
result2 = calc.add(2, 3)       # 5
result3 = calc.add(2, 3, 4)    # 9
print(result1, result2, result3)"""

#**kwargs (Arbitrary Keyword Arguments):The **kwargs syntax is used to pass a variable number of keyword arguments to a function. 
#Inside the function, **kwargs collects these keyword arguments into a dictionary, where the keys are the argument names and the 
#values are the argument values.
"""def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, country="USA")
# Output:
# name: Alice
# age: 30
# country: USA"""

#*args (Arbitrary Positional Arguments) & **kwargs (Arbitrary Keyword Arguments):
"""def example_function(arg1, *args, kwarg1=None, **kwargs):
    print("arg1:", arg1)
    print("args:", args)
    print("kwarg1:", kwarg1)
    print("kwargs:", kwargs)

example_function(1, 2, 3, kwarg1="Hello", name="Alice", age=30)"""

"""def example_function(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

example_function(1, 2, 3, greeting="Hello", name="Alice", age=30)"""

#Run-time polymorphism (Method Overriding):
"""class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Create instances of the derived classes
dog = Dog()
cat = Cat()

# Call the speak method on instances
dog.speak()  # Output: "Dog barks"
cat.speak()  # Output: "Cat meows"
"""

#Abstraction

#Abstract Classes
"""class Shape:
    def area(self):
        raise NotImplementedError("This method must be implemented in a subclass.")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

square = Square(5)
print(square.area())  # 25"""

#Interfaces
"""
from abc import ABC, abstractmethod
 
class Polygon(ABC): 
    @abstractmethod
    def noofsides(self):
        print("We are talking about polygon.")
 
class Triangle(Polygon): 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides.")
 
class Quadrilateral(Polygon): 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides.")
 
# Driver code
T = Triangle()
T.noofsides()
 
Q = Quadrilateral()
Q.noofsides()
"""

#Linear Search-Iterative
"""
def linearSearch(array, value):
  for i in range(len(array)):
    if array[i] == value: return i
  return -1

array = [1, 56, 34, 897, 23, 8]
value = 897

result = linearSearch(array, value)
if result == -1:
  print("Target element not found.")
else:
  print(f"Target element found as index {result}.")
"""

#Linear Search-Recursive
"""
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1

    elif arr[index] == target:
        return index

    else:
        return linear_search_recursive(arr, target, index + 1)
    
array = [4, 2, 7, 1, 9, 5]
target_element = 7

result = linear_search_recursive(array, target_element)
if result != -1:
    print("Element", target_element, "found at index", result)
else:
    print("Element", target_element, "does not found in the array.")
"""

#Binary Search-Iterative
"""
def binary_search(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] < target:
      left = mid + 1
    elif arr[mid] > target:
      right = mid - 1
    else:
      return mid

  return -1
  
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

result = binary_search(arr, target)
if result == -1:
  print("Target element not found.")
else:
  print(f"Target element found as index {result}.")
"""

#Binary Search-Recursive
"""
def binary_search(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            return binary_search(arr, left, mid - 1, target)
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, right, target)
        else:
            return mid
        
    else:
        return -1
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

result = binary_search(arr, 0, len(arr)-1, target)
if result == -1:
  print("Target element not found.")
else:
  print(f"Target element found as index {result}.")
"""

#Sorting
"""
numbers = [5, 2, 7, 1, 9, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=len)
print(sorted_names)

numbers = [5, 2, 7, 1, 9, 3]
numbers.sort()
print(numbers)

names = ["Alice", "Bob", "Charlie", "David"]
names.sort(key=len)
print(names)

numbers = [5, 2, 7, 1, 9, 3]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

numbers = [5, 2, 7, 1, 9, 3]
numbers.sort(reverse=True)
print(numbers)

numbers = [5, 2, 7, 1, 9, 3]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)

names = [5, 2, 7, 1, 9, 3]
names.sort(key=lambda x: -x)
print(names)

numbers = [5, 2, 7, 1, 9, 3]
sorted_numbers = sorted(numbers, key=lambda x: x % 2 == 0)
print(sorted_numbers)

people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 31}
]
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)

people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 31}
]
sorted_people = sorted(people, key=lambda x: -x['age'])
print(sorted_people)

people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 31}
]
sorted_people = sorted(people, key=lambda x: x['age'], reverse=True)
print(sorted_people)
"""

#Swapping
"""
a = 5
b = 10

temp = a
a = b
b = temp

print(a, b)


a = 5
b = 10

a, b = b, a

print(a, b)


my_list = [1, 2, 3, 4, 5]
i, j = 1, 3

temp = my_list[i]
my_list[i] = my_list[j]
my_list[j] = temp

print(my_list)


my_list = [1, 2, 3, 4, 5]
i, j = 1, 3

my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)


my_list = [1, 2, 3, 4, 5]
i, j = 1, 3

my_list[i:j+1] = my_list[j:i-1:-1]

print(my_list)
"""

#Bubble Sort-Iterative

"""def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]

numbers = [5, 2, 7, 1, 9, 3]
bubble_sort(numbers)
print(numbers)"""


#Bubble Sort-Recursive

"""def bubble_sort_recursive(arr, n):
    if n <= 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    bubble_sort_recursive(arr, n - 1)

numbers = [5, 2, 7, 1, 9, 3]
bubble_sort_recursive(numbers, len(numbers))
print(numbers)"""


#Selection Sort-Iterative

"""def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = [5, 2, 7, 1, 9, 3]
selection_sort(numbers)
print(numbers)"""


#Selection Sort-Recursive

"""def selection_sort_recursive(arr, n):
    if n <= 1:
        return

    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i

    arr[max_index], arr[n-1] = arr[n-1], arr[max_index]

    selection_sort_recursive(arr, n - 1)

numbers = [5, 2, 7, 1, 9, 3]
selection_sort_recursive(numbers, len(numbers))
print(numbers)"""


#Insertion Sort-Iterative

"""def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

numbers = [5, 2, 7, 1, 9, 3]
insertion_sort(numbers)
print(numbers)"""


#Insertion Sort-Recursive

"""def insertion_sort_recursive(arr, n):
    if n <= 1:
        return

    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

    insertion_sort_recursive(arr, n - 1)


numbers = [5, 2, 7, 1, 9, 0]
insertion_sort_recursive(numbers, len(numbers))
print(numbers)"""


#Merge Sort
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = 0  # Index for the left half
    j = 0  # Index for the right half

    # Merge the elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from the left or right half
    merged.extend(left[i:])
    merged.extend(right[j:])
                                                                             

numbers = [11, 5, 98, 45, 1, 35]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
"""

#Stack-LIFO
"""
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print("Stack:", self.stack)
    
stack = Stack()
stack.push(12)
stack.push(23)
stack.push(9)
stack.print_stack()
print(stack.size())  
print(stack.peek()) 
stack.print_stack() 
print(stack.pop())
stack.print_stack()   
print(stack.pop())  
stack.print_stack() 
print(stack.size())
"""

#Queue-FIFO
"""
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)
    
    def print_queue(self):
        print("Queue:", self.queue)
    
queue = Queue()
queue.enqueue(12)
queue.enqueue(92)
queue.enqueue(37)
queue.print_queue()
print(queue.size())  
print(queue.peek()) 
queue.print_queue() 
print(queue.dequeue())
queue.print_queue()  
print(queue.dequeue())
queue.print_queue()  
print(queue.size())
"""

#Quick Sort-Iterative
"""
def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()

        if start >= end:
            continue

        pivot = arr[end]  # Choose the last element as the pivot
        partition_index = partition(arr, start, end, pivot)

        stack.append((start, partition_index - 1))  # Left subarray
        stack.append((partition_index + 1, end))  # Right subarray

    return arr

def partition(arr, start, end, pivot):
    partition_index = start  # Index of the partition

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1

    arr[partition_index], arr[end] = arr[end], arr[partition_index]  # Move pivot to its final position
    return partition_index

numbers = [5, 2, 7, 1, 9, 3]
sorted_numbers = quick_sort_iterative(numbers)
print(sorted_numbers)
"""

#Quick Sort-Iterative
def iterative_quicksort(arr):
    """
    Iterative quick sort
    :param arr: arr to be sorted
    :return:
    """
    if arr is None or len(arr) <= 1:
        return

    lo = 0
    hi = len(arr)-1

    stack = Stack()
    stack.push(lo)
    stack.push(hi)


    while not stack.is_empty():

        hi = stack.pop()
        lo = stack.pop()

        # as long as we have at least two elements to sort
        if lo < hi:

            # create the partitions
            p = partition(arr, lo, hi)

            # push the left partition indexes
            stack.push(lo)
            stack.push(p-1)

            # push the right partition indexes
            stack.push(p+1)
            stack.push(hi)

    return arr


def partition(a, lo, hi):
    """
    Last element pivot partition: rearrange elements in the array by putting all the elements < than pivot to the left
    and elements > than pivot to the right.
    :param a: array to partition
    :param lo: lower bound of the array to partition
    :param hi: higher bound of the array to partition
    :return: the final pivot position in the array
    """
    pivot = a[hi]
    i = lo
    j = lo

    while j <= hi:
        if (a[j] < pivot):
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1

    a[i], a[hi] = a[hi], a[i]

    return i

class Stack():
    """
    Simple stack implementation
    """
    def __init__(self):
        """
        Initialize the list of items of the stack
        """
        self.list = []

    def push(self, item):
        """
        Push an item onto the stack
        :param item: The item to push
        :return:
        """
        self.list.append(item)

    def pop(self):
        """
        Pop an item from top of the stack
        :return: The popped item
        """
        if len(self.list) > 0:
            item = self.list.pop()
            return item
        else:
            raise "ERROR: Stack is empty."

    def peek(self):
        """
        Peek on top of the stack
        :return: the item on top of the stack
        """
        if len(self.list) > 0:
            return self.list[len(self.list)-1]
        else:
            return None

    def is_empty(self):
        """
        Check if the stack is empty
        :return: True if empty / False if not empty
        """
        return len(self.list) == 0

    def size(self):
        """
        Get the size of the stack
        :return:
        """

        return len(self.list)
"""
numbers = [5, 2, 7, 1, 9, 3]
sorted_numbers = iterative_quicksort(numbers)
print(sorted_numbers)
"""

#Quick Sort-Recursive
"""
def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_recursive(left) + equal + quick_sort_recursive(right)

numbers = [5, 2, 7, 1, 9, 3]
sorted_numbers = quick_sort_recursive(numbers)
print(sorted_numbers)
"""

#Radix Sort
def radix_sort(array, radix = 10):
  """
  Sorts the given array using Radix Sort.

  Args:
    array: The array to sort.
    radix: The radix of the number system.

  Returns: The sorted array.
  """
  max_value = max(array)
  place_value = 1
  while max_value // place_value > 1:
    bucket = [[] for _ in range(radix)]
    #print(bucket)
    for i in range(len(array)):
      digit = (array[i] // place_value) % radix
      bucket[digit].append(array[i])
      #print(bucket)
    array = []
    for i in range(radix):
      array += bucket[i]
      #print(array)
    place_value *= radix
  return array

"""array = [121, 432, 564, 23, 1, 45, 788]
sorted_array = radix_sort(array)
print(sorted_array)"""


#Singly Linked List
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add(self, value, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == value:
                temp = current.next
                current.next = new_node
                new_node.next = temp
                return
            current = current.next
        print("Value is not in the linked list.")  
        
    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        if self.is_empty():
            print("Linked List is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

my_list = SinglyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.prepend(5)
my_list.display()
print(my_list.search(20))
my_list.add(10, 15)
my_list.display()
my_list.add(18, 19)
my_list.display()
my_list.delete(20)
my_list.display()
"""

#Doubly Linked List
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add(self, value, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == value:
                temp = current.next
                current.next = new_node
                new_node.prev = current
                new_node.next = temp
                temp.prev = new_node
                return
            current = current.next
        print("Value is not in the linked list.")
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def delete(self, data):
        if self.is_empty():
            print("List is empty.")
            return
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        if self.is_empty():
            print("Linked List is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

my_list = DoublyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.prepend(5)
my_list.display()
print(my_list.search(10))
my_list.add(10, 15)
my_list.display()
my_list.add(18, 19)
my_list.display()
my_list.delete(20)
my_list.display()
"""

#Binary Search Tree
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
    else:
      current_node = self.root
      while True:
        if value < current_node.value:
          if current_node.left is None:
            current_node.left = new_node
            break
          else:
            current_node = current_node.left
        else:
          if current_node.right is None:
            current_node.right = new_node
            break
          else:
            current_node = current_node.right

  def search(self, value):
    current_node = self.root
    while current_node is not None:
      if value == current_node.value:
        return current_node
      elif value < current_node.value:
        current_node = current_node.left
      else:
        current_node = current_node.right
    return None  

  def delete_node(self, value):
    current_node = self.root
    while current_node is not None:
      if value == current_node.value:
        # We found the node to delete.
        if current_node.left is None and current_node.right is None:
          # The node is a leaf node.
          return current_node
        elif current_node.left is None:
          # The node has only a right child.
          return current_node.right
        elif current_node.right is None:
          # The node has only a left child.
          return current_node.left
        else:
          # The node has two children.
          # Replace the node with its successor.
          successor = current_node.right
          while successor.left is not None:
            successor = successor.left
          current_node.value = successor.value
          # Delete the successor node.
          successor = current_node.right
          while successor.left is not None:
            successor = successor.left
          successor.value = None
      elif value < current_node.value:
        current_node = current_node.left
      else:
        current_node = current_node.right
    return None
  
  def successor(self, value):
    current_node = self.root
    while current_node is not None:
      if value == current_node.value:
        successor = current_node.right
        while successor.left is not None:
            successor = successor.left 
        return successor.value
      elif value < current_node.value:
        current_node = current_node.left
      else:
        current_node = current_node.right
    return None
  
  def predecessor(self, value):
    current_node = self.root
    while current_node is not None:
      if value == current_node.value:
        predecessor = current_node.left
        while predecessor.right is not None:
            predecessor = predecessor.right
        return predecessor.value
      elif value < current_node.value:
        current_node = current_node.left
      else:
        current_node = current_node.right
    return None
  
def inorder_traversal(root):
    if root is None:
        return []
    else:
        return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)
  
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(20)

inorder_traversal_result = inorder_traversal(bst.root)
print(inorder_traversal_result)

node = bst.search(15)
if node is not None:
  print(node.value, "is in BST.")

deleted_node = bst.delete_node(2)
if deleted_node is not None:
  print(deleted_node.value)

inorder_traversal_result = inorder_traversal(bst.root)
print(inorder_traversal_result)

suc = bst.successor(10)
print(suc)
pre = bst.predecessor(10)
print(pre)
"""

"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def delete_node_recursive(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        # The node to be deleted is found.
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # The node to be deleted has two children.
        successor = find_min(root.right)
        root.value = successor.value
        root.right = delete_node_recursive(root.right, successor.value)
    return root

def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def inorder_traversal(root):
    if root is None:
        return []
    else:
        return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

if __name__ == "__main__":
  root = Node(10)
  root.left = Node(5)
  root.right = Node(15)
  root.left.left = Node(2)
  root.left.right = Node(7)
  root.right.left = Node(12)
  root.right.right = Node(20)
  
  inorder_traversal_result = inorder_traversal(root)
  print(inorder_traversal_result)

  deleted_node = delete_node_recursive(root, 10)
  print(deleted_node.value)

inorder_traversal_result = inorder_traversal(root)
print(inorder_traversal_result)
"""

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def delete_node_iterative(root, key):
    parent = None
    current = root

    while current:
        if key == current.val:
            # Case 1: Node with no children or only one child
            if not current.left:
                if parent:
                    if current == parent.left:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                else:
                    root = current.right
            elif not current.right:
                if parent:
                    if current == parent.left:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    root = current.left
            # Case 2: Node with two children
            else:
                successor = find_min_node(current.right)
                current.val = successor.val
                current.right = delete_node_iterative(current.right, successor.val)

            break
        elif key < current.val:
            parent = current
            current = current.left
        else:
            parent = current
            current = current.right

    return root

def find_min_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def inorder_traversal(root):
    if root is None:
        return []
    else:
        return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

inorder_traversal_result = inorder_traversal(root)
print(inorder_traversal_result)

new_root = delete_node_iterative(root, 3)

inorder_traversal_result = inorder_traversal(root)
print(inorder_traversal_result)
"""

"""
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#LevelOrder Traversal
def levelorder(root):
    if root is None:
        return
    queue = [root]
    levelorder = []
    while queue:
        node = queue.pop(0)
        levelorder.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(levelorder)

#InOrder Traversal
def inorder(root):
  stack = []
  inorder = []
  current = root
  while current or stack:
    while current:
      stack.append(current)
      current = current.left
    current = stack.pop()
    inorder.append(current.data)
    current = current.right
  print(inorder)


def inorderR1(root):
    if not root:
        return []
    result = []
    if root.left:
        result.extend(inorderR1(root.left))
    result.append(root.data)
    if root.right:
        result.extend(inorderR1(root.right))
    return result

def inorderR2(root):
    if root is None:
        return []
    left_traversal = inorderR2(root.left)
    right_traversal = inorderR2(root.right)
    return left_traversal + [root.data] + right_traversal 

#PreOrder Traversal
def preorder(root):
    if root is None:
        return
    stack = [root]
    preorder = []
    while stack:
        current = stack.pop()
        preorder.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    print(preorder)

def preorderR1(root):
    if root is None:
        return []
    left_traversal = preorderR1(root.left)
    right_traversal = preorderR1(root.right)
    return [root.data] + left_traversal + right_traversal

def preorderR2(root):
    if root is None:
        return
    print(root.data)
    preorderR2(root.left)
    preorderR2(root.right)

#PostOrder Traversal
def postorder(root):
    if root is None:
        return []
    left_traversal = postorder(root.left)
    right_traversal = postorder(root.right)
    return left_traversal + right_traversal + [root.data]

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

levelorder(root)

inorder(root)
result = inorderR1(root)
print(result)
outcome = inorderR2(root)
print(outcome)

preorder(root)
outcome = preorderR1(root)
print(outcome)
preorderR2(root)

traversal = postorder(root)
post_order = []
for node in traversal:
   post_order.append(node)
print(post_order)
"""

#Max Heap
"""
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def pop(self):
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_child_index = index
            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_child_index]:
                largest_child_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_child_index]:
                largest_child_index = right_child_index
            if largest_child_index != index:
                self._swap(index, largest_child_index)
                index = largest_child_index
            else:
                break

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

heap = MaxHeap()
heap.insert(45)
heap.insert(40)
heap.insert(32)
heap.insert(38)
heap.insert(35)
heap.insert(26)
heap.insert(5)
heap.insert(32)
heap.insert(31)
print(heap.heap)

max_value = heap.peek()
print(max_value)

max_value = heap.pop()
print(max_value)
print(heap.heap)

max_value = heap.peek()
print(max_value)
"""

#Min Heap
"""
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def pop(self):
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_child_index = index
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_child_index]:
                smallest_child_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_child_index]:
                smallest_child_index = right_child_index
            if smallest_child_index != index:
                self._swap(index, smallest_child_index)
                index = smallest_child_index
            else:
                break

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

heap = MinHeap()
heap.insert(5)
heap.insert(40)
heap.insert(12)
heap.insert(49)
heap.insert(56)
heap.insert(15)
heap.insert(21)
heap.insert(72)
heap.insert(81)
print(heap.heap)

min_value = heap.peek()
print(min_value)

min_value = heap.pop()
print(min_value)
print(heap.heap)

min_value = heap.peek()
print(min_value)
"""

#Hash Map-Problem

"""class HashMap:
    def __init__(self):
        self.buckets = []
        print(len(self.buckets))

    def insert(self, key, value):
        bucket_index = self.hash(key)
        print(bucket_index, self.hash(key))
        bucket = self.buckets[bucket_index]
        if bucket is None:
            bucket = []
            self.buckets[bucket_index] = bucket
            bucket.append((key, value))

    def get(self, key):
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        if bucket is None:
            return None
        for key_value in bucket:
            if key_value[0] == key:
                return key_value[1]
        return None

    def hash(self, key):
        return hash(key) % len(self.buckets)"""


#HashMap-Chaining:
"""
class HashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(10)]

    def insert(self, key, value):
        hash_value = hash(key) % len(self.buckets)
        print(hash(key), hash_value)
        bucket = self.buckets[hash_value]
        bucket.append((key, value))

    def get(self, key):
        hash_value = hash(key) % len(self.buckets)
        bucket = self.buckets[hash_value]
        for key_value in bucket:
            if key_value[0] == key:
                return key_value[1]
        return None
    
    def delete(self, key):
        hash_value = hash(key) % len(self.buckets)
        bucket = self.buckets[hash_value]
        for key_value in bucket:
            if key_value[0] == key:
                del bucket[key]
        return None"""

#HashMap-OpenAddressing
"""class HashMap():
    def __init__(self, capacity):
        self.buckets = [None] * capacity

    def insert(self, key, value):
        index = self.hash(key)
        while self.buckets[index] is not None:
            index = (index + 1) % len(self.buckets)
        self.buckets[index] = (key, value)

    def get(self, key):
        index = self.hash(key)
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (index + 1) % len(self.buckets)
        return None

    def hash(self, key):
        return hash(key) % len(self.buckets)

#hash_map = HashMap()
hash_map = HashMap(20)
hash_map.insert("Sachin", "India")
hash_map.insert("Roger", "Switzerland")
hash_map.insert("Wood", "USA")
hash_map.insert("Warne", "Australia")
hash_map.insert("Sangakkara", "Srilanka")
print(hash_map.buckets)


value = hash_map.get("Sangakkara")
print(value)

hash_map.delete("Roger")
print(hash_map.buckets)"""

#Directed Graph
"""class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        self.adjacency_list[source].append(destination)
                                                                      
    def get_neighbors(self, source):
        if source not in self.adjacency_list:
            return []
        return self.adjacency_list[source]

    def delete_edge(self, source):
        if source in self.adjacency_list:
            del self.adjacency_list[source]
        for node in self.adjacency_list:
            if source in self.adjacency_list[node]:
               self.adjacency_list[node].remove(source)
        return self.adjacency_list       
    
graph = DirectedGraph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("C", "D")

print(graph.adjacency_list)

print(graph.get_neighbors("A"))
print(graph.get_neighbors("B"))
print(graph.get_neighbors("C"))
print(graph.get_neighbors("D"))
print(graph.get_neighbors("E"))

graph.delete_edge("B")

print(graph.adjacency_list)

print(graph.get_neighbors("A"))
print(graph.get_neighbors("B"))
print(graph.get_neighbors("C"))
print(graph.get_neighbors("D"))"""

#BFS
"""def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
    return visited

graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": [],
}
print(bfs(graph, "A"))"""

#DFS
"""def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    return visited

graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": [],
}
print(dfs(graph, "A"))"""

#Undirected Graph
"""class UndirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def get_neighbors(self, source):
        if source not in self.adjacency_list:
            return []
        return self.adjacency_list[source]

    def delete_edge(self, source):    
        if source in self.adjacency_list:
            for neighbor in self.adjacency_list[source]:
                self.adjacency_list[neighbor].remove(source)
            del self.adjacency_list[source]
        return self.adjacency_list
    
graph = UndirectedGraph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("C", "D")

print(graph.adjacency_list)

print(graph.get_neighbors("A"))
print(graph.get_neighbors("B"))
print(graph.get_neighbors("C"))
print(graph.get_neighbors("D"))

graph.delete_edge("A")

print(graph.adjacency_list)

print(graph.get_neighbors("A"))
print(graph.get_neighbors("B"))
print(graph.get_neighbors("C"))
print(graph.get_neighbors("D"))"""

#Weighted Graph
"""class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination, weight):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = {}
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = {}
        self.adjacency_list[source][destination] = weight
        self.adjacency_list[destination][source] = weight

    def get_neighbors(self, source):
        if source not in self.adjacency_list:
            return []
        return self.adjacency_list[source].keys()

    def get_weight(self, source, destination):
        if source not in self.adjacency_list or destination not in self.adjacency_list[source]:
            return None
        return self.adjacency_list[source][destination]
    
    def delete_edge(self, source):    
        if source in self.adjacency_list:
            for neighbor in self.adjacency_list[source]:
                del self.adjacency_list[neighbor][source]
            del self.adjacency_list[source]
        return self.adjacency_list
    
graph = WeightedGraph()

graph.add_edge("A", "B", 10)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "C", 2)
print(graph.adjacency_list)

neighbors = graph.get_neighbors("A")
print(neighbors)

weight = graph.get_weight("A", "C")
print(weight)

graph.delete_edge("A")
print(graph.adjacency_list)"""

#Complete Graph
"""def complete_graph(n):
    graph = {}
    for i in range(n):
        graph[i] = []
        for j in range(n):
            if i != j:
                graph[i].append(j)
    return graph

graph = complete_graph(5)
print(graph)"""

#Cyclic Graph
"""def cyclic_graph(n):
    graph = {}
    for i in range(n):
        graph[i] = []
        for j in range(i + 1, n):
            graph[i].append(j)
    return graph

graph = cyclic_graph(5)
print(graph)"""

#Dynamic programming is an algorithmic technique for solving problems by breaking them down into smaller subproblems and storing the 
#solutions to those subproblems. This allows the algorithm to avoid re-calculating the same subproblems over and over again.
"""def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(35))"""

"""def fibonacci(n):
    fibs = [0] * (n + 1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[n]

print(fibonacci(205))"""

"""----The Longest Palindromic Subsequence (LPS) problem is to find the length of the longest subsequence of a given string that 
is a palindrome.----"""

"""def longest_palindromic_subsequence(s):
    n = len(s)

    # Create a memoization table to store computed results.
    memo = [[-1] * n for _ in range(n)]

    def lps_recursive(i, j):
        # Base case: If the string has only one character, it's a palindrome of length 1.
        if i == j:
            return 1

        # Base case: If the string has two characters and they are the same, it's a palindrome of length 2.
        if s[i] == s[j] and i + 1 == j:
            return 2

        # Check if the result is already memoized.
        if memo[i][j] != -1:
            return memo[i][j]

        # If the first and last characters are the same, they contribute 2 to the length.
        if s[i] == s[j]:
            memo[i][j] = 2 + lps_recursive(i + 1, j - 1)
        else:
            # If the first and last characters are different, we consider two possibilities:
            # 1. Exclude the first character and find LPS in the remaining substring.
            # 2. Exclude the last character and find LPS in the remaining substring.
            memo[i][j] = max(lps_recursive(i + 1, j), lps_recursive(i, j - 1))

        return memo[i][j]

    # Call the recursive function with the entire string.
    return lps_recursive(0, n - 1)

# Test the function
s = "babad"
length = longest_palindromic_subsequence(s)
print(f"The length of the longest palindromic subsequence in '{s}' is {length}")"""

"""def longest_palindromic_subsequence(s):
    n = len(s)

    # Create a table to store the lengths of longest palindromic subsequences.
    dp = [[0] * n for _ in range(n)]

    # Each character in the string is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Fill in the table using dynamic programming.
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The value at dp[0][n-1] represents the length of the longest palindromic subsequence.
    return dp[0][n - 1]

# Test the function
s = "babad"
length = longest_palindromic_subsequence(s)
print(f"The length of the longest palindromic subsequence in '{s}' is {length}")"""

"""----The Levenshtein distance, also known as the edit distance, is a measure of the similarity between two strings. It is defined as 
the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other.----"""

"""def levenshtein_distance(s1, s2):
    # Create a dictionary to memoize computed distances for pairs of substrings.
    memo = {}

    def recursive_distance(i, j):
        # Check if the distance for this pair of substrings is already memoized.
        if (i, j) in memo:
            return memo[(i, j)]

        # Base case: If one of the strings is empty, return the length of the other string.
        if i == 0:
            return j
        if j == 0:
            return i

        # If the last characters of the strings are the same, no edit is needed.
        if s1[i - 1] == s2[j - 1]:
            cost = 0
        else:
            cost = 1

        # Recursively compute the three possible edit distances and choose the minimum.
        result = min(
            recursive_distance(i - 1, j) + 1,      # Deletion
            recursive_distance(i, j - 1) + 1,      # Insertion
            recursive_distance(i - 1, j - 1) + cost  # Substitution
        )

        # Memoize the computed distance.
        memo[(i, j)] = result
        print(memo)
        return result

    # Call the recursive function with the lengths of the input strings.
    return recursive_distance(len(s1), len(s2))

# Test the function
s1 = "kitten"
s2 = "sitting"
distance = levenshtein_distance(s1, s2)
print(f"The Levenshtein distance between '{s1}' and '{s2}' is {distance}")"""

"""def levenshtein_distance(s1, s2):
    # Create a matrix to store the edit distances between substrings.
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix.
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the matrix using dynamic programming.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

    # The final value in the matrix represents the Levenshtein distance.
    print(dp)
    return dp[m][n]

# Test the function
s1 = "kitten"
s2 = "sitting"
distance = levenshtein_distance(s1, s2)
print(f"The Levenshtein distance between '{s1}' and '{s2}' is {distance}")"""

#Data Manipulation
#NumPy(Numerical Python):
"""import numpy as np

a = np.zeros(5)
print(a)

b = np.ones(5)
print(b)

c = np.empty(5)
print(c)

d = np.arange(5)
print(d)

e = np.linspace(1, 5, num = 3)
print(e)

f = np.random.rand(5)
print(f)

g = np.array([11, 63, 87, 34, 91])
print(g)

[0. 0. 0. 0. 0.]
[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]
[0 1 2 3 4]
[1. 3. 5.]
[0.73009891 0.12011758 0.27783913 0.05231131 0.84500524]
[11 63 87 34 91]"""

"""import numpy as np

# Create a 1-dimensional ndarray
arr1d = np.array([1, 2, 3, 4, 5])

# Create a 2-dimensional ndarray(matrix)
arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])

# Create a 3-dimensional ndarray
arr3d = np.array([[[1, 2],
                   [3, 4]],
                  [[5, 6],
                   [7, 8]]])"""

"""import numpy as np

# Create a NumPy array
data = np.array([1, 2, 3, 4, 5])

# Perform operations
squared_data = data ** 2
print(squared_data)
sum_of_data = np.sum(data)
print(sum_of_data)"""

#Array Slicing
"""import numpy as np

# Create a NumPy array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Basic slicing: extracting a range of elements
#subset = arr[start:stop]          # Elements from start(inclusive) to stop(exclusive)
#subset = arr[start:stop:step]     # Elements from start to stop with a step

# Common slicing examples
subset1 = arr[2:6]                 # Elements from index 2 to 5
subset2 = arr[:5]                  # Elements from the beginning to index 4
subset3 = arr[5:]                  # Elements from index 5 to the end
subset4 = arr[::2]                 # Every second element

# Negative indexing: counting from the end of the array
subset5 = arr[-3:]                 # Last 3 elements
subset6 = arr[-5:-2]               # Elements from the last 5th(inclusive) to 2nd last(exclusive)
subset7 = arr[::-1]                # Reverse the array
print(subset1, subset2, subset3, subset4, subset5, subset6, subset7)"""

"""import numpy as np

# Create a two-dimensional NumPy array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Basic slicing: extracting rows and columns
subset_rows = matrix[start_row:end_row]           # Rows from start_row(inclusive) to end_row(exclusive)
subset_cols = matrix[:, start_col:end_col]        # Columns from start_col(inclusive) to end_col(exclusive)

# Slicing specific rows and columns
subset = matrix[start_row:end_row, start_col:end_col]  # Rows and columns from start_row to end_row and start_col to end_col

# Slicing entire rows or columns
row = matrix[row_index]              # Get a specific row(row_index)
col = matrix[:, col_index]           # Get a specific column(col_index)

# Slicing with step
subset = matrix[start_row:end_row:step_row, start_col:end_col:step_col]  # Slicing with row and column steps"""

"""import numpy as np

# Create a two-dimensional NumPy array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Slicing specific rows and columns
subset = matrix[0:2, 1:3]  # Rows 0-1 and Columns 1-2
print(subset)
# Output:
# array([[2, 3],
#        [5, 6]])

# Slicing entire rows or columns
row = matrix[1]   # Second row
print(row)
# Output: array([4, 5, 6])

col = matrix[:, 2]  # Third column
print(col)
# Output: array([3, 6, 9])

# Slicing with step
subset = matrix[0:3:2, 0:3:2]  # Rows 0-2 with step 2 and Columns 0-2 with step 2
print(subset)
# Output:
# array([[1, 3],
#        [7, 9]])"""

"""import numpy as np
#subset = my_3d_array[depth_start:depth_stop:depth_step, row_start:row_stop:row_step, col_start:col_stop:col_step]

# Create a sample 3D array
my_3d_array = np.arange(24).reshape(2, 3, 4)

slice1 = my_3d_array[1, :, :]
slice2 = my_3d_array[0, 1:3, :]
slice3 = my_3d_array[:, 1:3, 2:4]
slice4 = my_3d_array[0:2:2, 0:3:2, 1:4:2]

print("Slice 1:")
print(slice1)
print("\nSlice 2:")
print(slice2)
print("\nSlice 3:")
print(slice3)
print("\nSlice 4:")
print(slice4)"""

#Array Reshaping
"""import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape into a different shape
reshaped_arr1 = arr.reshape((2, 3))
reshaped_arr2 = np.reshape(arr, (2, 3))
print(reshaped_arr1)
print(reshaped_arr2)

# Reshape into a 1D array
flattened_arr1 = reshaped_arr1.flatten()
flattened_arr2 = np.ravel(reshaped_arr1)
print(flattened_arr1)
print(flattened_arr2)

# Reshape into a 1D array using -1 (NumPy will infer the size)
arr_1d = reshaped_arr1.reshape(-1)
arr__1d = np.reshape(reshaped_arr1, -1)
print(arr_1d)
print(arr__1d)

# Reshape into a 2D array with a fixed number of rows and automatically computed columns
arr_2d_auto1 = arr.reshape(2, -1)
arr_2d_auto2 = np.reshape(arr, (2, -1))
print(arr_2d_auto1)
print(arr_2d_auto2)

# Reshape into a 3D array
arr_3d = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2, 2, 2)
print(arr_3d)
arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr_3d = np.reshape(arr, (2, 2, 2))
print(arr_3d)

# Transpose a 2D array (swap rows and columns)
transposed_arr1 = reshaped_arr1.T
transposed_arr2 = np.transpose(reshaped_arr1)
print(transposed_arr1)
print(transposed_arr2)"""

# Array Spliting and Concatenation
"""import numpy as np

# Create an example array
arr = np.arange(12).reshape(3, 4)

# Split the array into three equally-sized sub-arrays along rows
sub_arrays = np.split(arr, 3, axis=0)

# Split the array into two sub-arrays along columns
sub_arrays2 = np.split(arr, 2, axis=1)

print("Original Array:")
print(arr)
print("\nSplit along rows:")
print(sub_arrays)
print("\nSplit along columns:")
print(sub_arrays2)

Original Array:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

Split along rows:
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

Split along columns:
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]"""

"""import numpy as np

# Create two example arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

# Concatenate arr2 to arr1 along rows (axis=0)
concatenated = np.concatenate((arr1, arr2), axis=0)

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)
print("\nConcatenated along rows:")
print(concatenated)"""

#Mathematical Operation
"""import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 10, 15])

result = np.add(arr1, arr2)
print("Result of addition:", result)
result = np.subtract(arr1, arr2)
print("Result of subtraction:", result)
result = np.multiply(arr1, arr2)
print("Result of multiplication:", result)
result = np.divide(arr1, arr2)
print("Result of division:", result)

Result of addition: [ 5 12 18]
Result of subtraction: [ -3  -8 -12]
Result of multiplication: [ 4 20 45]
Result of division: [0.25 0.2  0.2 ]"""

#Array Aggregation
"""import numpy as np

arr = np.array([1, 2, 3, 4, 5])

#Sum
total = np.sum(arr)
print(total)

#Product
product = np.prod(arr)
print(product)

#Cumulative Sum & Product
cumulative_sum = np.cumsum(arr)
cumulative_product = np.cumprod(arr)
print(cumulative_sum, cumulative_product)

#Mean
average = np.mean(arr)
print(average)

#Median
median = np.median(arr)
print(median)

#Max & Min Value
min_value = np.min(arr)
max_value = np.max(arr)
print(min_value, max_value)

#Variance & Standard Deviation
std_deviation = np.std(arr)
variance = np.var(arr)
print(std_deviation, variance)"""

#Aggregation along Axis
"""import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Compute the sum along rows(axis=0) & columns(axis=1)
sum_rows = np.sum(matrix, axis=0)
sum_cols = np.sum(matrix, axis=1)
print(sum_rows, sum_cols)

# Compute the mean along rows(axis=0) & columns(axis=1)
mean_rows = np.mean(matrix, axis=0)
mean_cols = np.mean(matrix, axis=1)
print(mean_rows, mean_cols)"""

"""import numpy as np

arr3d = np.array([[[1, 2],
                   [3, 4]],
                  [[5, 6],
                   [7, 8]]])

## Compute the sum along depth(axis=0), rows(axis=1) & columns(axis=2)
sum_depths = np.sum(arr3d, axis=0)
sum_rows = np.sum(arr3d, axis=1)
sum_cols = np.sum(arr3d, axis=2)

print(sum_depths)
print("\n", sum_rows)
print("\n", sum_cols)

[[ 6  8]
 [10 12]]

 [[ 4  6]
  [12 14]]

 [[ 3  7]
  [11 15]]"""

#Pandas
#DataFrame
"""import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
print(df)
#Or
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [10, 20, 30, 40, 50]})
print(df)"""

#Series
"""import pandas as pd

data = [10, 20, 30, 40, 50]
my_series = pd.Series(data)
print(my_series)

data = [10, 20, 30, 40, 50]
custom_index = ['A', 'B', 'C', 'D', 'E']
my_series = pd.Series(data, index=custom_index)
print(my_series)

#data2 working as index
data1 = [10, 20, 30, 40, 50]
data2 = [12, 23, 34, 45, 56]
my_series = pd.Series(data1, data2)
print(my_series)

#Not Working
data1 = [10, 20, 30, 40, 50]
data2 = [12, 23, 34, 45, 56]
custom_index = ['A', 'B', 'C', 'D', 'E']
my_series = pd.Series(data1, data2, index=custom_index)
print(my_series)"""

# Create a DataFrame with a MultiIndex
"""import pandas as pd

data = {
    'Sales': [100, 120, 150, 130, 200, 180],
    'Quantity': [10, 12, 15, 13, 20, 18]
}

index = pd.MultiIndex.from_tuples(
    [('2023-01', 'Product_A'),
    ('2023-01', 'Product_B'),
    ('2023-02', 'Product_A'),
    ('2023-02', 'Product_B'),
    ('2023-03', 'Product_A'),
    ('2023-03', 'Product_B')], 
    names=['Month', 'Product'])

df = pd.DataFrame(data, index=index)
print(df)"""


#Data Filtering:
#Boolean Indexing:
"""import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

#Filter rows where column 'A' is greater than 3
filtered_df = df[df['A'] > 3]
print(filtered_df)

#Multiple Conditions:Filter rows where column 'A' is greater than 2 and column 'B' is less than 40
filtered_df = df[(df['A'] > 2) & (df['B'] < 40)]
print(filtered_df)

#isin() Method:Filter rows based on values present in a list
values_to_filter_A = [2, 4]
filtered_df = df[df['A'].isin(values_to_filter_A)]
print(filtered_df)"""

"""import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# Create a boolean mask for filtering
mask = df['Age'] > 30
# Apply the mask to filter rows
filtered_df = df[mask]
print(filtered_df)

#String Filtering:Filter names starting with 'A'
filtered_df = df[df['Name'].str.startswith('A')]
print(filtered_df)

# Filtering using multiple conditions
mask = (df['Age'] > 30) & (df['Name'].str.startswith('C'))
filtered_df = df[mask]
print(filtered_df)

#Filtering by Index:
filtered_df = df.loc[df.index.isin([0, 2])]
print(filtered_df)

#Filtering Null Values:Filter rows where 'Age' is not null & null
filtered_df = df[df['Age'].notnull()]
print(filtered_df)
filtered_df = df[df['Age'].isnull()]
print(filtered_df)
#Empty DataFrame
#Columns: [Name, Age]
#Index: []"""

"""import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

filtered_df = df.query('Age > 30')
print(filtered_df)

#String Filtering:Filter names starting with 'A'
filtered_df = df.query('Name.str.startswith("A")')
print(filtered_df)

# Filtering using multiple conditions
filtered_df = df.query('(Age > 30) & (Name.str.startswith("C"))')
print(filtered_df)
filtered_df = df.query('(Age > 30) and (Name != "Charlie")')
print(filtered_df)

#Filtering Null Values:Filter rows where 'Age' is not null & null
filtered_df = df.query('Age.notnull()')
print(filtered_df)
filtered_df = df.query('Age.isnull()')
print(filtered_df)
#Empty DataFrame
#Columns: [Name, Age]
#Index: []"""



#Data Reshaping
#Pivot:
"""import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01'],
    'Product': ['A', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 120]
}
df = pd.DataFrame(data)
print(df)

# Pivot the DataFrame
pivot_df = df.pivot(index='Date', columns='Product', values='Sales')
print(pivot_df)"""

"""import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01'],
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [100, 150, 200, 120]
}
df = pd.DataFrame(data)
print(df)

# Pivot the DataFrame
pivot_df = df.pivot(index='Date', columns='Product', values='Sales')
print(pivot_df)"""

#Melt
"""import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-02'],
    'A': [100, 120],
    'B': [150, 130]
}
df = pd.DataFrame(data)
print(df)

# Melt the DataFrame
melted_df1 = df.melt(id_vars='Date', var_name='Product', value_name='Sales')
print(melted_df1)
#Or
melted_df2 = pd.melt(df, id_vars='Date', var_name='Product', value_name='Sales')
print(melted_df2)"""

#Stacking & Unstacking
"""import pandas as pd

# Create a sample DataFrame with a MultiIndex
data = {
    'Sales': [100, 120, 150, 130, 200, 180],
    'Quantity': [10, 12, 15, 13, 20, 18]
}

index = pd.MultiIndex.from_tuples([
    ('2023-01', 'Product_A'),
    ('2023-01', 'Product_B'),
    ('2023-02', 'Product_A'),
    ('2023-02', 'Product_B'),
    ('2023-03', 'Product_A'),
    ('2023-03', 'Product_B')
], names=['Month', 'Product'])

df = pd.DataFrame(data, index=index)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Stack the DataFrame to convert columns into a MultiIndex
stacked_df = df.stack()

# Print the stacked DataFrame
print("\nStacked DataFrame:")
print(stacked_df)

# Unstack the DataFrame to pivot the innermost level back to columns
unstacked_df = stacked_df.unstack()

# Print the unstacked DataFrame
print("\nUnstacked DataFrame:")
print(unstacked_df)"""

"""import pandas as pd

# Create a sample DataFrame with a MultiIndex
data = {
    'Sales': [100, 120, 150, 130, 200, 180],
    'Quantity': [10, 12, 15, 13, 20, 18]
}

index = pd.MultiIndex.from_tuples([
    ('Product_A', '2023-01'),
    ('Product_B', '2023-01'),
    ('Product_A', '2023-02'),
    ('Product_B', '2023-02'),
    ('Product_A', '2023-03'),
    ('Product_B', '2023-03')
], names=['Product', 'Month'])

df = pd.DataFrame(data, index=index)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Stack the DataFrame to convert columns into a MultiIndex
stacked_df = df.stack()

# Print the stacked DataFrame
print("\nStacked DataFrame:")
print(stacked_df)

# Unstack the DataFrame to pivot the innermost level back to columns
unstacked_df = stacked_df.unstack()

# Print the unstacked DataFrame
print("\nUnstacked DataFrame:")
print(unstacked_df)"""

#Concatenation:
"""import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})

result = pd.concat([df1, df2], axis=0)

print("\nConcatenated result (vertical):")
print(result)

Concatenated result (vertical):
    A   B
0  A0  B0
1  A1  B1
2  A2  B2
0  A3  B3
1  A4  B4
2  A5  B5
"""

"""import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'], 'D': ['D0', 'D1', 'D2']})

result = pd.concat([df1, df2], axis=1)

print("\nConcatenated result (horizontal):")
print(result)

Concatenated result (horizontal):
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
"""

#Merge:
"""import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

result1 = pd.merge(df1, df2, on='key', how='inner')
print(result1)

result2 = pd.merge(df1, df2, on='key', how='left')
print(result2)

result3 = pd.merge(df1, df2, on='key', how='right')
print(result3)

result4 = pd.merge(df1, df2, on='key', how='outer')
print(result4)

  key  value1  value2
0   B       2       4
1   C       3       5
  key  value1  value2
0   A       1     NaN
1   B       2     4.0
2   C       3     5.0
  key  value1  value2
0   B     2.0       4
1   C     3.0       5
2   D     NaN       6
  key  value1  value2
0   A     1.0     NaN
1   B     2.0     4.0
2   C     3.0     5.0
3   D     NaN     6.0"""

#Join:
"""import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['a', 'b', 'c'])
df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2']}, index=['b', 'c', 'd'])

result1 = df1.join(df2, how='inner', on=df1.index, lsuffix='', rsuffix='')
print(result1)

result2 = df1.join(df2, how='left', on=df1.index, lsuffix='', rsuffix='')
print(result2)

result3 = df1.join(df2, how='right', on=df1.index, lsuffix='', rsuffix='')
print(result3)

result4 = df1.join(df2, how='outer', on=df1.index, lsuffix='', rsuffix='')
print(result4)

  key_0   A   B   C
b     b  A1  B1  C0
c     c  A2  B2  C1
    A   B    C
a  A0  B0  NaN
b  A1  B1   C0
c  A2  B2   C1
    key_0    A    B   C
b       b   A1   B1  C0
c       c   A2   B2  C1
NaN     d  NaN  NaN  C2
    key_0    A    B    C
a       a   A0   B0  NaN
b       b   A1   B1   C0
c       c   A2   B2   C1
NaN     d  NaN  NaN   C2
"""

#Data Aggregation
#Aggregating Single Column
"""import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Value': [10, 15, 20, 25, 12]
}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum of 'Value' within each group
result = df.groupby('Category')['Value'].sum()
print(result)

result = df.groupby('Category')['Value'].max()
print(result)

result = df.groupby('Category')['Value'].min()
print(result)

result = df.groupby('Category')['Value'].mean()
print(result)

result = df.groupby('Category')['Value'].median()
print(result)

result = df.groupby('Category')['Value'].count()
print(result)"""

#Aggregating Single Column Through Multiple Methods
"""import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Value': [10, 15, 20, 25, 12]
}
df = pd.DataFrame(data)

# Calculate both mean and sum for 'Value' within each group
result = df.groupby('Category')['Value'].agg(['mean', 'sum'])
print(result)"""

#Aggregating Multiple Columns
"""import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Value': [10, 15, 20, 25, 12],
    'Quantity': [134, 342, 245, 678, 546]
}
df = pd.DataFrame(data)

# Group by 'Category' and calculate sum and mean for 'Value' and 'Quantity'
result = df.groupby('Category').agg({'Value': 'sum', 'Quantity': 'mean'})
print(result)
result = df.groupby('Category').agg({'Value': ['sum', 'mean'], 'Quantity': ['sum', 'mean']})
print(result)"""

#Custom Aggregation
"""import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Value': [10, 15, 20, 25, 12]
}
df = pd.DataFrame(data)

# Define a custom aggregation function
def custom_agg(arr):
    return arr.max() - arr.min()

# Group by 'Category' and apply the custom aggregation function
result = df.groupby('Category')['Value'].agg(custom_agg)
print(result)"""

#Aggregation Using Pivot Table
"""import pandas as pd

# Create a sample DataFrame with sales data
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
    'Product': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Sales': [100, 120, 150, 80, 90, 110]
}
df = pd.DataFrame(data)

# Create a pivot table to summarize sales by product and date
pivot_table = df.pivot_table(index='Product', columns='Date', values='Sales', aggfunc='sum')
print(pivot_table)
pivot_table = df.pivot_table(index='Date', columns='Product', values='Sales', aggfunc='sum')
print(pivot_table)
pivot_table = df.pivot_table(index='Product', columns='Date', values='Sales')
print(pivot_table)
pivot_table = df.pivot_table(index='Date', columns='Product', values='Sales')
print(pivot_table)"""

#Matplotlib: https://matplotlib.org/stable/contents.html
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 9]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()"""

#Figure and Axes:A figure represents the entire window or page where your plots are drawn and axes are the individual plotting areas 
#or subplots within the figure.

#Creating a Figure and Axes Using plt.subplots():
"""import matplotlib.pyplot as plt

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Create a figure with multiple subplots (e.g., 2 rows and 2 columns)
fig, axs = plt.subplots(2, 2)

# axs is now a 2D array of axes objects, and you can access individual subplots using indexing
axs[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16])
axs[0, 0].set_title('Subplot 1')

axs[0, 1].scatter([1, 2, 3, 4], [2, 4, 6, 8])
axs[0, 1].set_title('Subplot 2')

axs[1, 0].bar(['A', 'B', 'C', 'D'], [10, 20, 15, 30])
axs[1, 0].set_title('Subplot 3')

axs[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
axs[1, 1].set_title('Subplot 4')

# Add a title to the entire figure
fig.suptitle('Multiple Subplots')

# Adjust spacing between subplots and figure
plt.tight_layout()
# Show the figure
plt.show()

plt.tight_layout(pad=1.0)  # Increase padding
plt.show()

plt.tight_layout(w_pad=4.0, h_pad=2.0)  # Increase horizontal and vertical spacing
plt.show()"""

#Creating a Figure and Axes Using plt.figure() and figure.add_subplot():
"""import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure()
#fig = plt.figure(figsize=(8, 6))

# Adding subplots to the figure
ax1 = fig.add_subplot(2, 2, 1)  # 2 rows, 2 columns, subplot index 1
ax2 = fig.add_subplot(2, 2, 2)  # Subplot index 2
ax3 = fig.add_subplot(2, 2, 3)  # Subplot index 3
ax4 = fig.add_subplot(2, 2, 4)  # Subplot index 4

# Customize and plot on ax1
ax1.plot([1, 2, 3, 4], [1, 4, 9, 16])
ax1.set_title('Subplot 1')

# Customize and plot on ax2
ax2.scatter([1, 2, 3, 4], [2, 4, 6, 8])
ax2.set_title('Subplot 2')

# Customize and plot on ax3
ax3.bar(['A', 'B', 'C', 'D'], [10, 20, 15, 30])
ax3.set_title('Subplot 3')

# Customize and plot on ax4
ax4.hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
ax4.set_title('Subplot 4')

# Add a title to the entire figure
fig.suptitle('Multiple Subplots')

# Adjust spacing between subplots and figure
plt.tight_layout()
# Show the figure
plt.show()"""

#Plotting Functions:

#Line Plots (plt.plot()):
"""import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 9]
plt.plot(x, y, label='Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')
plt.legend()
plt.show()"""

#Scatter Plots (plt.scatter()):
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 9]
plt.scatter(x, y, label='Scatter Plot', color='red', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.legend()
plt.show()"""

#Bar Plots (plt.bar() and plt.barh()):
"""import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C']
values = [25, 40, 30]
plt.bar(categories, values, color='blue', alpha=0.9)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()

plt.barh(categories, values, color='blue', alpha=0.9)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Bar Chart Example')
plt.show()"""

#Histograms (plt.hist()):
"""import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color='green', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()"""

#Pie Charts (plt.pie()):
"""import matplotlib.pyplot as plt

labels = ['Category A', 'Category B', 'Category C']
sizes = [25, 35, 40]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart Example')
plt.show()"""

# %1.1f formats the percentage as a floating-point number with one digit before the decimal point and one digit after 
# and %% is used to include a literal percent symbol in the label.

# By default, the pie chart starts at an angle of 0 degrees (the positive x-axis). Setting startangle to 90 degrees rotates 
# the starting point to the positive y-axis.

#Box Plots (plt.boxplot()):
"""import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 6]
plt.boxplot(data)
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()"""

# Median (Line Inside the Box), Box (IQR - Interquartile Range), Whiskers (Lines Extending from the Box), Outliers (Individual Points)
# The whiskers typically extend to a maximum of 1.5 times the IQR from either Q1 or Q3. 
# Any data points beyond this range are considered potential outliers and are plotted individually as points.

#Heatmaps (plt.imshow()):
"""
import matplotlib.pyplot as plt
import numpy as np

# Create sample data (a 5x5 matrix)
data = np.random.rand(5, 5)

# Create a heatmap
plt.imshow(data, cmap='viridis')  # 'viridis' is a colormap
plt.colorbar()  # Add a colorbar to the plot

# Add labels to the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a title
plt.title('Basic Heatmap Example')

# Show the heatmap
plt.show()"""

"""
import matplotlib.pyplot as plt
import numpy as np

# Create sample data (a 5x5 matrix)
data = np.random.rand(5, 5)

# Create a heatmap with custom colormap and color range
plt.imshow(data, cmap='coolwarm', vmin=0, vmax=1)  # 'coolwarm' colormap
plt.colorbar()

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Heatmap')

plt.show()"""

#Customization and Styling:

#Setting Axis Labels and Titles:
#Use plt.xlabel() and plt.ylabel() to set labels for the x and y axes.
#Use plt.title() to set the title of the plot.

#Adding a Legend:Use plt.legend() to add a legend to your plot.
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label='Dataset 1')
plt.plot(x, y2, label='Dataset 2')

plt.legend()

plt.show()"""

"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [5, 15, 20, 25]

plt.plot(x, y1, label='Data 1')
plt.plot(x, y2, label='Data 2')

plt.legend(loc='upper left', title='Legend', fontsize=12)

plt.show()"""

#Adjusting Axis Limits:
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)

plt.xlim(0, 5)
plt.ylim(0, 20)

plt.show()"""

#Adding Grid Lines:
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)

plt.grid(True)

plt.show()"""

#Changing Fonts and Text Properties:
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)

plt.xlabel('X-axis Label', fontsize=14, fontweight='bold')
plt.ylabel('Y-axis Label', fontsize=14, fontweight='bold')

plt.title('Customized Title', fontsize=16, fontweight='bold', fontstyle='italic')

plt.show()"""

#Customizing Plot Size and Aspect Ratio:
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.figure(figsize=(8, 4))  # Set figure size

plt.plot(x, y)

plt.show()"""

#Line Style, Color and Marking:
"""import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y, linestyle="--", color="red")
plt.show()

plt.plot(x, y, marker="o")
plt.show()"""


