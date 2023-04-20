print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

if tip_percent == 10:
    total_bill = bill * 1.1
elif tip_percent == 12:
    total_bill = bill * 1.12
elif tip_percent == 15:
    total_bill = bill * 1.15

bill_per_person = round(total_bill / number_of_people, 2)

print("Each person shold pay: " + str(bill_per_person))