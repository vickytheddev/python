#single inheritance
print("Single inheritance.....")
class A:
    def display_a(self):
        print("Hello I am parant class")

class B(A):
    def display_b(self):
        print("Hello I am child class")

obj=B()
obj.display_a()
obj.display_b()

print()

#multilevel inheritance
print("Multilevel inheritance.....")
class A:
    def display_a(self):
        print("Hello I am parant class")

class B(A):
    def display_b(self):
        print("Hello I am child class")

class C(B):
    def display_c(self):
        print("Hello I am clild of child")

obj=C()
obj.display_a()
obj.display_b()
obj.display_c()

print()
#multiple inheritance
print("Multiple inheritance.....")
class A:
    def display_a(self):
        print("Hello I am parant class")

class B():
    def display_b(self):
        print("Hello I am child class")

class C(A,B):
    def display_c(self):
        print("Hello I am clild of child")

obj=C()
obj.display_a()
obj.display_b()
obj.display_c()