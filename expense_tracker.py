# Expense Tracker

expenses = []

while True:
    print("\n--- Expense Entry ---")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/etc.): ")
    amount = float(input("Enter amount: "))

    # Store as a dictionary
    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    # Ask user if they want to continue
    choice = input("Add another expense? (y/n): ").lower()
    if choice != 'y':
        break

# Display all expenses
print("\n--- All Expenses ---")
total = 0
for e in expenses:
    print(f"{e['date']} | {e['category']} | Rs.{e['amount']}")
    total += e['amount']

print(f"\nTotal Expenses: Rs.{total}")
