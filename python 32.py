#set method in python...
#union and it's updates()
# s1= {1,2,5,6}
# s2= {3,6,7}
# print(s1.union(s2))   #same as in mathematics..
# print(s1,s2)
# s1.update(s2)  #here the set 1 get updated..
# print(s1,s2)
# s2.update(s1)  #here the set 2 get updated..
# print(s1,s2)

#intersection and it's updates()
# s1= {1,2,5,6}
# s2= {3,6,7}
# print(s1.intersection(s2))
# print(s1,s2)
# s1.intersection_update(s2)
# print(s1,s2)
# s2.intersection_update(s1)
# print(s1,s2)

#symmetric difference and it's update()
#symmetric difference= (A union B) - (A intersection B)
# s1= {1,2,5,6}
# s2= {3,6,7}
# print(s1.symmetric_difference(s2))
# print(s1,s2)
# s1.symmetric_difference_update(s2)
# print(s1,s2)
# s2.symmetric_difference_update(s1)
# print(s1,s2)

#isdisjoint()
# s1= {1,2,5,6}
# s2= {3,6,7}
# print(s1.isdisjoint(s2))
# s3= {1,2,5}
# s4= {3,6,7}
# print(s3.isdisjoint(s4))

#issuperset()      {subset and superset are just opposite term}
# cities1= {"Tokyo", "Madrid", "Delhi", "Berlin"}
# cities2= {"Tokyo", "Madrid", "Delhi"}
# print(cities1.issuperset(cities2))
# cities3= {"Delhi", "Tokyo", "Mumbai"}
# print(cities1.issuperset(cities3))

#issubset()
# cities1= {"Tokyo", "Madrid", "Delhi", "Berlin"}
# cities2= {"Tokyo", "Madrid", "Delhi"}
# print(cities2.issubset(cities1))
# cities3= {"Delhi", "Tokyo", "Mumbai"}
# print(cities3.issubset(cities1))

#add()  (when you want to add a single item)
# cities1= {"Tokyo", "Madrid", "Delhi", "Berlin"}
# cities1.add("Bengluru")
# print(cities1)

#updates     (when you want to add more than a single item)
# cities1= {"Tokyo",  "Delhi", "Berlin"}
# cities2= {"Tokyo", "Madrid"}
# cities1.update(cities2)
# print(cities1)

#remove()/discard()
#If we try to delete an item which is not  present in set,
# then remove() raises an error, whereas discard() does not raise any error..
# cities= {"Tokyo", "Madrid", "Delhi", "Berlin"}
# cities.remove("Tokyo")
# print(cities)
# cities.discard("Berlin")
# print(cities)

#pop()   (any random value can be pop out)
# cities= {"Tokyo", "Madrid", "Delhi", "Berlin"}
# item= cities.pop()
# print(cities)
# print(item)

#del
# cities= {"Tokyo", "Madrid", "Delhi", "Berlin"}
# del cities
# print(cities)  #all the element inside the set get deleted even the variable name

#clear()
# cities= {"Tokyo", "Madrid", "Delhi", "Berlin"}
# cities.clear()
# print(cities)   #it just only clears the elements inside the cities

#check if item exist
info= {"carla",19,False, 5.9}
if "carla" in info:
    print("carla is present")
else:
    print("carla is not present")    