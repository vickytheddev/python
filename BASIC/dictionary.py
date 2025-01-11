#mutable
dict={
    "name" : "vicky",
    "subject" : ["python","c","java"],
    "topic" : ("dict","set"),
    "age" : 20,
    "isadult" : True,
    "percentage" : 77.6
}

print(dict)

dict["name"]="pintu"  #overwrite
dict["surname"]="yadav"

print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))

new_dict ={"cityname":"mumbai"}
dict.update(new_dict)
print(dict)