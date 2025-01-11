#mutable
marks=[90,80,85,75,60]
print(marks[0])
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-5:-2])

#list method
print("\nString method\n")
marks.append(60)
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks.insert(3,60)
print(marks)

marks.remove(80)
print(marks)

marks.pop(3)
print(marks)


list2=["vicky","mumbai","uvpce",123]
print(list2)