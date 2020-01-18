# Python: The Basics

## Comments

~~~python
# This is a Python comment - code blocks are so useful!
~~~

## Declaration/Initialization

~~~python
# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."
~~~

## Data Types

~~~python
boolean = True
number = 1.1
total = 0
max_val = 10
string = "Strings can be declared with single or double quotes."
List = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
Tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None
~~~

## Simple Logging

~~~python
print "Printed!"
~~~

## Conditionals

~~~python
cake = "okay"
if cake == "delicious":
    print("Yes please!")
elif cake == "okay":
    print("I'll have a small piece.")
else:
    print("No, thank you.")
~~~

## Loops

~~~python
for item in List:
    print item

while (total < max_val):
    total += values[i]
    i += 2
~~~

## Functions

~~~python
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r

calculate_stuff(5, 2)
~~~

## Class

~~~python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)  

sam = Person("Sam", 6)
sam.birthday()
sam.print_name()
sam.print_age()
~~~

