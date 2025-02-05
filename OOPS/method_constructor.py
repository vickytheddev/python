class Demo:
    a=10
    b=20

    def __init__(self):
        print("I am constructor")
        
    def showvalue(self):
        print(self.a)

    def addvalue(self):
        print(self.a + self.b)

    def addthreevalue(self,c):
        print(self.a + self.b + c)

obj=Demo()
obj.showvalue()
obj.addvalue()
obj.addthreevalue(30)
