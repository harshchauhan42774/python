def anagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("Both Worls are anarams")
    else:
        print("Both Words are not anagrams")
str1=input("Enter one word:")
str2=input("Enter another word:")
anagram(str1,str2)