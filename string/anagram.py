str1=input("enter string1:")
str2=input("enter string2:")
if len(str1)!=len(str2):
    print("not anagram")
a=sorted(str1)
b=sorted(str2)
if a==b:
    print("anagram")
else:
    print("not anagram")        
