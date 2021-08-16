class Student:
    def __init__(self,nam,age,address):
        self.name=nam
        self.age=age
        self.address=address
    def speak(self):
        print(f"hi i am {self.name} , i am {self.age} years old, and my address is {self.address}")

sanju=Student("sanju roy",22,"arambagh")
kali=Student("kali",54,"india")
# sanju.speak()
# kali.speak()
romesh=Student("romesh",45,"kannada ")
# romesh.speak()
# romesh.clas=9

# print(Student.__dict__)
# print(sanju.__dict__)

# romesh.speak()
# print(romesh.clas)
# print(sanju.__dict__)
# print(romesh.__dict__)

class Calculator(object):
    def __init__(self,n1,n2):
        # pass
        self.num=n1
        self.num2=n2
    @staticmethod
    def addition():
        sum=0

        n=int(input("how many number you want to add:"))
        for i in range(n):
            n1=int(input(f"enter the {i+1} number:"))
            sum+=n1

        return f"the addition of the given {i+1} numbers is: {sum}"
    def substraction(self):
        return f"the substraction of the given two numbers is : {self.num - self.num2}"
    def multiplication(self):
        return f"the multiplication of the given numbers is : {self.num*self.num2}"
    def division(self):
        return f"the division of the given numbers is: {self.num//self.num2}"
    def square(self):
         return f"the square of the given number is {self.num**self.num2}"
    def remainder(self):
        return f"the remainder of the given number is {self.num%self.num2}"


# n=Calculator(5,2)
# print(n.multiplication())
# print(n.division())
# print(n.substraction())
# print(n.addition())
# print(n.square())
# n1=Calculator(5,4)
# print(n1.multiplication())
# n=Calculator(10102611,467)
# print(n.addition())
# print(n.remainder())
"""
class Demo(object):
    def __init__(self):
        pass
    def call(self):
        a=Calculator.addition()
        print(a)
d=Demo()
d.call()
"""
def fn():
     """this is an empty function"""
# print(fn.__doc__)