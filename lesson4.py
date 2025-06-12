# class 4: number type data(int,float,complex)
num1 = 450 # int type
num2 = 65.45 # float type
num3 = 3+5j # complex type x+yj
# we can use type() or isinstance() to know the data type
print(type(num1))
print(isinstance(num2,float)) # return True or False
# some operation and casting
subt = num1-num2
summ = num1+num3
multip = num1*num3
print(subt)
print(summ)
print(multip)
n = float(num1)
print(type(n))
n2 = complex(num2)
print(n2)
# int to float/complex, float to int/complex are possible but complex to others don't
