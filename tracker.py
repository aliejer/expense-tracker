# Expense Tracker Installment 2: Talking to the User
# Author: Aliejer C. Tortillas
# Description: A simple console-based expense tracker.

print("=" * 40)
print("\tEXPENSE TRACKER".center(30))
print("\tMake Every Peso Count".center(20))
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

total = amount1 + amount2
average = total / 2

print("\n")
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t{amount1}")
print(f"\t- {item2}:\t{amount2}")

print(f"{'Total Spent'}:\t\t{total}")
print(f"{'Average'}:\t\t{average}")

<<<<<<< HEAD

=======
print("-" * 40)
print("Made by: Aliejer C. Tortillas | Installment 2")
>>>>>>> 1407969 (Installment 2: tracker takes input)
