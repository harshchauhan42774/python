y=int(input("Enter years:"))
if (y%4==0 and y%100!=0)or(y%400==0):
	print("this is leap years")
else:
	print("this is not a leap years")