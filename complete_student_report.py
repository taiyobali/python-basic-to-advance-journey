
# class 24
# student report analysis program (small project)
# step 1
number = int(input("How many student want to add: "))
name = []
roll = []
clas = []
phone = []
math = []
physics = []
chemistry = []
highest = []
lowest = []
total = []
average = []
result = []
grade = []

for i in range(1,number+1):
    print("\n")
    print(f"Student data {i} ")
    print("\n")
    na = input("Name: ")
    ro = int(input("Roll: "))
    cla = int(input("Class: "))
    pho = input("Phone: ")
    mat = float(input("Math: "))
    phy = float(input("Physics: "))
    che = float(input("Chemistry: "))

    # step 2
    all_sub = mat,phy,che
    high = max(all_sub)
    low = min(all_sub)

    tot = sum(all_sub)
    ave = round(tot/3)

    # step 3
    if mat<33:
        result.append("Fail ❌ ")
    elif phy<33:
        result.append("Fail ❌ ")
    elif che<33:
        result.append("Fail ❌ ")
    else:
        result.append("Pass ✅ ")

    if ave<33:
        grade.append("F")
    elif (ave>= 33) and (ave<=50):
        grade.append("D")
    elif (ave>= 51) and (ave<=70):
        grade.append("C")
    elif (ave>= 71) and (ave<=80):
        grade.append("B")
    elif (ave>= 81) and (ave<=90):
        grade.append("A")
    else:
        grade.append("A+")

    name.append(na)
    roll.append(ro)
    clas.append(cla)
    phone.append(pho)
    math.append(mat)
    physics.append(phy)
    chemistry.append(che)
    highest.append(high)
    lowest.append(low)
    total.append(tot)
    average.append(ave)

# step 4
student_data = []
for n,ro,c,p,m,phy,che,h,l,t,a,re,g in zip(name,roll,clas,phone,math,physics,chemistry,highest,lowest,total,average,result,grade):
    data = {
        "Name": n,
        "Roll": ro,
        "Class": c,
        "Phone": p,
        "Math": m,
        "Physics": phy,
        "Chemistry": che,
        "Highest": h,
        "Lowest": l,
        "Total": t,
        "Average": a,
        "Result": re,
        "Grade": g
    }
    student_data.append(data)

print(f"Student Info. {student_data}")
print("\n")
for i in student_data:
    print(i)

# step 5
for index,student in enumerate(student_data):
    print("\n")
    print(f"student info. {index}")
    print("\n")
    print(f"Name: {student["Name"]}")
    print(f"Roll: {student["Roll"]}")
    print(f"Class: {student["Class"]}")
    print(f"Phone: {student["Phone"]}")
    print(f"Total: {student["Total"]}")
    print(f"Average: {student["Average"]}")
    print(f"Result: {student["Result"]}")
    print(f"Grade: {student["Grade"]}")

print("program finished! Congratulation ✅✅")
