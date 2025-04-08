#introduction to lists
# marks=[3,6,7,"Mukesh", True]
# print(type(marks))
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

#negatives index
# marks=[3,5,4,7,8, "Mukesh"]
# print(marks[-3])  #negatives index
# print(marks[len(marks)-3])  #positives index
# print(marks[5-3])  #positives index
# print(marks[2])  #All are same

# #check whether an item is present in the list
# if 7 in marks:
#     print("Yes")
# else:
#     print("No")    
# if "7" in marks:
#     print("Yes")
# else:
#     print("No")    
# if "Mukesh"  in marks:
#     print("Yes")
# else:
#     print("No")   
# #same things applies for strings as well     
# if "kesh"  in "Mukesh":
#     print("Yes")
# else:
#     print("No")    
# if "ksh"  in "Mukesh":
#     print("Yes")
# else:
#     print("No") 


# marks=[3,5,4,7,8, "Mukesh",2,7,4]
# print(marks)
# print(marks[:])
# print(marks[1:])
# print(marks[:2])
# print(marks[1:-1])
# print(marks[1:4])
# #jump index
# print(marks)
# print(marks[1:8])
# print(marks[1:8:2])
# print(marks[1:8:3])

#list comprehenstion
list=[i*i for i in range(10)]
print(list)
list=[i*i for i in range(10) if i%2==0]
print(list)