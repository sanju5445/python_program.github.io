tl=(1,2,3,4,5,6)
# print(type(tl))
# print(len(tl))
# t=("apple",)
# print(type(t))
# for i in tl:
    # print(i)
t=(1,2,3,4,5,6,7)
# print(t[-4:-1])
# if 4 in t:
#     print("yes the item is present in the tuple")

x=("A","B","C","D","E")
# y=list(x)
# print(type(y))
# y.append("F")
# x=tuple(y)
print(x)
y=("F",)
x+=y
# print(x)
# print(x*4)


fruits=("guava","mango","orange","cherry","banana")
(a,*b,c)=fruits
# print(a)
# print(b)
# print(c)


# for i in fruits:
#     print(i)
# temp=[]
# for i in range(len(fruits)):
#     temp.append(fruits[i])
#     print(fruits[i])
# print(temp)


num=tuple((2,5,7,2,9,4,6))
# num.sort()
# n=list(num)
# n.sort()
# num=tuple(n)
print(num)
print(num.count(2))
print(num.index(7))
