import csv

from dateutil import parser

def parse_month_year(user_input):
    try:
        #to ensure that the user inputs the month before the year
        date = parser.parse(user_input, dayfirst=True)
        return date.month, date.year
    except Exception as e:
        print("Invalid date format. Try again.")
        return None, None


#main function
def main():
    role = input("What would you like to do: \n 1. Add expense \n 2. View expense\n")
    if role == "1":
        add()
    elif role == "2":
        user_input = input("Enter month and year (e.g., 'September 2025' or '9/2025'): ")
        month, year = parse_month_year(user_input)
        view()
    else:
        print("Please enter a valid input")        
def expenditure_breakdown(n):
    total = 0
    

#adding function
def add():
    fieldnames = ["Amount", "Category", "Note", "Date"]
    amount = input("Amount: ")
    category = input("Category: ")
    note = input("Note: ")
    date = input("Date (DD-MM-YYYY): ")

    expense = {
        "Amount": amount,
        "Category": category,
        "Note": note,
        "Date": date
    }

    with open("expense.csv", "a+", newline='') as file:
        writer = csv.DictWriter(file, fieldnames = fieldnames)

        file.seek(0)
        if not file.read(1):
            writer.writeheader()
        
        writer.writerow(expense)    

def view():
    with open("expense.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Date']} | {row['Category']} | KES {row['Amount']} | {row['Note']}")


if __name__ == "__main__":
    main()

