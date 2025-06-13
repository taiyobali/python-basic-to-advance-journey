
# class 8: input() function
name = input("enter your name: ")
print(f"HI, {name}")
# all type take as a str, but we can cast
num1 = int(input("enter your num:"))
num2 = int(input("enter your num:"))
summ = num1+num2
print(summ)
num3 = float(input("enter any num: "))
num4 = float(input("enter any num: "))
multi = num3*num4
print(multi)
user_n = input("enter your user name: ")
user_p = input("enter your password: ")
print(f"Welcome {name}, your user name is {user_n} and password {user_p}")
x,y,z = input("enter 3 word: ").split() #for multiple input in a line
print(x,y,z)
# summation and average program
total_input = int(input("How many num do you want to add: "))
total = 0
count = 1
while count<=total_input:
    num = float(input(f"enter num {count}: "))
    total += num
    count += 1
aver = total/total_input
print(f"your summation is {total} and average is {aver}")
