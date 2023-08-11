str1=input("enter string:")
char=input("enter char:")
for i in str1:
    if i==char:
        str1=str1.replace(char,'')
print(str1)        