#function arguments in python
# default function
# def average(a=8,b=4):
#     print("The average is ",(a+b)/2)

# average()  #default value came to action..
# average(4)
# average(4,6)

# def name(fname, mname="John", lname= "Whatson"):
#     print("Hello", fname, mname, lname)

# name("Amy")
# name("Amy","Agarwal")
# name("Amy","Agarwal","Jain")

#keyword arguments-- the order in which arguments are passed doesn't metter
# def average(a,b):
#     print("The average is ",(a+b)/2)

# average(b=7,a=5)  
# average(b=8,a=2)

#required arguments
# def average(a,b,c=1):
#     print("The average is ",(a+b+c)/2)

# average(5,8)
# average(2,9)

#keywords arbitrary arguments:
# def average(*numbers):
#      print(type(numbers))
#      sum= 0
#      for i in numbers:
#         sum= sum+i
#      print("Average is ", sum/len(numbers))

# average(3,6,7)
# average(3,6,7,5,8,2,4,9)
# average(3,6,7,5,4)

# def name(**name):
#     print(type(name))
#     print("Hello",name["fname"], name["mname"],name["lname"])

# name(fname= "mukesh", lname="rakesh", mname="chandan")

#return statements
def average(*numbers):
     print(type(numbers))
     sum= 0
     for i in numbers:
        sum= sum+i
    #  return 7   
     return sum/len(numbers)

c=average(3,6,7)
d=average(3,6,7,5,8,2,4,9)
print(c)
print(d)