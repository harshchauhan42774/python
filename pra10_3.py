import datetime
a=input("Enter date in dd/mm/yyyy: ")
l=a.split("/")
print(l)
dd=int(l[0])
mm=int(l[1])
yyyy=int(l[2])
d=datetime.date(yyyy,mm,dd)
ans=d.strftime("%m/%d/%y")
print(ans)