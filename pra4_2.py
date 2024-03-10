h=int(input("Enter no of hours worked:"))
w=int(input("Enter hours wages:"))
if(h<=40):
	total= h*w
elif(h>40):
	total= 40 * w + (h-40) * w * 1.5
print("total weekly wages :",total)
	