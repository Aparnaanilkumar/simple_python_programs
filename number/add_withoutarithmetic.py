def add(a,b):
    while b!=0:
        carry=a&b
        a=a^b
        b=carry<<1
    return a
a=int(input("num1:"))
b=int(input("num2:"))
print("add result:",add(a,b))


   