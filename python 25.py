#operation in tuples
#manipulating tuples
# countries= ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)  #converting tuple to list
# temp.append("Russia")   #add item
# temp.pop(3)             #remove item
# temp[4]= "Finland"      #change item
# countries= tuple(temp)  #converting list to tuple
# print(countries)

# #adding two tuple
# countries1= ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
# countries2= ("Vietnam", "India", "China")
# southEastAsia= countries1 + countries2
# print(southEastAsia)

#count()method
# tup1=(1,5,3,6,343,8,3,1,2,1)
# print(tup1.count(3))
# print(tup1.count(1))
# print(tup1.count(343))

#index() method
tup1=(1,5,3,6,343,8,3,1,2,1)
print(tup1.index(3))
print(tup1.index(343))
print(tup1.index(8))
#index method for any specific region
print("Count of 3 in tup1 is ", tup1.index(3,4,9))
#index of 3 in between 4th(3) and 9th(8) index
print(len(tup1))   #tuple length