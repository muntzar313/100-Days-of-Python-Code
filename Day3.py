# Code to check whether the year is a leap year or not
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0 :
    print("Leap year.")
elif year % 100 == 0 :
    print("Leap year.")
elif year % 5 == 0 :
    print("Leap year.")
else:
    print("Not leap year.")

# Flowchart 
![Image Alt Text](Leap_year.png)
