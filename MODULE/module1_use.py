import module1
print(module1.sum(10,20))
print(module1.mul(10,20))

print()

from module1 import sum
print(sum(4,5))

print()

from module1 import *
print(sum(4,5))
print(mul(4,5))

print()

import module1 as m
print(m.sum(3,8))
print(m.mul(3,8))