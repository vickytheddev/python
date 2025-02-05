class Student:
    def __init__(self):
        self.__name=""

    def getname(self):
        return self.__name
    
    def setname(self,name):
        self.__name=name

obj=Student()
obj.setname("vicky")
k=obj.getname()
print(k)

    