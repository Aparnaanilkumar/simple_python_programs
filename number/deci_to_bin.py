decimal=int(input("number:"))
temp=decimal
bin=''
while temp>0:
    rem=temp%2
    bin=str(rem)+bin
    temp=temp//2
print(bin)

