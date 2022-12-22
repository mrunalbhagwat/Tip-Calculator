print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_ppl = int(input("How many people to split the bill? "))
total_bill = ((tip / 100) + 1) * bill
total_share = total_bill / no_of_ppl
final=round(total_share,2)
print(f"Each person should pay: ${final}")
