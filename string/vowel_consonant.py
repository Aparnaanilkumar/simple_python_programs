char=input("enter:")
x='aeiouAEIOU'
flag=0
for i in x:
    if i==char:
        
        flag=1
        break
if flag==1:
    print("vowel")
else:
    print("consonant")    