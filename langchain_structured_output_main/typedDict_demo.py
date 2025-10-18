from typing import TypedDict

class Person(TypedDict):

    name : str
    age : int

persom : Person = {'name':'suraj','age':24}

# in short in typed dict it shows that what should be the data type of the given key and value 
# like age should be int

print(persom)