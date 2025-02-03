dict={
    "name" : "vicky",
    "subject" : ["python","c","java"],
    "topic" : ("dict","set"),
    "age" : 20,
    "isadult" : True,
    "percentage" : 77.6
}

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))

print()

for k in dict.keys():
    print(k)

print()

for v in dict.values():
    print(v)

print()

for i,j in dict.items():
    print(i,j)

print()

del dict["age"]
print(dict)

print()

print(dict.pop("percentage"))
print(dict)

print()

dict.update({"topic":("java","python")})
print(dict)

print()

dict["cource"]="Btech"
print(dict)

dict["subject"]="python"
print(dict)