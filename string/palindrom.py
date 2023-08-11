str=input("enter string:")
rev=''
for i in str:
    rev=i+rev
if str==rev:
    print("palindrom")
else:
    print("not")     