# lst=['apple','mango','guava','orange','banana']
# print(type(lst))
# print(len(lst))
# for i in lst:
#     print(i)

# for i in range(len(lst)):
    # print(lst[i])
# i=0
# while i<len(lst):
#     print(lst[i])
#     i+=1
# [print(x) for x in lst]

lst1=[45,40,'apple',54,'mango',78,True,85,65]
# print(lst1)
# for i in lst1:
#     print(i)

# for i in range(len(lst1)):
#     print(lst1[i])
#     print(i)
lst=['apple','mango','guava','orange','banana']
# print(lst[0])
# print(lst[:])
# lst.clear()
# print(lst)
# if 'orange' in lst:
#     print("yes")
lst.insert(2,'xyz')
# print(lst)
lst.append("xxx")
# print(lst)
# lst.extend(lst1)
# print(lst)
# print(lst1)
# lst1.remove(True)
# print(lst1)
# lst.pop(2)
# print(lst)
# del lst1[2]
# print(lst1)
# lst.pop()
# print(lst)
# del lst1
# print(lst1)
lst.remove('xxx')

# print(lst)
# print(lst)
newst=[]

for x in lst:
    if 'a' in x:
        newst.append(x)
# print(newst)
newst.clear()
# for x in lst:
#     if x!="apple":
#          newst.append(x)
#
# for x in lst:
#     newst.append(x)
# print(newst)
# for x in range(10):
#     newst.append(x)
# print(newst)
# for x in range(10):
#     if x<5:
#         newst.append(x)
# print(newst
for i in lst:
    newst.append(i.upper())
# print(newst)
n=[]
# for x in lst:
#     n.append('hello')
# print(n)
for x in lst:
    if x!="xyz":
        n.append(x)
    else:
        n.append('cherry')
# print(n)
# lst.sort()
# print(lst)
n=[100,25,75,65,85,74]
# print(n)
# n.sort(reverse=True)
# print(n)
# n.clear()
# n=lst
# print(lst)
# print(n)
# n.pop()
# print(n)
# print(lst)
# n=lst.copy()
# print(n)
# n.pop()
# print(n)
# print(lst)
# def reverse(str):
#     return x[::-1]
# x="i am the best in the world"
# print(reverse(x))
# lst.reverse()
# print(lst)
xx=list((100,25,25,45,45,45,45,21,20))
# print(type(xx))
# print(xx)
# cnt=xx.count(45)
# print(cnt)
# print(xx.index(45))





l=['apple',"mango","guava","orange","banana"]
lst=[]
def rev(s):
    return [i for i in reversed(s)]
# print(rev(l))


def count(x):
    even=0
    odd=0
    for i in x:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("the number of even number is : ",even)
    print("the number of odd number is : ",odd)



st=[25,45,85,6,21,45,78,65,25,45,45,12,36,54,57]
count(st)




# take input from user
lit=[]
n=int(input("enter the length of the list:"))
print("enter the numbers:")
for i in range(n):
    data=int(input(""))
    lit.append(data)
print(lit)