import json
transactions = [] 
total_income = 0
total_expense = 0
file_name = "expenses.json"

def add_transaction():
    global total_income, total_expense
    
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    t_type = input("Type (income/expense): ").lower()
    
    transaction = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
        "type": t_type
    }
    
    transactions.append(transaction)
    
    if t_type == "income":
        total_income += amount
    elif t_type == "expense":
        total_expense += amount
    else:
        print("Invalid type! please select any one of the following....!")
    
    print("\nTransaction added successfully!")


def view_transactions():
    if not transactions:
        print("\nNo transactions recorded yet.")
    else:
        for i, t in enumerate(transactions, start=1):
            print(f"{i}. {t['date']} | {t['category']} | {t['description']} | {t['amount']} | {t['type']}")
        print()


def view_summary():
    balance = total_income - total_expense
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {balance}")


def save_data():
    data = {
        "transactions": transactions,
        "total_income": total_income,
        "total_expense": total_expense
    }
    with open(file_name, "w") as file:
        json.dump(data, file)
    print("\nData saved successfully!")


def load_data():
    global transactions, total_income, total_expense
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            transactions = data["transactions"]
            total_income = data["total_income"]
            total_expense = data["total_expense"]
        print("\nData loaded successfully!")
    except FileNotFoundError:
        print("\nNo saved data found.")



load_data() 

while True:
    print("==== Expense Tracker ====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Summary")
    print("4. Save Data")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        save_data()
    elif choice == "5":
        save_data()
        print("thank you for using my expense tracker!")
        break
    else:
        print("\nInvalid choice! Please try again.")
