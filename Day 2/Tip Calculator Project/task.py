print("Welcome to the tip calculator!")
t_bill = float(input("What was the total bill?"))

a = round(10/100, 2)
b = round(12/100, 2)
c = round(15/100, 2)

tip_percent_option = input("How much tip would you like to give? a = 10%, b = 12%, c = 15% ")

if tip_percent_option == "a":
    tip_percent = a
elif tip_percent_option == "b":
    tip_percent = b
else:
    tip_percent = c

tipBill_amount = (t_bill * tip_percent) + t_bill

amountOf_people = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round((tipBill_amount/amountOf_people),2)}")


