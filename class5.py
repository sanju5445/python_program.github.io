class A(object):
    def __init__(self):
        pass
    def methoda(self):
        print("this is a methoda")
        return "2"
    def methodc(self):
        d=self.methoda()
        print(f"this is coming from methoda {d}")
        ob=B()
        d1=ob.methodb()
        print(f"this is coming from methodb {d1}")
class B(object):
    def __init__(self):
        pass
    # @staticmethod
    def methodb(self):
        print("this is a methodb")
        return "3"

# o=A()
# print(o.methoda())
# o.methodc()
# class x:
#    def fn(self):
#     print("heyy!!!! ghow are you ???")
#     input(":>")
#     return 25
# c=x()
# a=c.fn()
# print(f"the return value of the given number is: {a}")


from class2 import *

# a=Calculator.addition()
# print(a)
b=Calculator(5,2)
# print(b.square())




class xyz:
    role="Hacker"
    def __init__(self,name,salary):
        self.name=name
        self.salray=salary
    def det(self):
        print(f"the name is {self.name},salary is {self.salray}, role is {self.role}")

    @classmethod
    def chro(cls,rle):
        cls.role=rle


# a=xyz("sanju",45)
# b=xyz("kali",54)
# a.det()
# b.det()
# print(b.__dict__)
# print(xyz.__dict__)
# # a.role="developer"
# print(a.__dict__)
# a.chro("developer")
# a.det()
# b.det()
# print(xyz.role)
