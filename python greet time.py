#write a program to greet eith in the evening, afternoon and morning..

import datetime
currentTime = datetime.datetime.now()
currentTime.hour

name=input("please enter your name:  ")

if currentTime.hour < 12:
    print("Hello Good mornig " + name)
elif currentTime.hour  < 12:
    print("Hello Good afternoon" + name)
else: 
    print("Hello Good evening " + name)


