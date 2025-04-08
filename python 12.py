#String slicing
names="Harry,Shubham"
print(names[0:5])
print(names[0:8])
print(names[0:11])
print(names[:5])  #it will carry from 0 characters
print(names[:])  #it will assume the first and last by default
print(names[0:-3])  # lines 8 and 9 means the same 
print(names[0:len(names)-3])  
print(names[-5:-3])  #---print(names[len(names)-5:len(names)-3])
print(names[-8:-3])


#length of strings
print(len(names))
fruit="Mango"
mangolen= len(fruit)
print(mangolen)
