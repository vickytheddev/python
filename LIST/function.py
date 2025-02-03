marks=[90,80,85,75,70,80]

#slicing
print(marks[0])
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-5:-2]) 
print(marks[0::2])  
print(marks[-1::-2])  
print(marks[-1::-1]) 

marks.append(60)
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks.insert(3,20)
print(marks)

marks.remove(80)
print(marks)

print(marks.pop(3))
print(marks)

del marks[1]
print(marks)

marks[1]=10
print(marks)

n=[30,40,50]
marks.append(n)
print(marks)

marks.extend(n)
print(marks)

marks.clear()
print(marks)

list=[1,2,4,6,2,6,5,7]
c= list.count(2)
print(c)

m= max(list)
print(m)

n= min(list)
print(n)

list.sort()
print(list)

list.reverse()
print(list)

i=list.index(6)
print(i)

