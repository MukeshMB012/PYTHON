#lists method in python
#adding elements to list
# l=[11,45,1,2,3,6]
# print(l)
# l.append(7)
# print(l)

#list.sort
# l=[11,45,1,2,3,6]
# print(l)
# l.sort()  #in ascending order 
# print(l)
# l.sort(reverse=True)  #in descending order
# print(l)

#reverse()
# l=[11,45,1,2,3,6]
# l.reverse()
# print(l)

#index(),,count()
# l=[11,45,1,2,3,1,3,6,1]
# print(l.index(1))
# print(l.index(45))
# print(l.index(3))
# print(l.index(11))
# print(l.count(1))
# print(l.count(3))
# print(l.count(23))

#copy()
# l=[11,45,1,2,3,1,3,6,1]
# print(l)
# m=l
# m[0]=0
# print(l)  #if we change elements in m, changes will occurs in l too.To avoid this we use copy()

# l=[11,45,1,2,3,1,3,6,1]
# print(l)
# m=l.copy()
# m[0]=0
# print(l) 
# print(m)

#insert()
# l=[11,45,1,2,3,1,3,6,1]
# print(l)
# l.insert(1,899)  #(index, elements)
# print(l)
# l.insert(4,5555)
# print(l)

#extend():
l=[11,45,1,2,3,1,3,6,1]
m=[454,675,785]
l.extend(m)
print(l)  #in this the l list also get changes

l=[11,45,1,2,3,1,3,6,1]
m=[454,675,785]
k=l+m
print(k)
print(l)
print(m)  # here the list l and m dont gets changes
