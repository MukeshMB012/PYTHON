#f-string in python
letter= "Hey my name is {} and I am from {}"
name= "Mukesh"
country= "India" 
print(letter.format(name, country))
#other way to print it 
# letter= "Hey my name is {1} and I am from {0}"
# print(letter.format(country, name))  

#use of f-string
print(f"Hey my name is {name} and I am from {country} ")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price= 49.09999
print(f"For only {price: .2f} dollars")

print(f"{2*30}")
print(type(f"{2*30}"))
