str1=input("enter string:")
char=input("enter char:")
char2=input("tobe placed:")
for i in str1:
    if i==char:
        a=str1.replace(char,char2)
print(a)       

# without replace()


# string = input("Enter a String : ")
# result = ''  #empty string
# ch = input("Enter a Character : ")
# for i in string:  
#         if i == ' ':  #if any space found in the string
#             i = ch   #replacing space with character
#         result += i   #concatenating each character of the string without space
# print(“String after removing space with t = ”,result)