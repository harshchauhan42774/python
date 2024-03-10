
#create a divtionary
d={1:'harsh',2:'chauhan',3:18,4:45}
d1={'a':'cusp','b':'harsh','c':13,'d':45.5}
#print dictionary items
print(d)
print(d1)
#add/remove key- values pair in /from a dictionary
d[5]=100
print(d)
p=d.pop(3)
print(p)
x=d.popitem()
print(x)3
#check wheter a key exists in dictonary
k='a'
if(k in d1.keys()):
    print("exists")
else:
    print("not exist")
#iterate through a dictionary
for i in d:
    print(i,d[i])
#concatenate multiple dictionary
d.update(d1)
print(d)
