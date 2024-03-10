def RGB(s):
    r=int(s[0:2],16)
    g=int(s[2:4],16)
    b=int(s[4:],16)

    print("red:",r)
    print("green:",g)
    print("blue:",b)

s="FF07A3"
RGB(s) 