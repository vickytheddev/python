import random
r=random.randint(2,3)  #include 2 and 3
print(r)

n=random.randrange(2,3)  #exclude 3
print(n)

l=[10,20,30,40]
lc=random.choice(l)
print(lc)

b=random.random()  #return value between 0 and 1
print(b)

k=[1,2,3,4,5,6]
random.shuffle(k)
print(k)

u=random.uniform(3,9) #return float value between 3 and 9
print(u)


