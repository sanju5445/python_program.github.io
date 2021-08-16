
    # FIND THE EVEN NUMBER
def even(start,end):
    for i in range(start,end):
        if i%2==0:
            print(i)

    # FIND THE ODD NUMBER
def odd(start,end):
    for i in range(start,end):
        if i %2 !=0:
            print(i)

   # FIND THE ADDITION
def add(n):
    sum=0
    while n>0:
        x=int(input("enter the no:"))
        sum+=x
        n-=1
    print("the total no of the given no is :",sum)
# add(4)

# PRIME OR NOT
def prime_or_not(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(f"the given number {num} is not prime")
                print(i ,'times',num//i,'is',num)
                break
            else:
                print(f"the given number {num} is not a prime number")
    else:
        print("the given number is not a prime number")

# prime_or_not(450)
def factorial(factorial):
    fact=1
    if fact<0:
        print("sorry favtorial of negative number is not possible")
    elif factorial==0:
        print("factorial of 0 is 1")
    else:
        for i in range(1,factorial+1):
            fact*=i
        print(fact)
# factorial(5)

       #CHECK  ARMSTRONG NUMBER for 3 digit
def arm(num):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    if sum==num:
        print(f"the given no {num} is an armstrong number")
    else:
        print(f"the given no {num} is not an armstrong number")
# arm(407)

# CHECK ARMSTRONG NUMBER FOR N DIGIT
def armstrong(num):
    ord=len(str(num))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**ord
        temp//=10
    if sum==num:
        print(f"the given number {num} is an armstrong number")
    else:
        print(f"the given number {num} is not an armstrong number")

# armstrong(4077)

  # REVERSE A NUMBER
def reverse_number(n):
    rev=0
    while n!=0:
        digit=n%10
        rev=(rev*10)+digit
        n//=10
    print("the reverse of the given number is ",rev)
# rev(100)

   # COUNT NUMBER OF DIGITS IN AN INTEGER
def count(n):
    cn=0
    while n != 0:
        n//=10
        cn+=1
    print("number of digits",cn)
# count(1000045 )
a=5
b=a//10
print(b)

# FIBONACCI SERIES

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
# fib(7)

   # HCF OR GCD

def gcd(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
            break
    print(hcf)
# gcd(54,24)


#    REVERSE A STRING

def reverse_string(str):
    pass
    # print(str[::-1])
a="i am the best in the world"
words=a.split(" ")
x=[1,2,3,4,5,6,7]
# print(list(reversed(x)))
# print(' '.join(reversed(a)))
count=0
for i in a:
    count+=1
# print(count)

b=a.split(" ")
# print(b)
getlen=0
for i in b:
    y=len(i)
    getlen+=y
# print(getlen)



     # ADD NATURAL NUMBER
def add_serries(num):
    i=1
    sum=0
    while i<=num:
        sum=sum+i
        i+=1
    print("the sum of the given series is:",sum)
# add_serries(10)
#
# x=int(input("enter first number:"))
# y=int(input("enter the second number:"))
# z=int(input("enter the third number:"))
# if x>y and x>z:
#     print(f"({x}) is the largest number ")
# elif y>x and y>z:
#     print(f"({y}) is the largest number")
# else:
#     print(f"({z}) is the largest number")


def binn(num):
  a=[]
  while num>0:
     p=num%2
     a.append(p)
     num//=2
  print(a[::-1])

# binn(45)



n=int(input("enter a number: "))
print(bin(n)[2:])
print(type(bin(n)))


