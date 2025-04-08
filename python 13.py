#String method
# a= "Harry"
# print(len(a))
# print(a.upper())  #String are immutable, so these are stored in another string
# print(a.lower())

#rstrip()
# a= "Harry!!!"
# print(a.rstrip("!"))
# a1= "!!!Harry!!!"
# print(a1.rstrip("!"))

#replace()
# a= "Harry is a boy, Harry is smart"
# print(a.replace("Harry", "John"))

#split-- it split the words presented in the strings
# a= "Harry is a boy, Harry is smart"
# print(a.split(" "))

#Capitalize()
# blogHeading= "introduction to JS"
# print(blogHeading.capitalize())

#centre()
# str1= "welcome to the Console!!!"
# print(len(str1))
# print(str1.center(50))
# print(len(str1.center(50)))

#count()
# a= "Harry is a boy, Harry is smart"
# print(a.count("Harry"))  #counts the number of times Harry occured in "a" string

#endswith()
# a= "Harry is a boy, Harry is smart"
# str1= "welcome to the Console!!!"
# print(str1.endswith("!!!"))
# print(a.endswith("smart"))
# print(a.endswith("mb"))
# print(a.endswith("rt"))
# print(str1.endswith("to",4,10))

#output()
# str2= "He's name is Dan. He is an honest man."
# print(str2.find("is"))
# print(str2.find("ishh"))  #return -1 when there is no same characters..
#print(str2.index("ishh")) ---return error in case of no same characters..

#isalnum()
# str3= "WelcomeToTheConsole" 
# print(str3.isalnum())

#isalpha()
# str3= "WelcomeToTheConsole" 
# str4= "Welcome100"
# print(str3.isalpha())
# print(str4.isalpha())

#islower()
# str= "Hello world"
# str1= "hello world"
# print(str.islower())
# print(str1.islower())

#isprintable()
# str1="We wish you a Merry christmas"
# str2="We wish you a Merry christmas\n"
# print(str1.isprintable())
# print(str2.isprintable())

#isspace()
# str1="We wish you a Merry christmas"
# str2="   "
# print(str1.isspace())
# print(str2.isspace())

#istitle()
# str1= "World Health Organization"
# str2= "World Health organization"
# print(str1.istitle())
# print(str2.istitle())

#isupper()
# str1="WORLD HEALTH ORGANISATION"
# str2="WORLD health ORGANISATION"
# print(str1.isupper())
# print(str2.isupper())

#startswith()
# str1="Python is a Intepreted Language"
# print(str1.startswith("Python"))
# print(str1.startswith("python"))

#swapcase()
str1="Python is a Intepreted Language"
print(str1.swapcase())

#title
str1= "His name is Dan, Dan is an honest man"
print(str1.title())

