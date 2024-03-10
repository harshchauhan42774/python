t=(10,18.7,'CHAUHAN',"HARSH")
#print tuple print
for i in t:
    print(i)
#convert tuple into list
l=list(t)
print(l)
#remove data items from a list
l.remove(18.7)
print(l)
#convert list in tuple
t1=tuple(l)
print(t1)
