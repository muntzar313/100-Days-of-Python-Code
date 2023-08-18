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
        







