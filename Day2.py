#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill ? $") )
tip_percent=int(input("What percentage tip would you like to give ? 10,12, or 15?"))
total_split=int(input("How many people to split the bill?"))


pay= tip_percent/100 *total_bill + total_bill
final_pay= round(pay/total_split,2)
print(f"Each person should pay : $ {final_pay}")

link: https://replit.com/@muntzar313/tip-calculator-start
