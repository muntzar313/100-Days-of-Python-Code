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
    # print("Your final bill is: $15")
elif size=='M':
    bill+=20
    # print("Your final bill is: $20")
elif size=='L':
    bill+=25
    # print("Your final bill is: $25")

if add_pepperoni=='Y':
    if size=='S':
        bill= bill +2
    else:
        bill= bill + 3
# print(f"your final bill is: {bill}")

if extra_cheese=='Y':
    bill+=1

print(f"Your final bill is: ${bill}")

# else:
#     print(f"Your final bill is : ${bill}")
