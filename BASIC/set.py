
collection={1,2,3,4,5,6,5,6,"hello","hello"}
print(collection)
print(len(collection))
#empty set

collection1=set()
print(type(collection1))

#set method
collection1.add(1)
print(collection1)
collection1.add(2)
collection1.add(3)
collection1.add((1,2,3,4,5))
collection1.remove(3)
print(collection1)

print(collection1.pop())
print(collection1.pop())
print(collection1)

collection1.clear()
print(collection1)


set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.union(set2))
print(set1.intersection(set2))
