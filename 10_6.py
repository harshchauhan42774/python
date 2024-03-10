def RGB(S):
    r=int(s[0:2],16)
    g=int(s[2:4],16)
    b=int(s[4:6],16)

    print("RED:",r)
    print("GREEN:",g)
    print("BLUE:",b)


s="FF07A3"
RGB(s)


#output:

#RED: 255
#GREEN: 7
#BLUE: 163
