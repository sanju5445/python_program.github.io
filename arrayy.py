import array as ay
ar=ay.array('i',[1,2,4,5,6])
# print(ar)
# ar.append(7)
# print(ar)
print(ar.buffer_info())
# print(ar[2])
# ar.reverse()
# print(ar)
# new=ay.array(ar.typecode,(i*i for i in ar))
# print(new)
# ar.append(4)
# print(ar)
# ar.pop(4)
# print(ar)
# del ar[1]
print(ar)
# x=ar
ar.reverse()
print(ar)
# print(x)
print(id(ar))

# for i in ar:
#     print(i)

arr=ay.array("i",[1,2,3,4,5,6,7,8,9])
print(arr)
arr.append(10)
print(arr)
print(type(arr))
print(arr)
del arr[1]
arr.pop()
arr.insert(1,2)
print(arr)
arr.append(10)
print(len(arr))
print(arr)
# flag=0
# x=int(input("enter the element you want to found:"))
# for i in range(len(arr)-1):
#     if arr[i]==x:
#         print(i)
#         flag=1
# if flag==0:
#     print("the elements is not present in the given array")


         # INSERTING AN ELEMENT

