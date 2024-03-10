f1=open("practical 11.txt",'r')
f2=open("practical 12.txt",'r')

n1=len(f1.read())
n2=len(f2.read())
n=n1+n2
f1.seek(0)
f2.seek(0)

for i in range(n):
    s1=f1.read(1)
    s2=f2.read(1)
    print(s1,end="")
    print(s2,end="")