
# class 10: about basic set type and dict type, swapping
# set item unchangeable, but we can add and remove,unordered,don't allow duplicate value
# only take int,float,complex,str,bool,tuple, item immutable, represent by {}
data = {123,65.50,True,"HELLO",(54,63,24587)}
print(type(data))
print(data)
# dict type data mutable,ordered(keys),don't allow duplicate keys, allow duplicate value
# for represent dict, {}, key: value
data = {
    "name": "Taylor",
    "Age": 18,
    "Dept": "ComputerE"
}
print(data)
print(type(data))
print(isinstance(data,dict))
# swapping
a = 50
b = 60
a,b = b,a
print(a)
print(b)
