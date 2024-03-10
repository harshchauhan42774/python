#crate and open file named practical 11.txt
f=open("practical 11.txt",'r')

#write a simple string to a file
#f.write("Hello World..")

#read the entire content of the file and display
#s=f.read()
#print(s)

#read the entire content of the file line by line and display
s=f.readlines()
print(s)
#read the entire content of the file and display
#f.writelines(["hii\n","hello..\n","welcome\n"])
f.readlines()
print("No of lines in files:",len(s))
c=0
for i in s:
    l=i.split()
    c=c+len(l)
print("No of worlds in files:",c)
f.close()