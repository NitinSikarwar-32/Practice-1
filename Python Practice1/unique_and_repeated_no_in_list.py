l1=[1,2,2,3,4,4,4,5,6,6,7,7,7]
l2=[i for i in l1 if l1.count(i)>1]
print(l2)
unique=set(l2)
print(unique)
