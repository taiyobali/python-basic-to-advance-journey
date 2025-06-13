
# class 16: dict data structure and methods
# dictionary is a mutable, ordered(keys), don't allow duplicate keys,allow duplicate value
# for represent dict , {}
data = {
    "name": "Taylor",
    "age": 18,
    "subject": "CS"
}
print(data)
print(isinstance(data,dict))
print(data["name"])
data["subject"] = "data science"
data["married"] ="NO"
print(data)
# there are almost 9 methods for dict type
# copy() update() keys() values() items() get() pop() clear() del
data2 = data.copy() #for copy
print(data2)
data3 = {
    "area":"asia",
    "gender": "male"
}
data.update(data3) #use to extend two dict or add items
print(data)
print(data.keys())
print(data.values())
print(data.items())
print(data.get("name"))
print(data.pop("gender"))
del data["area"]
print(data)
data.clear()
print(data)
# dict input
total_input = int(input("how many num you want to add: "))
dict_data = {}
for i in range(total_input):
    key = input(f"enter your key{i}: ")
    value = input(f"enter your value{i}: ")
    dict_data[key] = value
print(dict_data)
