# print(10>9)
# print(10==9)
# print(bool("hello"))
# print(bool(1500))
# x="world"
# y=150000
# print(bool(x))
# print(bool(y))
# print(bool(0))
# print(bool(None))
# print(bool(""))
# class myclass():
#     def __len__(self):
#         return 0
#
# ob=myclass()
# print(bool(ob))
#
#
# def myfunction():
#     return True
#
# if myfunction():
#     print("YES")
# else:
#     print("NO")


# x="200"
# print(isinstance(x,str))
# a=bool(1)
# i=1
# while a:
#     print(i)
#     i+=1
#     if i==500:
#         break

def rev_sen(sentence):
    words=sentence.split(' ')
    rev_sen=' '.join(reversed(words))
    # print(rev_sen)
    return rev_sen


        # convert decimal to binary
'''
num=int(input("enter a decimal number to convert into binary :"))
x=str('')
while num>0:
    r=num%2
    num=int(num/2)
    y=str(r)
    x=x+y
bn=x.split(' ')
bnn=' '.join(reversed(bn))
print(bnn)

'''
a=16
# print(bin(a))
def decimalToBinary(num):
    if num>1:
        decimalToBinary(num//2)
    print(num%2,end='')


n=int(input('enter a number:'))
decimalToBinary(n)
