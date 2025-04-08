#Recursion in python
#factrial(7)= 7*6*5*4*3*2*1
#factrial(6)= 6*5*4*3*2*1
#factrial(5)= 5*4*3*2*1
#factrial(0)= 1

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(5))    
# print(factorial(4))    
# print(factorial(3))    

#for 5 steps are--
# 5 * factorail(4)
# 5 * 4 * factorail(3)
# 5 * 4 * 3 * factorail(2)
# 5 * 4 * 3 * 2 * factorail(1)
# 5 * 4 * 3 * 2 * 1

#Quick quiz-- Write a program to print the Fibonacci sequence
def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(3))    
print(fibo(4))    
print(fibo(5))    
print(fibo(6))    
print(fibo(19))    