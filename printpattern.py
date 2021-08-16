     # SIMPLE YRAMID PATTERN

def prinstar(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")

# prinstar(5)

def pr(n):
    lst=[ ]
    for i in range(1,n+1):
        lst.append("* "*i)
    print("\n".join(lst))

# pr(10)



    # SIMPLE PYRAMID PATTERN AFTER 180 DEGREE
def pr2(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k)