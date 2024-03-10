s=0
n=10000
-for i in range(1,n):
	if(n%i==0):
		s=s+i
if(n==s):
	print("number is perfect")
else:
	print("number is not perfect")