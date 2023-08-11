num=int(input("number:"))
n=num
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if num==sum:
    print("perfect")
else:
    print("not")            

