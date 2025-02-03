#immutable
tpl=(4,2,7,4,9,0,1,0,7)
l=len(tpl)
for i in range(l):
    print(tpl[i])

print()

m=max(tpl)
print(f"{m}\n")

n=min(tpl)
print(f"{n}\n")

c=tpl.count(0)
print(f"{c}\n")

i=tpl.index(2)
print(f"{i}\n")
