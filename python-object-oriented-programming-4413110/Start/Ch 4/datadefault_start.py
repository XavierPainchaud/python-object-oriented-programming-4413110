# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.ra(20, 40))
    

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)


# b1 = Book()
# print(b1)

b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b2)
print(b3)

@dataclass 
class Person:
   name : str = "John Doe"
   age : int = 35
   city : str = "New York"
   occupation : str


@dataclass 
class Person:
   occupation : str
   name : str = "John Doe"
   age : int = 35
   city : str = "New York"