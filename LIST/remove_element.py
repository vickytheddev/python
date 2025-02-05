list=[10,60,40,90,30,50]
l=len(list)
for i in list:
    print(i,end=" ")

print("After removing an element")
list.remove(90)
for i in list:
    print(i,end=" ")