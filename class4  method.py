     # ALTERNATIVE CAONSTRUCTOR

class Student:
    def __init__(self,nam,age,address):
        self.name=nam
        self.age=age
        self.address=address
    def speak(self):
        return f"hi i am {self.name} , i am {self.age} years old, and my address is {self.address}"
        # return "thanks for using"
    @classmethod
    def from_slash(cls,str):
        return cls(*str.split("/"))
        # a=str.split("/")
        # return cls(a[0],a[1],a[2])
    @classmethod
    def from_dash(cls,str):                                                 #ALTERNATIVE CONSTRUCTOR
        # a=str.split("-")
        # return cls(a[0],a[1],a[2])
         return cls(*str.split("-"))
    @classmethod
    def from_space(cls,str):
        a=str.split(" ")
        return cls(*a)


     # ALTERNATIVE CONSTRUCTOR                                              #ALTERNATIVE CONSTRUCTOR


ram=Student("sanju roy",25,"arambagh")
sam=Student("kali",45,"kolkata")
rohit=Student.from_slash("rohit/22/kannada")
arjun=Student.from_dash("arjun-25-kolkata")
# print(ram.speak())
# print(sam.speak())
# print(rohit.speak())
# print(arjun.speak())

t=Student.from_space("simi 15 canada")
# print(t.speak())



                        # STATIC METHOD


class Employee:
    def __init__(self,nam,age):
        self.name=nam
        self.age=age
    def speak(self):
        print(f"hi i am {self.name} , i am {self.age} years old")

    def greet(self):
        print(f"this is a good {self.name} ")

    @staticmethod
    def print_good():
        print("thanks for use me!!!")


# Employee.greet()
# Employee.greet()
e2=Employee("harry",27)
e2.speak()
Employee.print_good()
e2.print_good()

