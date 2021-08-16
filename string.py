a='hello'
b="hello"
# print(a,b)

                   # multiline string

ab=""" the quick brown fox jumps over the lazy dog... i am the beswt in the world... why we say sorry its doesn't mean that we are wrong 
        its just mean that we value the person  and the relationship more than being right.... we have to choose what we want being right or love """
# print(ab)
x="""
*
**
***
****
*****
******
*******
********

"""
# print(x)





# strings are arrays

a="hello,world"
# print(a[6:11])

z='banana'
for i in z:
    pass
    # print(i)
# string leangth

 # checking a string is present or not
# print(len(a))

str = " the quick brown fox jumps over the lazy dog "
# print('fox' in str)


if "the" in str:
    pass
    # print("yes 'the' is present" )
# print("fox" not in str)
if('zo' not in str):
    pass
    # print("no not in string")


  # slicing string

a="hello world"
# print(a[2:5])
# print(a[:1])



# modify string

# python ahs a set of built in method that we can use on strings..
# upper case
# print(a.upper())
b="          WHO AM I"
# print(b.capitalize())
# print(b.lower())

# remove whitespace
# print(b.strip())


# print(b.replace("AM I","ARE WE"))
# print(b.replace(" ","$"))
str="i am the best in the world"
# p=(str.split(","))
# print(p)
# print(p[0])
# print(str.split(","))


# string concatenation


a="hello"
b="world"
c=a+ b
# print(c)
# print(f"{a} {b}")


# print("i am the besy in\t the \bwor\nld")


          # string excercise   #string excercise       string excercise      string excercise        string excercise

# chheck wheather a string is palindrome or not
def palindroem(a):
    # a = input("enter a string to check whether it palindrome or not :")
    mid = (len(a) - 1) // 2
    # print(len)
    # print(a[4])
    lst = len(a) - 1
    # print(lst)
    # print(a[9])
    flag = 0
    fst = 0
    while (fst <= mid):
        if (a[fst] == a[lst]):
            fst += 1
            lst -= 1
        else:
            flag = 1
            break;

    if flag == 0:
        print("the given string is a palindrome")
    else:
        print("the given string is not palindrome")


# x=input("enter the string to check its palindrome or not: ")
# palindroem(x)

def symmetric(b):
    mid=(len(b)-1)//2
    fst=0
    lst=len(b)-1
    flag=0
    n=mid
    while(fst<=mid):
        if(b[fst]==b[lst-n]):
            fst+=1
            n-=1
        else:
            flag=1
            break;


    if(flag==0):
        print("the given string is symmetric")

    else:
        print("the given string is not symmetric")


# y=input("enter a string to check whether its symmetric or not: ")
# symmetric(y)





# reverse words in a given string in python

def rev_sen(sentence):
    words=sentence.split(' ')
    rev_sen=' '.join(reversed(words))
    # print(rev_sen)
    return rev_sen




# a=input("enter a string to rreverse:")
# print(rev_sen(a))

# xx="i am the best in the world"
# yy=(xx.split(' '))
# print(yy)
# rev=' '.join(reversed(yy))
# print(rev)



# find the length of a given string
def findLen(str):
    count=0
    for i in str:
        count+=1
    return count

# while(True):
    # x=input('Are you want to continue:Y/N\n')
    # if(x=='y' or x=='Y'):
    #    a=input("enter a string to check its length:")
    #    print(f"the length of the given string '{a}':",findLen(a))
    # elif(x=='n' or x=='N'):
    #    exit(0)
    # else:
        # print("you enter a wrong key")


 # find the string length ignore the space
# str =input("enter a string: \n")

strOn = str.split(" ")

# print(strOn)

getLen = 0
y = 0

for x in strOn:
    y = len(x)
    getLen += y


# print('Length => ', getLen)

def getlen(str):
    count=0
    for x in str:

        count=count+1
    return count



