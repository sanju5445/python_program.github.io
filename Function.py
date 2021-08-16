# def greeting(name):
#     print("hello",name +" good morning")
#     print("whats going on!!")
#
# # greet('sanju')
# def add(x,y):
#     sum=x+y
#     print("the sum of the given two number is:",sum)
# # add(25,25)
#
# def greet(name,msg):
#     print("hello", name +" ," +msg)
# # greet('sanju','who are you?')
# # # greeting('sanju')
# def greet(name='kali',msg="good morning!!"):
#     print('Hey',name+" , "+msg)
# greet('sanju','who are you??')
# greet(name='pritam',msg="are you know who am i !!1")
# greet('sanju',msg='how are you')
# greet(name='sanju',msg='who are you')

# def fn(x,y,z):
#     pass
# fn(2,5,'hell')
#
# def greet(*names,msg):
#     print('hello', names , msg)
# greet('pradip','sanju','sandip','sourav','sudip',msg='good morning to all')




# ANONYMOUS FUNCTION

# def square(n):
#     return n*n

sqr=lambda x:x*x
# print(sqr(5))
# print(square(6))
summ=lambda a,b,c:a+b+c

# print(summ(25,25,50))


# Recursion
def sum(n):
    if n==1:
      return 1
    else:
       return n +sum(n-1)
# print(sum(10))
s="i am the best in the world"
def gl(str):
    l = 0
    y = 0
    word = str.split()
    for i in word:
        y = len(i)
        l = l + y
    print("the length of the given string without space is", l)


def leng(str):
    count = 0
    for i in str:
        count += 1
    print("the length of the given string is", count)
