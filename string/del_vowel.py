str1=input("enter string:")
a=''

for i in str1:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        i=""
    a=a+i
print("result is:",a)         


