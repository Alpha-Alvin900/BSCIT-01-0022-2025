from datetime import datetime

# i) Take inputs from the user
bookID = input("Enter Book ID: ")
dueDate_str = input("Enter Due Date (dd-mm-yyyy): ")
returnDate_str = input("Enter Return Date (dd-mm-yyyy): ")

# Convert string dates to datetime objects
dueDate = datetime.strptime(dueDate_str, "%d-%m-%Y")
returnDate = datetime.strptime(returnDate_str, "%d-%m-%Y")

# ii) Calculate days overdue
daysOverdue = (returnDate - dueDate).days

# If book is returned on time or earlier
if daysOverdue <= 0:
    fineRate = 0
    fineAmount = 0
else:
    # iii) Determine fine rate
    if daysOverdue <= 7:
        fineRate = 20
    elif daysOverdue <= 14:
        fineRate = 50
    else:
        fineRate = 100

    # Calculate fine amount
    fineAmount = fineRate * daysOverdue

# iv) Display the output
print("\n----- Library Fine Details -----")
print(f"Book ID      : {bookID}")
print(f"Due Date     : {dueDate_str}")
print(f"Return Date  : {returnDate_str}")
print(f"Days Overdue : {daysOverdue if daysOverdue > 0 else 0}")
print(f"Fine Rate    : Ksh. {fineRate}")
print(f"Fine Amount  : Ksh. {fineAmount}")32