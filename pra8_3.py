def fib(n):
    if(n<=1):
        return(n)
    else:
        c=fib(n-1)+fib(n-2)
        return(c)
n=int(input("Enter a number f fibnacci sequence:"))
for i in range(1,n+1):
    x=fib(i)
    print(x)