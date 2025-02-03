l1=[1,2,3,4,5]
l2=[5,4,3,2,1]

for a,b in zip(l1,l2):
    print(a,b)

print()

#another method
t=len(l1)
for h in range(t):
    print(l1[h],l2[h])