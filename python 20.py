#function
def calculationGmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equall")

a=9
b=8
calculationGmean(a,b)
isGreater(a,b)

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
calculationGmean(a,b)
isGreater(a,b)
