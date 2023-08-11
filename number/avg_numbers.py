num=int(input("number of entries:"))

arr=[]
for i in range(0,num):
    digit=int(input("enter numbers:"))
    arr.append(digit)
sum=sum(arr)
avg=sum/num
print("avg is:",avg)        
