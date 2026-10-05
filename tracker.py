# Expense Tracker - Installment 3: The Tracker Does Math
# Author: Aliejer C. Tortillas
# Description: Console-based expense tracker with tax and budget.

print("=" * 40)
print("EXPENSE TRACKER".center(40))
print("Make Every Peso Count".center(40))
print("=" * 40)

print("\nWelcome! Track your expenses with ease.\n")

print("MAIN MENU")
print("[1] Add Expense".center(20) + "\t\t(coming soon)")
print("[2] View All Expenses".center(25) + "\t(coming soon)")
print("[3] Show Total Spent".center(23) + "\t\t(coming soon)")
print("[4] Exit".center(11) + "\t\t\t(coming soon)\n")

name = input("What's your name: ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? $"))

item2 = input("\nSecond expense? ")
amount2 = float(input("Amount? $"))

subtotal = 0
subtotal += amount1
subtotal += amount2

average = subtotal / 2

tax_percent = int(input("\nTax rate %: "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Your budget: $"))
over_budget = total > budget
left = budget - total

print("\n")
print("-" * 40)
print("SUMMARY")
<<<<<<< HEAD
print(f"\t- {item1}:\t{amount1}")
print(f"\t- {item2}:\t{amount2}")

print(f"{'Total Spent'}:\t\t{total}")
print(f"{'Average'}:\t\t{average}")

<<<<<<< HEAD

=======
print("-" * 40)
print("Made by: Aliejer C. Tortillas | Installment 2")
>>>>>>> 1407969 (Installment 2: tracker takes input)
=======
print(f"\t- {item1}\t${amount1}")
print(f"\t- {item2}\t\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand Total:\t\t${total}")
print(f"Over Budget?:\t\t{over_budget}")
print(f"Left in Budget:\t\t${left}")
print("-" * 40)
print(f"Made by: Aliejer C. Tortillas | Installment 3")
>>>>>>> 02cb44f (Installment 3: tracker does math)
