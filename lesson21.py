
# enumerate(_) and search_replace from file in python
name = ["taylor","max","antonio","alex","delta"]
age = [18,19,17,20,19]
varsity = ["MIT", "Harvard", "Stanford", "California", "Florida"]
data = list(zip(name,age,varsity)) #zip iterable
print(data)
# unzip iterable--1
name1,age1,varsity1 = zip(*data) #unzip iterable
print(name1)
print(age1)
print(varsity1)
# index unzip--2
name = ["taylor","max","antonio","alex","delta"]
age = [18,19,17,20,19]
varsity = ["MIT", "Harvard", "Stanford", "California", "Florida"]
data = list(zip(name,age,varsity))
name1,age1,varsity1 = data[0:5] # unzip 0 to 5-1
print(name1)
print(age1)
print(varsity1)
# unzip by loop--3
data = zip(name,age,varsity)
for name1,age1,varsity1 in data:
    print(name1,age1,varsity1)
# unzip by loop and enumerate()
name = ["taylor","max","antonio","alex","delta"]
age = [18,19,17,20,19]
varsity = ["MIT", "Harvard", "Stanford", "California", "Florida"]
data = zip(name,age,varsity)
for index,pair in enumerate(data):
    name1,age1,varsity1 = pair
    print(f"index={index} name={name1} age={age1} varsity={varsity1}")
# file zip
import zipfile as zf
data = zf.ZipFile("zipfile2.zip","w")
data.write("excal.csv")
data.write("student_info.csv")
data.write("text1.txt.txt")
# for check
import zipfile as zf
print(zf.is_zipfile("zipfile2.zip"))  # True or False
#file unzip
import zipfile as zf
with zf.ZipFile("zipfile2.zip","r") as file:
    file.extractall("unzip_file1")
# search and replace in file in python
with open(r"text1.txt",'r') as file:
    data = file.read()
    data = data.replace('python','python programming')
with open(r"text1.txt",'w') as file:
    file.write(data)

text = ("Hello every one , I'm a new programmer in python programming. So what can I do right now."
        " I love python programming.  "
        "advise to be expert in python programming.")
import re
data = re.sub('python programming','python',text)
print(data)
