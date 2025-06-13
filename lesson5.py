
# class 5: string type data and all methods
# for represent string, we need to use ""/''
data = "basic python for mine! Data Science fun!"
print(type(data))
print(isinstance(data,str))
print("Hello world",data)
print("I'm a" + " programmer")
import sys
print(sys.getsizeof(data))  #for size
print(id(data))
print(len(data))
# there are almost 20 methods for string
print(data.count("i")) #for count any string
print(data.find("for"))  #to see the index of any string
print(data.index("p")) # almost same like find
print(data.lower()) #to cast in lower case
print(data.casefold()) # same like lower
print(data.upper())  #to convert in upper case
print(data.capitalize())  #only first word capital
print(data.swapcase())  #small to upper and upper to small
print(data.title())  # title
print(data.islower())  # to check the case
print(data.isupper())  # to check the case
print(data.isdigit())   # to check the case
print(data.encode())  #bytes
print(data.split())  #just like list type
print(data.center(100))   #the string stay center
print(data.replace("mine","everyone"))
print(data.strip("!"))  #for remove something
print(" ".join(data))  #to add something
print(f"Are you agree with {data}")  #formet methods
# others \, ordered, indexing
print("I love \"Programming\" so much")  #after \, '' "" doesn't execute
print("\\\\") #\\ = \
data = "basic python for mine! Data Science fun!"
#       0123456...... index
print(data[2])
print(data[0:6])  # 0 to 6-1
print(data[-1])  # last
