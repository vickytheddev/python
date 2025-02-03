cource={
    "php":{"duration":"2Months","fees":"15000","use":"most"},
    "python":{"duration":"2Months","fees":"55000","use":"most"},
    "java":{"duration":"2Months","fees":"10000","use":"most"},
}

print(f"{cource}\n")
print(f"{cource["php"]}\n")
print(f"{cource["php"]["fees"]}\n")

for i,j in cource.items():
    print(i,j)

print()

for i,j in cource.items():
    print(i,j["duration"],j["fees"])

print()

cource["java"]["fees"]="12000"
for i,j in cource.items():
    print(i,j)
