#if else condition
#condition operators
# <, >, <=, >=, ==, !=
# a=int(input("Enter your age: "))
# print("your age is: ", a)
# if(a>=18):
#     print("you can drive")  #indentation space?
# else:
#     print("you cannot drive")  

#use of elif
# num= int(input("Enter the value of num: "))
# if(num<0):
#     print("Number is negative.")
# elif(num==0):
#     print("Number is Zero.")
# elif(num==999):
#     print("Number is Special")    
# else:
#     print("Number is positive.")        

#nested if statements
num= int(input("Enter the value of num: "))
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")        

else:
    print("Number is Zero.")        