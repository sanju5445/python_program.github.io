def matrixx():
    nr=int(input("enter the number of rows:"))
    nc=int(input("enter the number of column:"))
    # DEFINE THE MATRIX
    matrix=[]
    print("enter the value row wise:")
    for i in range(nr):
        a=[]
        for j in range(nc):
            a.append(int(input()))
        matrix.append(a)
    for i in range(nr):
        for i in range(nc):
            print(matrix[i][j], end=" ")
        print("\r")

# matrixx()
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(type(lst))
# print(lst)


  # find the value 16

def find_element(arr,key):
    for i in range(len(lst)):
        if lst[i] == 16:
            print(i)
            # break
# find_element(lst,16)
def binary_srh(arr,low,high,key):
    mid=int((low+high)//2)
    if key==arr[mid]:
        return mid
    if key>arr[mid]:
        return binary_srh(arr,mid+1,high,key)
    if key<arr[mid]:
        return binary_srh(arr,low,mid-1,key)
    return 0
# print(len(lst))
a=binary_srh(lst,0,20,12)
print(a)
def insert_element(arr,pos,key):
    for i in range(len(arr)):
        if i==pos:
            # arr[i]=key
            arr.insert(i,key)
            break
    print(arr)
def delete_element(arr,pos):
    for i in range(len(arr)):
        if i ==pos:
            del arr[i]
            break
    print(arr)
def poww(base,n):
    if n==0:
        return 1
    elif n==1:
        return base
    else:
        # return base**n
        return (base*poww(base,n-1))

# print(lst)