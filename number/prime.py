num=2
flag=0
for i in range(2,num):
    if (num%i ==0):
        flag=1
        break
if flag==1:
    print("prime")
else:
    print("not prime")    

