
# class 14: break,continue,pass control statement
"""
syntax
for i in iterable:
    if condition:
        break/continue
while condition:
    if condition:
        break/continue
"""
for i in range(1,100):
    if i==11:  #loop stop forever
        break
    print(f"{i}*17 = {i*17}")
x = 1
while x<=100:
    if x==11:
        break
    print(f"{i}*12 = {i*12}")
    x += 1
for i in range(1,100):
    if i%2==1:
        continue # just skip those iterations
    print(i)
x = 1
while x<100:
    if x%2==1:
        continue
    print(x)
    x += 1
for i in range(100):
    pass # for skip error and future code
x = 1
while x==10:
    pass
