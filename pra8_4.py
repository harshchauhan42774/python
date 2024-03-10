def prime(n):
    f=0
    for i in range(2,n):
        if(n%i==0):
            f=1
            break
    if(f==0):
        print("most prime")
    else:
        print("prime")
print(start)
n=int(input("Enter the value of N:"))
x=prime(n)

print(x)