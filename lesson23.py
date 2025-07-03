
# a function is an organized code block, reusable, and use for a specific work
"""
def fuc_name(parameters):
    statement
    return
fuc_name(value)
"""
def data():
    print("welcome to python programming")
data()

def name_data(name):
    data = f"HI, Welcome mr.{name}"
    return data
print(name_data("Taylor"))

def num_data():
    a = 20
    b = 50
    summ = a+b
    return summ
print(num_data())

def summ_data(a,b):
    summ = a+b
    return summ
print(summ_data(45,96))

def user_input():
    x1 = int(input("x1 = "))
    x2 = int(input("x2 = "))
    y1 = int(input("y1 = "))
    y2 = int(input("y2 = "))
    return (x1,y1), (x2,y2)
print(user_input())
r1,r2 = user_input()
print(r1)
print(r2)
xy,_ = user_input()
print(xy)

def sq_cube(x):
    sq = x**2
    cub = x**3
    return sq,cub
print(sq_cube(5))

def mulp1():
    x = int(input("x = "))
    y = int(input("y = "))
    multi = x*y
    return multi
print(mulp1())

def mulp2():
    total1 = mulp1()
    z = int(input("z = "))
    total2 = total1*z
    return total2
print(mulp2)

def country_name(country="Bangladesh"):
    data = f"HI, I'm from {country}"
    return data
print(country_name())
print(country_name("USA"))


def num_d(a,b=0):
    if a>b:
        return f"a = {a} is grater than b = {b}"
    elif a<b:
        return f"a = {a} is less than b = {b}"
    else:
        return f"a = {a} and b = {b} are same"
print(num_d(100,50))
print(num_d(50))
print(num_d(5,5))

def num_name(name_user):
    user = input("enter your user name: ")
    return user
print(num_name("taylor"))
