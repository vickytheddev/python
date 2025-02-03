l=[10,20,30,40,50]
length=len(l)
print(length)

print()

#for n in range(length):
#    print(l[n])

for a in l:
    print(a)

print()

#reverse iterate
for n in range(length-1,-1,-1):  #last_index , first_index , decrement
    print(l[n])