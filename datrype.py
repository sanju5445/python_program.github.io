# in progaraming data type is an important concept. variable can store data of different types can do differnet things
x=5
# print(type(x))
# time convert: we can convert from one data type to another
print("\n")
x=1
y=4.5
z=1j
# print(type(x))
# print(type(y))
# print(type(z))
a=float(x)
# print(a)
b=int(y)
# print(b)
# c=int(z) : we cant convert the complex datattpe
# print(z)


# random number: python doesn't have a random function to make a random  number,
# but python has a built module called random that can be used to make random number
import random
i=0
while(i<10):
   a=[(random.randrange(1,10))]
   print(a)
   i+=1


print(random.randrange(0,10))


# x=int('54')
# y=45
# sum=x+y
# print(sum)