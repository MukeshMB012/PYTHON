#exercise 2 solution

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