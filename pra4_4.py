e=int(input("Enter english marks:"))
m=int(input("Enter maths marks:"))
s=int(input("Enter science marks:"))
t=(e+m+s)/3
print(t)
if (t>=90):
	print("GRADE A")
elif(t>=80 and t<=89):
	print("GRADE B")
elif(t>=70 and t<=79):
	print("GRADE C")
elif(t>=60 and t<=69):
	print("GRADE D")
elif(t>=50 and t<=59):
	print("GRADE E")
elif(t<=50):
	print("FAIL")
else:
	print("Enter marks in 1 to 100")
	