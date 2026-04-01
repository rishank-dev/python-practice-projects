# ================================ PROJECT START ========================================

import json
from tabulate import tabulate
import time
from datetime import datetime

sleep = lambda: time.sleep(2)

print("\n", " " * 20 + "MONTHLY EXPENSE TRACKER")


# load data from the file
def load_data():
    try:
        with open("expense_file.txt") as file:
            data = file.read().strip()
            if not data:
                return []
            else:
                return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return []


# save data into the file
def data_saver_helper(expense_list):
    with open("expense_file.txt", "w") as file:
        json.dump(expense_list, file)


# Ask user for choice
def user_choice():
    print(f"\n{'-' * 15} Menu {'-' * 15} \n")
    print(" (1.)  Add Expense")
    print(" (2.)  View Expenses")
    print(" (3.)  Delete Expense")
    print(" (4.)  Monthly Report")
    print(" (5.)  Category Summary")
    print(" (6.)  Exit \n")
    print("-" * 40)

    while True:
        choice = int(input("\nEnter your choice from (1 - 6) : "))
        if choice in [1, 2, 3, 4, 5, 6]:
            return choice
        else:
            print("Try entering a Valid Choice! ")


# add expense
def add_expense(expense_list):
    print("\nAdding a new EXPENSE to your expense list...... \n ")

    while True:
        try:
            amount = f"{int(input("Enter the 'amount' (in rupees) : ").strip()) : ,}"
            if amount == "0":
                print("Enter a vaild amount.")
                continue
            else:
                break
        except ValueError:
            print("Your amount should be a valid number.")

    category = (
        input(
            "Enter the category to which your expense belongs to (Food/Travel/Bill/Shopping/Other) : "
        )
        .lower()
        .strip()
    )

    if category not in ["food", "travel", "bill", "shopping", "other"]:
        print(
            "Any of the choices other than those given in the options will be considered into 'other' category. "
        )
        category = "other"

    description = (
        input("Enter a small description for later understanding : ")
        .strip()
        .capitalize()
    )

    add_date = datetime.now().strftime("%d-%m-%Y")
    add_time = datetime.now().strftime("%I:%M:%S %p")

    notes = {
        "Amount (in Rs.)": amount,
        "Category": category,
        "Description": description,
        "Date_add": add_date,
        "Time_add": add_time,
    }

    expense_list.append(notes)

    data_saver_helper(expense_list)

    print("\nEntry added successfully!!! \n")


# view expense
def view_expense(expense_list):
    print("\n YOUR EXPENSES :- \n")

    if not expense_list:
        print("No entry added yet.\n")
        return

    print("*" * 40)
    print(
        tabulate(
            expense_list,
            headers="keys",
            tablefmt="github",
            colglobalalign="center",
            maxcolwidths=30,
            showindex=range(1, len(expense_list) + 1),
        )
    )
    print("\n" + "*" * 40)


# delete expense
def del_expense(expense_list):
    if not expense_list:
        print("No entry added yet.\n")
        return

    print("\nThe entry deleted will be permanently removed from your expense list. \n")

    try:
        expense_index = int(input("\nEnter entry number to delete : "))
    except ValueError:
        print("Entry number should be a valid number")
        return

    for index, entry in enumerate(expense_list):
        if expense_index == index + 1:
            removed = expense_list.pop(index)

            data_saver_helper(expense_list)
            print(
                f"Entry amount: '{removed['Amount']}' and category : '{removed['Category']}' is deleted from your expense list."
            )
            break
    else:
        print(f"entry number {expense_index} not found.")


# generate a monthly report
def month_report(expense_list):
    print("\nThe program will generate a monthly report of all your expenses. \n")
    try:
        month = int(input("Enter the month number (1-12) : "))
        if month not in range(1, 13):
            print("Month number should be between 1-12. \n")
    except ValueError:
        print("Try entering a valid month number. \n")

    try:
        year = int(input("Enter the year number : "))
    except ValueError:
        print("Try entering a valid month number. \n")

    monthly_report_list = []

    for index, entry in enumerate(expense_list):
        entry_month = datetime.strptime(entry["Date_add"], "%d-%m-%Y").month
        entry_year = datetime.strptime(entry["Date_add"], "%d-%m-%Y").year

        if month == entry_month and year == entry_year:
            monthly_report_list.append(entry)

    view_expense(monthly_report_list)


# generate a category summary
def category_summary(expense_list):
    print(
        "\nThe program will generate a list of all your expenses in a particular category."
    )
    print(
        "All the categories other than : food, travel, bill and shopping will be considered in 'other' category. \n"
    )

    while True:
        category = (
            input("Enter a category (food/travel/bill/shopping/other) : ")
            .strip()
            .lower()
        )
        if category not in ["food", "travel", "bill", "shopping", "other"]:
            print(
                "Try entering a valid category (food, travel, bill, shopping) or in any other case, enter 'other' category."
            )
        else:
            break

    
    category_summary_list = []

    for index, entry in enumerate(expense_list):
        if category == entry["Category"]:
            category_summary_list.append(entry)

    view_expense(category_summary_list)



# main loop
def main():
    expense_list = load_data()

    while True:
        user = user_choice()

        match user:
            case 1:
                add_expense(expense_list)
                sleep()
            case 2:
                view_expense(expense_list)
                sleep()
            case 3:
                del_expense(expense_list)
                sleep()
            case 4:
                month_report(expense_list)
                sleep()
            case 5:
                category_summary(expense_list)
                sleep()
            case 6:
                print("Exiting the program .....")
                for i in range(1,6):
                    time.sleep(0.5)
                    print(".")
                
                print("\n")
                break


main()



# ====================================== PROJECT END =============================================
