char=input("enter:")
v=0
c=0
for i in char:
    if i in('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    else:
        c=c+1
print("num of vowel is:",v,"num of consonants is :",c)            

