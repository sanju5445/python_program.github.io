s={'A','P','P','L','E'}
# print(type(s))
# for i in s:
#print(i)

set1={"sanju",45,True,54.54,"male"}
set1.add(5)
set1.update(s)
print(set1)
# print(set1)
for i in set1:
    print(i)
print(s)
print(set1)
print(set1)
   # UNION MWTHOD
s1={"A","B","D","E"}
s2=s.union(s1)
# print(s)

  # INTERSECTION METHOD
l={1,2,3,4,5,6}
l1={2,4,5,9,0,3}
l2=l.intersection(l1)
# print(l2)
l3=l.symmetric_difference(l1)
# print(l3)
l4=l1.difference(l)
# print(l4)
