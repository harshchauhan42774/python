s1={10,18.7,'CUSP','FALSE'}
s2={10,56.4,'CHAUHAN','HARSH'}
#print set items 
for i in s1:
    print(i)
#add items in from a set.
s1.add(50)
print(s1)
#remove items in from a set
s1.remove(50)
print(s1)
#perfrom union operation on set
u=s1.union(s2)
print(u)
#perfrom intersection operation on set
i=s1.intersection(s2)
print(i)
#perfrom difference operation on set
d=s1.difference(s2)
print(d)
#perfrom symmetric_difference operation on set
sd=s1.symmetric_difference(s2)
print(sd)
