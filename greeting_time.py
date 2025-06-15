import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(t, "this is the current time")
ask = input("do you want to enter the time manually (y/n):")
if ask == "y" or ask == "Y":
    hour = int(input("enter the hour:"))
    if hour <0 or hour > 23:
        print("invalid hour")
        exit()
if hour >=0 and hour <12:
    print("Good Morning Sir")
elif hour >=12 and hour <19:
    print("Good Afternoon Sir")
elif hour >=119 and hour <23:
    print("Good Night Sir")