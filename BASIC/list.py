#mutable
#[ ]
#,
#use indexing 0...

marks=[90,80,85,75,70,80]
print(marks[0])

#list method
print("\nlist method\n")

print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-5:-2])  #negative indexing
print(marks[0::2])  #start to end increment
print(marks[-1::-2])  #end to start decrement
print(marks[-1::-1]) #reverse

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

#mixed list
list2=["vicky","mumbai","uvpce",1,5,2,3,5]
print(list2)


#nested list
list=[1,2,3,[5,6,7]]
print(list[0])
print(list[3])
print(list[3][1])