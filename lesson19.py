
# class 19: array data type
# array almost like list(mutable,ordered,allow duplicate value,[],9methods)
# array only take one data type at a time
import array as ar
data = ar.array('i',[32,65,98,785,562,369,877])
print(data)
print(type(data))
# 'i' = int, 'f' = float, 'u' = unicode...
data2 = ar.array('f',[3.1416,9.8,6400.0])
print(data2)
print(type(data2))
