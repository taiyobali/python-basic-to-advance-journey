
# class 12: if, elif, else conditional statement
# we need to follow indentation rules
"""
Block1
    Block2
        Block3
        Block3
    Block2
Block1
"""
"""
if expression1: 
    statement1
    if expression2:
        statement
    elif expression2:
        statement
    else:
        statement
elif expression1:
    statement
    ..........
else: 
    statement
"""
x = int(input("enter your num1: "))
y = int(input("enter your num2: "))
z = int(input("enter your num3: "))
if x>y and x>z:
    print(f"x is greater than all {x}")
elif y>x and y>z:
    print("y is greater than")
else:
    print("z is greater than")
# electricity bill program
total_input_unit = int(input("Enter your unit: "))
total_unit_bill = 0
if total_input_unit<=100:
    total_unit_bill = total_input_unit*12
elif total_input_unit<=200:
    total_unit_bill = (100*12)+(total_input_unit-100)*15
elif total_input_unit<=500:
    total_unit_bill = (100*12)+(100*15)+(total_input_unit-200)*18
else:
    total_unit_bill = (100*12)+(100*15)+(300*18)+(total_input_unit-500)*22
vat = (total_unit_bill*5)/100
total = total_unit_bill+vat
discount = 0
if total>2000:
    discount = (total*0.1)
else:
    discount = 0
total_bill = total_unit_bill+vat-discount
print(f"Your bill without vat: {total_unit_bill}")
print(f"Your electricity vat: {vat}")
print(f"Your discount on bill: {discount}")
print(f"Your total bill: {total_bill}")
