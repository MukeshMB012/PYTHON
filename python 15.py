#Exercise..(proper solution in 26)
import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)

if(hour>=5 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<16):
    print("Good Afternoon")
elif(hour>=16 and hour<21):
    print("Good Evening")
else:
    print("Good Night") 



#greeting according to the time(easy way)
# timestamp= int(input("Enter the time: "))
# if(timestamp>=5 and timestamp<12):
#     print("Good Morning")
# elif(timestamp>=12 and timestamp<16):
#     print("Good Afternoon")
# elif(timestamp>=16 and timestamp<21):
#     print("Good Evening")
# else:
#     print("Good Night")      

  
#TRIED
# import time
# timestamp= int(time.strftime('%H:%M:%S'))
# print(timestamp)

# if(timestamp>=int(5:00:00) and timestamp<int(12:00:00)):
#     print("Good Morning")
# elif(timestamp>=int(12:00:00) and timestamp<int(16:00:00)):
#     print("Good Afternoon")
# elif(timestamp>=int(16:00:00) and timestamp<int(21:00:00)):
#     print("Good Evening")
# else:
#     print("Good Night") 