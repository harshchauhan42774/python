name=input("Enter File name:")
f=open(name,'r')
s=f.read()
print(s)
for i in s:
    c=s.count(i)
    print(i,"==",c)