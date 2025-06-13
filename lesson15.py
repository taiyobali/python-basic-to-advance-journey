
# class 15: list data structure and comprehension
# list is a mutable, ordered, allow duplicate value, allow all data types,
# for represent list , [] , list(())
list1 = [12,54,63.65,True,"HELLO",{54,69,324},(545,96,565,54)]
print(list1)
print(isinstance(list1,list))
print(list1[2])
print(list1[-1][2])
list1[1] = "CSE"
print(list1)
list2 = list((987,654,"English",6+6j))
print(type(list2))
# there are almost 12 methods for list type
"""
copy() append() insert() extend() index() count() 
sort() reverse() remove() pop() clear() del
"""
data = [450,36.22,True,"Hello world",2,2,(54,87,6+6j),{547,3.25,"program"}]
list3 = data.copy()
print(list3)
data.append(2025)  #add item at the last index
print(data)
data.insert(0,"I'm determined") #add item by index
print(data)
list4 = [1,2,3,4,5,11,15,18]
list5 = [6,7,8,9,10,12,20,35,40,21,23,19]
list4.extend(list5) #list1+list2
print(list4)
# new_list = list4+list5
print(data.index(True))
print(data.count(2))
list4.sort()  #accending
print(list4)
list4.sort(reverse=True) #decending
print(list4)
data.reverse() #reverse
print(data)
data.remove(450)
print(data)
print(data.pop(2)) #remove by index
del data[3] #remove
print(data)
data.clear() #all remove
print(data)
# list comprehension
# syntax [expression for i in iterable if condition(optional)]
my_data = [i**2 for i in range(100) if i%2==0]
print(my_data)
data = "basic python for mine"
data = data.split()
list6 = [i for i in data]
print(list6)
list7 = [len(i) for i in data]
print(list7)
matrix = [[j for j in range(5)] for i in range(3)]
