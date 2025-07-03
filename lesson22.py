
# 25 build_in functions in python
# print() output func
print("data science")
print(54841)
# len() func , for lengths
data = [123,54,3.1416,True,"hello"]
print(len(data))
# input() func, for take input from user
name = input("enter your name: ")
print(f"hello,{name}")
# type(), isinstance(), for see the data type
name = "guido van rossum"
print(type(name))
print(isinstance(name,str))
# int(), float(), str() .... for type casting
x = "456"
n = int(x)
print(type(n))
# range() , generate sequence
for i in range(1,11):
    print(f"{i}.AI and ML")
data = list(range(1,6))
print(data)
# sum() func, for sum all items
data = [1,5,9,3,7,59,54,84,654,654,5487,547,2,6,8,5]
total = sum(data)
print(total)
total_100 = sum(data,100) #100+sum
print(total_100)
#list(), tuple() , type casting
data = list((54,68,65,254,54))
print(data)
print(type(data))
# set() func
data = set((564,65,3.14716,9.8))
print(data)
print(type(data))
# dict() func
# enumerate(), index+value
list_data = ["apple","banana","orange","pineapple"]
for i in enumerate(list_data):
    print(i)
# max(), min(), highest num and lower num
data = [1,5,9,3,7,59,54,84,654,654,5487,547,2,6,8,5]
data_max = max(data)
print(data_max)
data_min = min(data)
print(data_min)
# round()
pi = 3.1416
print(round(pi)) # 3
print(round(pi,2)) # 3.14
# any(), all()
bool_list = [True,False,True,False]
print(any(bool_list))
print(all(bool_list))
# slice()
data = [1,5,9,3,7,59,54,84,654,654,5487,547,2,6,8,5]
slice_list = data[slice(1,6)]
print(slice_list)
# chr(), ord()
print(ord("$"))
print(chr(65))
# zip() zip(A,B)
# sorted() accenting
data = [1,5,9,3,7,59,54,84,654,654,5487,547,2,6,8,5]
data = sorted(data)
print(data)
# 20. reversed() function
data = reversed(data)
print(data)
