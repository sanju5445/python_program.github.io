# class Student:
#     no_of_leaves=10
#     salary=500000
#
# s1=Student()
# s2=Student()
# s1.name="sanju roy"
# s1.age=22
# s1.role="machine learning engineer"
#
# s2.name="kali"
# s2.age=25
# s2.role="hacker"
# print(s1.name, s1.role)
# # print(s2.__dict__)
# print(s2.no_of_leaves)
# print(Student.no_of_leaves)
# s2.no_of_leaves=9
# print(s2.no_of_leaves)
# print(s1.no_of_leaves)
# print(Student.no_of_leaves)
#
# print(s1.salary)
# print(s2.salary)
# s2.salary=45000
# print(Student.salary)
# print(s1.salary)
# print(s2.salary)
# print(s1.__dict__)
# print(s2.__dict__)


         # ASBOUT SELF
class Employee:
    age=54
    def pd(self):
        print(f" Your Name is {self.name},\n salary is {self.salary},\n role is {self.role}")
    pass


sanju=Employee()
kali=Employee()
sanju.name="sanju roy"
sanju.salary=50000
sanju.role="Machine Learning Engineer"

kali.name="kali"
kali.salary=5445
kali.role="Hacker"

# print(sanju.role,sanju.salary)
# sanju.pd()
# print(sanju.__dict__)
# print(Employee.__dict__)


class Student:
    """this is a database to store student details of kalyani government engineering college"""
    college="Kalyani Engineering College"
    def __init__(self,sname,srole,sadd):
        self.name=sname
        self.role=srole
        self.add=sadd

    def prdet(self):
        return f"your name is {self.name}, and role is {self.role}, and address is {self.add}"
s1=Student("kali","hacker","kolkata")
# s2=Student()
# s3=Student()
print(s1.prdet())
