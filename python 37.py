#Finally keyword in Python
# try:
#     l=[1,3,5,7]
#     i= int(input("Enter the index: "))
#     print(l[i])

# except:
#     print("Some error occured:")

# finally:
#     print("I am always executed")  #it is always executed even in the function


#inside function
#case 1
def func1():
    try:
      l=[1,3,5,7]
      i= int(input("Enter the index: "))
      print(l[i])
      return 1 #even after executing the above line it will not return, it will return after executing the finally line

    except:
      print("Some error occured:")
      return 0

    finally:
      print("I am always executed")

#case 2  
# def func1():
#     try:
#       l=[1,3,5,7]
#       i= int(input("Enter the index: "))
#       print(l[i])
#       return 1

#     except:
#         print("Some error occured:")
#         return 0

#     print("I am always executed")  

i=func1()
print(i)