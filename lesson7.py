
# class 7: binary type and None type data
# None type mean value null
x = None
print(type(x))
# binary type: bytes,bytearray,memoryview
# bytes immutable,ordered,allow duplicate value, range 0-255, bytes()
my_list = [2,8,69,120,54,3,78,120,200,213,245,255]
data = bytes(my_list)
print(data)
print(type(data))
print(data[2])
# bytearray mutable,ordered,allow duplicate value, range 0-255, bytearray()
my_list = [2,8,69,120,54,3,78,120,200,213,245,255]
data = bytearray(my_list)
print(data)
print(type(data))
print(data[2])
data[2] = 100
print(data[2])
my_str = "basic python for everyone"
my_data = bytearray(my_str,"utf-8") #for str type data "utf-8"
print(my_data)
print(type(my_data))
my_data[0] = ord("B")
print(my_data)
# memoryview mutable,ordered, only cast from bytes and bytearray
my_str = "basic python for everyone"
my_data = bytearray(my_str,"utf-8")
mv = memoryview(my_data)  #memoryview type data
print(mv)
print(type(mv))
print(mv[2])
mv[6] = ord("P") # for string: ord()
print(mv)
