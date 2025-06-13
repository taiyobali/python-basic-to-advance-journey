
# class 6: basic boolean and sequence type data
# bool type data mean True, False
x = True
y = False
print(type(x))
print(isinstance(y,bool))
num1 = 50
num2 = 70
print(num1<num2)
print(num1==50)
print(num2<num1)
print(type(num1<=num2))
# sequence: list, tuple , range, array, str(completed)
# list type data mutable, ordered, allow duplicate value, allow all data types
# for represent list [], list(())
list_1 = [12,50,80.50,True,"Hello",5+6j,[54,26,987],(541,9544.4,445)]
print(list_1)
print(type(list_1))
print(list_1[2])
print(list_1[-1][2])
list_1[1] = "ML"
print(list_1)
list_2 = list((54,875,9.54))
print(type(list_2))
print(list_2)
# tuple immutable, ordered, allow duplicate value, allow all data types, (), tuple(())
data = (12,52,85.54,True,"HI",{54,69,454})
print(data)
print(type(data))
print(data[2])
# range
for i in range(5): #0 to 5-1
    print(i)
for i in range(2,20,3): # 2 to 20-1, increasing 3
    print(i,"I'm programmer")
# array type almost like list ,it can take one data type at a time
import array as ar
data = ar.array("i",[54,85,96,34,57,841])
print(data)
print(type(data))
# str type already completed
