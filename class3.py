class calculator:
    def addition(self,*n):
        sum=0
        for i in n:
            sum+=i
        return sum
# a=calculator()
# a.addition(10,20,30)



class xyz:
    no_of_leaves=9
    def __init__(self,name,salary,role):
        self.name=name
        self.salray=salary
        self.role=role
    def det(self):
        print(f"the name is {self.name},salary is {self.salray}, role is {self.role}")

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

a=xyz("sanju",54,"hacker")
b=xyz("aa",45,"sajfh")
# a.det()
# print(a.no_of_leaves)
# print(b.no_of_leaves)
# print(xyz.no_of_leaves)
# a.change_leaves(45)
# print(a.no_of_leaves)
# print(b.no_of_leaves)
# print(xyz.no_of_leaves)


class Person:
    def __init__(my,name,age):
        my.name=name
        my.age=age
    def greet(ab):
        print(f"The name is {ab.name}, and age is {ab.age}")
    @staticmethod
    def gr():
        print("thanks for using me!!")

p1=Person("sanju roy",25)
# p1.greet()






class Person2:
    def __init__(self,name):
        self.name=name
    def printname(self):
        print(f"THIS IS {self.name}")
        a=Person.gr()
        return a

                                            # SUB CLASS
class Student(Person2):
    pass
c=Person2("sanju")
c.printname()
# print(c.name)