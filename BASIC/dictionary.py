#mutable
#key value pair

dict={
    "name" : "vicky",
    "subject" : ["python","c","java"],
    "topic" : ("dict","set"),
    "age" : 20,
    "isadult" : True,
    "percentage" : 77.6
}
print(type(dict))

print(dict)

print(dict["name"])

print()

dict["name"]="pintu"  #overwrite
dict["surname"]="yadav" #add new key value
print(dict)

print()

print(dict.keys())
print()
print(dict.values())
print()
print(dict.items())
print()
print(dict.get("name"))

print()

new_dict ={"cityname":"mumbai"}
dict.update(new_dict)  #add new key value
print(dict)

