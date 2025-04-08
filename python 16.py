#match case statements
x=int(input("Enter the value of x: "))
#x is the variables to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    #case with if-condition
    case _ if x!=90:
        print(x,"is not 90")    
    case _ if x!=80:
        print(x,"is not 80")
    case _:     #default value
        print(x)    