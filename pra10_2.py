def check_vc(s):
    v=0
    c=0
    s=s.lower()     
    for i in s:
        if(i in ['a','e','o','i','u']):
            v=v+1
        else:
            c=c+1
    return(v,c)

str=input('enter any string:')
t=check_vc(str)
print('no of vowels:',t[0])
print('no of consonats',t[1])


               
