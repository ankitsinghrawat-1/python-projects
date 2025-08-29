import time
import pyttsx3 as pyt

t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(t, "this is the current time")

if hour >= 0 and hour < 12:    
      greeting = "Good Morning Sir"
      engine = pyt.init()
      engine.say(greeting)
      engine.runAndWait()
      print(greeting)

elif hour >= 12 and hour < 19:
      greeting = "Good Afternoon Sir"
      engine = pyt.init()
      engine.say(greeting)
      engine.runAndWait()
      print(greeting)

elif hour >= 19 and hour < 23:
      greeting = "Good Night Sir"
      engine = pyt.init()
      engine.say(greeting)
      engine.runAndWait()
      print(greeting)


ask = input("do you want to enter the time manually (y/n):")
if ask == "y" or ask == "Y":
    hour = int(input("enter the hour:"))
    if hour <0 or hour > 23:
        print("invalid hour")
        exit()
    if hour >=0 and hour <12:
      
      greeting = "Good Morning Sir"
      engine = pyt.init()
      engine.say(greeting)
      engine.runAndWait()
      print(greeting)

    elif hour >=12 and hour <19:

      greeting = "Good Afternoon Sir"
      engine = pyt.init()
      engine.say(greeting)
      engine.runAndWait()
      print(greeting)

    elif hour >=19 and hour <23:
      greeting = "Good Night Sir"
      engine = pyt.init()
      engine.say(greeting)
      engine.runAndWait()
      print(greeting)
