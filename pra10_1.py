def palindrome(s):
    s1=s[::-1]
    if(s==s1):
        print("palindrome")
    else:
        print("not palindrome")
str=input('enter any palndrome')

palindrome(str)