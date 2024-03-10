name=input("Enter File name:")
f=open(name,'r')
s=f.read()
l=s.split()
for i in l:
    if(i.isdigit()):
        print(i)
