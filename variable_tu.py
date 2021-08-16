x=5
y="jhon"
# print(x,y)

# cast
x=str('john')
y=str(5445)
print(x +'', y)

# print(type(x))
# print(type(y))
myVariableName='who am i'
# print(myVariableName)
a=54
b=54
c=a+b
print(c)
x,y,z=54,25,45
# print(x)
# print(y)
# print(z)
sum=x+y+z
# print(sum)
x=y=z='orange'
# print(x)
# print(y)
# print(z)
fruits=['apple','mango','guava']
x,y,z=fruits
print(x)
print(y)
print(z)


# global variable
x='AWESOME'
def fn():
    print("python is "+x)


# fn()


def fnn():
    global x
    x='awesome'



print("pythpn progrqam is " +x)

