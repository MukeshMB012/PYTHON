#Raising custom error in Python
a= int(input("Enter any value between 5 and 9: "))

#raising custom error
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

