num=8778
temp=num
rev=0
rem=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print(rev)
if num==rev:
    print("pal") 
else:
    print("not")       