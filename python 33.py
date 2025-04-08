#Dictionaries in python
dic={
    344: "Harry",
    56:"Subham",
    678:"Zakir",
    567:"Neha"
}
print(dic[567])      #it do throw error if the key is missing in the dictionaries.
print(dic.get(567))  #it doesn't throw error if the key is missing in the dictionaries.
print(dic)
print(dic.keys())
print(dic.values())

#for printing key and values using for loop
for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")