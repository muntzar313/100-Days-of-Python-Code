import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_img = [rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper , 2 for Scissors."))
print(game_img[user_choice])
computer_choice=random.randint(0,2)
print("Computer Choose.")
print(game_img[computer_choice])


# For 0
if user_choice==0 and computer_choice==1:
  print("you Loose.")
elif user_choice==0 and computer_choice==2:
  print("You Win.")
elif user_choice==0 and computer_choice==0:
  print("Its a Draw.Try Again.")

# for 1
if user_choice==1 and computer_choice==0:
  print("You Win.")
elif user_choice==1 and computer_choice==1:
  print("Its a Draw.Try Again.")
elif user_choice==1 and computer_choice==2:
  print("You Loose.")

# for 2
if user_choice==2 and computer_choice==0:
  print("You Loose.")
elif user_choice==2 and computer_choice==1:
  print("You Win.")
elif user_choice==2 and computer_choice==2:
  print("Its a Draw.Try Again.")

# if user_choice != (0,1,2):
#   print("It's an Invalid Number.Try Again.")
  

# if choice=='0':
#   print(rock)
# elif choice=='1':
#   print(paper)
# elif choice=="2":
#   print(scissors)
# # else:

# # print("Computer Choose.")
# computer_choice=random.randint(0,2)
# print(f"comuter choose.{computer_choice}")
# if computer_choice=="0":
#   print(rock)
# elif computer_choice=="1":
#   print(paper)
# elif computer_choice=="2":
#   print(scissors)
# print(random.choice(computer_choice))
