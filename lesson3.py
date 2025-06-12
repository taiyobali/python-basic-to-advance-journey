# class 3: about basic data_types,type() func, type_casting
# there are many data types in python
"""
number: integer,float,complex
boolean: bool
sequence: list,tuple,range,array,string
set: set, frozenset
mapping: dictionary
None type: None
binary: bytes,bytearray,memoryview
"""
# we will publish classes on each topic(data types)
# type() function: to know the data type
name = "Mark Zuckerberg"
print(type(name))
num = 230
print(type(num))
# type casting mean cast the data type into another type
# for type cast: int() float() complex() list() tuple() str() dict() set() bytes()......
num = 124 # int
n = float(num)
print(type(n))
data = "5421545" # str
new = int(data)
print(type(new))
