class Student:
    __name="vicky"

    def __displayinfo(self):
        print("Hello I am method")

    def __init__(self):
        print(self.__name)
        self.__displayinfo()

obj=Student()
