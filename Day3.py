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


# Pizza Order Practice 
# Problem Statement
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1


# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == 'S':
    bill+=15
    
elif size=='M':
    bill+=20
    
elif size=='L':
    bill+=25
    

if add_pepperoni=='Y':
    if size=='S':
        bill= bill +2
    else:
        bill= bill + 3


if extra_cheese=='Y':
    bill+=1
    
print(f"Your final bill is: ${bill}")

Task 5 

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


merge_string=name1+name2
lower_string=merge_string.lower()

t=lower_string.count("t")
r=lower_string.count("r")
u=lower_string.count("u")
e=lower_string.count("e")

true=t+r+u+e

l=lower_string.count("l")
o=lower_string.count("o")
v=lower_string.count("v")
e=lower_string.count("e")

love=l+o+v+e
love_score=int(str(true) + str(love))




if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")





Task: Treasure Island.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇



cross=input("you are at coss road.Where do you want to go ? left or right? \n ").lower()
if cross == "right":
  print("you fell into hell.Game Over")
else:
  cross=="left"
  next_pass=input('You\'ve come to lake. This is an island. Type "wait" to wait for boat or type "swim" to swim. \n').lower()
  if next_pass=="swim":
    print("You are attacked by trout. Game over")
  else:
    next=input("From which door you want to go ? 'red', 'blue','yellow' ? \n").lower()
    if next=="red":
      print("Burned by fire. Game Over. ")
    elif next=="blue":
      print("Eaten by beasts.Game Over.")
    elif next=="yellow":
      print("You Win.")
    else:
      print("Game Over")
    
  
  
  







