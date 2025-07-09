import csv
#main function
def main():
    role = input("What would you like to do: \n 1. Add expense \n 2. View expense\n")
    if role == "1":
        add()
    elif role == "2":
        view()
    else:
        print("Please enter a valid input")        


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