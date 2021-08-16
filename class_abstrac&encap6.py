class Employee:
    company_name='TCS'
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
    def speak(self):
        return f"hi i am {self.name} , i am {self.role}, and my salary is {self.salary}"
    @staticmethod
    def fn():
        return "thanks for using me"
sanju=Employee("sanju roy","machine learning engineer",555)
kali=Employee("kali","hacker",545)
sanju.speak()

                         # INHERITANCE         INHERITENCE        INHERITENCE

class Programmer(Employee):
    def __init__(self,name,role,salary,languages):
        self.name = name
        self.role = role
        self.salary = salary
        self.languages=languages
    def spk(self):
        return f"hi i am {self.name} , i am {self.role}, and my salary is {self.salary} and i know  {self.languages} languages"

s1=Programmer("rakesh","developer",525,['python','java'])
s2=Programmer("rahim","front_end_developer",545,['python','cp'])
print(s1.company_name)
print(s1.spk())
print(s1.languages)
def jj():
   for i in (s1.languages):
      print(i)
      for j in i:
         print(j)

print(s1.fn())




