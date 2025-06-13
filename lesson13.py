
# class 13: for loop and while loop
"""syntax1  
for i in iterable:
    statement
syntax2
var = ...
while condition:
    statement
"""
for i in range(2,20):
    print(f"{i},I'm a programmer")
data = "basic python for mine"
data = data.split()
for i in data:
    print(i)
for i in range(len(data)):
    print(data[i])
# summation
total_input = int(input("how many num do you want to add: "))
total = 0
for i in range(total_input):
    num = float(input(f"enter your num{i}:"))
    total += num
print(total)
# while loop works by conditions
total_input = int(input("how many num you want to add: "))
total = 0
count = 1
while count<=total_input:
    number = float(input(f"enter your num{count}:"))
    total += number
    count += 1
print(f"your summation is {total}")
# Nested loop, first outer loop then inner loop
# shape create
num = int(input("enter row: "))
for i in range(num):
    for x in range(i):
        print("#",end=" ")
    print("\n")

list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    index = 0
    while index<len(list1):
        for x in range(i):
            print(i,end=" ")
        index += 1
    print("\n")
