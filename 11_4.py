f1=open("practical 11.txt",'r')
f2=open("practical 12.txt",'w')
s=f1.read()
l=s.split()
for i in l:
    if(len(i) == 4):
        s=s.replace(i,"****")
f2.write(s)
f1.close()
f2.close()