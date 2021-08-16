
      # order of(N)

def ex1( n ):
   total = 0
   for i in range( n ) :
      total += i
      print(i)
   return total


def ex2(n):
   count = 0
   for i in range(n):
      count += 1
   for j in range(n):
      count += 1
   return count

def ex4(n):
   count = 0
   for i in range(n):
        for j in range(25):
           count += 1
   return count


# print(ex4(20))

     # order of(N2)
def ex3(n):
   count = 0
   for i in range(n):
      for j in range(n):
         count += 1
   return count
# print(ex3(20))

def ex5(n):
   count = 0
   for i in range(n):
      for j in range(i + 1):
         count += 1
   return count

# print(ex5(20))



# order of log base2 N
def ex6(n):
  count = 0
  i = n
  while i >= 1:
      count+=1
      i=i//2
  return count

# print(ex6(20))


# order of n log2 n time

def ex7(n):
   count = 0
   for i in range(n):
      count += ex6(n)
   return count
print(ex7(20))