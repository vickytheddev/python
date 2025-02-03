l=[]
for a in range(1,101):
    l.append(a)
print(l)

print()

n=[h for h in range(1,101)]  #pass int value in list
print(n)

print()

n=[h for h in range(1,101) if h%2==0]  #after using filter
print(n)

print()

str="vicky"  #pass string in list
k=[g for g in str]
print(k)