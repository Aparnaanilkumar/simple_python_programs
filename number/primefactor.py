def prime_factor(num):
    arr=[]
    for i in range(1,num):
        if(num%i==0):
            arr.append(i)
    for i in arr:
        for j in range(2,i):
            if(i%j!=0):
                print(i)

num=int(input("number"))
prime_factor(num)
                    


            
