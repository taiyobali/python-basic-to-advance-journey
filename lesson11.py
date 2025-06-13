
# class 11: operators
# there are almost 7 types of operators in python
"""
Arithemetic operators: + - * / % ** //
Assignment operators: = += -= *= /= %= **= //= &= |= ^= <<= >>=
Logical operators: and or not
Comparison operators: == != > < >= <=
Bitwise operators: & | ~ ^ << >>
Identity operators: is, is not
Membership operators: in, not in
"""
x = 1254
y = 36599
print(x+y)
print(x*y)
print(y//x) #show only int value
print(y%x)  #reminder
import math
print(math.floor(y/x))
print(math.ceil(y/x))
x += 150  # x = x+150
y *= 5   # y = y*5
print(y>x and y>1000) # return True if both are. correct
print(x>y or y>x)  #return True if one/two correct
print(not(x>y and x>100)) # reverse
print(x==y)
print(x!=y)
print(y>=x)
x = 99
y = 90
print(bin(x)) # binary form
print(x&y)
print(x|y)
print(x<<5) #left shift x*(2**5)
print(x>>5) #right shift x/(2**5)
print(x is y) #same id() function
print(x is not y) # diff id()
list1 = [54,63,29,85]
print(54 in list1)  #membership
print(100 not in list1)
