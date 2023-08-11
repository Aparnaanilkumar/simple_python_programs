num=1001
flag=0
while num>0:
    j=num%10
    num=num//10
    if(j!=0 and j!=1):
        flag=1
        break
if flag==1:
    print("not")
else:
    print("binary")    
