def gcd(a,b):
    if(b==0):
        return a
    else:
        c=gcd(b,a%b)
        return c
x=gcd(20,12)
print(x)
