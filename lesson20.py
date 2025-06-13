
# class 20: zip func and file zip
"""
iterableA(a,b,c)    iterableB(x,y,z)
zip(A,B) = ax,by,cz
"""
# iterable zip
name = ["asif","niloy","rahim","max","taylor"]
dept = ["zoology","chemical","marketing","Information","IT"]
age = [20,17,21,20,18]
data = zip(name,dept,age)
print(list(data))
print(tuple(data))
print(dict(data))
#iterable unzip
name1,dept1,age1 = zip(*data)
print(name1)
print(dept1)
print(age1)
# file zip
import zipfile as zf
data = zf.ZipFile("zip1.zip","w")
data.write("filename1")
data.write("filename2")
data.write("filename3")
# file unzip
import zipfile as zf
with zf.ZipFile("oldzip1.zip","r") as file:
    file.extractall("newfilename")
