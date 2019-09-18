import json
from datetime import datetime
import time
import os.path
import sys

def exit_program(): #function to exit program
        print("")
        print("Thanks! Have a great day!") 
        print("")  
        sys.exit(0)

print("")
print("~~ Welcome to your checkbook~~") #prints opening statement, does not repeat

while True: #repeats until the user exits
    print("""
These are your options via the terminal:
    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) view transactions
    5) modify past transaction 
    6) exit (type exit at any time to exit)
    """) #shows user options every time

    while True: #repeats until user enters a valid entry
        time.sleep(.5)
        user_select = input("What would you like to do today? ")
        if user_select == "exit":
            exit_program()
        elif user_select in "123456": #only valid entries
            break
        else:
            print("Invalid entry.")

    if os.path.exists("transactions.txt"): 
        with open("transactions.txt") as f:
            data = json.load(f) #open latest data list
    else: 
        f= open("transactions.txt","w+")
        f.write("[]")
        f.close() 
        with open("transactions.txt") as f:
            data = json.load(f) #if data list doesnt exist, create it and open it

    if os.path.exists("balance.txt"):
        balance = (open("balance.txt","r")) #open balance sheet
    else: 
        f= open("balance.txt","w+")
        f.write("0")
        f.close() 
        balance = (open("balance.txt","r")) #if balance doesnt exist, create and open it
 
    if user_select == "1":
        print(f"Your balance is ${balance.read()}.") #print balance from balance sheet

    elif user_select == "2":
        while True: #repeats until numeric entry
            change_balance = input("How much would you like to withdraw? ")
            if change_balance == "exit":
                exit_program()
            elif change_balance.replace(".","").isdigit():
                break
            else:
                print("This is not a numeric value.")
        
        change_balance = format(float(change_balance), ".2f") #format change_balance to manipulate
        print(f"Withdraw amount: ${change_balance}")
        change_description = input("Description (optional): ") 
        if change_description == "exit":
            exit_program()        

        after_change = format((float(balance.read()) - float(change_balance)), ".2f")
        print("")
        print(f"Your new balance is ${after_change}.") #shows updated balance

        balance = (open("balance.txt", "w"))
        balance.write(str(after_change)) #write new balance back to balance sheet

        data.append(
            {
            'id' : len(data),
            'type': 'withdraw',
            'amount': "$" + change_balance,
            'date': datetime.now().strftime("%m/%d/%y"),
            'time': datetime.now().strftime("%H:%M"),
            'description': change_description
            }) #add withdraw to data list
        
        if float(after_change) < 0: #perform if negative balance
            print("")
            print("*** Warning: Negative balance. Incurs $25 overdraft fee. ***")
            after_change = format(float(after_change) - float(25), ".2f")
            print(f"Your balance after fees is ${after_change}.") #shows updated balance

            balance = (open("balance.txt", "w"))
            balance.write(str(after_change)) #write new balance back to balance sheet

            data.append(
                {
                'id' : len(data),
                'type': 'fee',
                'amount': "$25.00",
                'date': datetime.now().strftime("%m/%d/%y"),
                'time': datetime.now().strftime("%H:%M"),
                'description': "overdraft fee"
                }) #add fee to data list

        with open("transactions.txt", "w") as f:
            json.dump(data,f) #dump data list into file
        
    elif user_select == "3":
        while True: #repeats until numeric entry
            change_balance = input("How much would you like to deposit? ")
            if change_balance == "exit":
                exit_program()
            elif change_balance.replace(".","").isdigit():
                break
            else:
                print("This is not a numeric value.")
        change_balance = format(float(change_balance), ".2f") #format change_balance to manipulate
        print(f"Deposit amount: ${change_balance}")
        change_description = input("Description (optional): ")
        if change_description == "exit":
            exit_program()

        after_change = format((float(balance.read()) + float(change_balance)), ".2f")
        print("")
        print(f"Your new balance is ${after_change}.") #shows updated balance

        balance = (open("balance.txt", "w"))
        balance.write(str(after_change)) #write new balance back to balance sheet

        data.append(
            {
            'id' : len(data),            
            'type': 'deposit',
            'amount': "$" + change_balance,
            'date': datetime.now().strftime("%m/%d/%y"),
            'time': datetime.now().strftime("%H:%M"),
            'description': change_description
            }) #add deposit to data list
        
        with open("transactions.txt", "w") as f:
            json.dump(data, f) #dump data list into file
            
    elif user_select == "4":
        print("")
        print("Available transactions:")

        while True: #repeats until valid entry
            print("    a) all transactions")
            print("    b) withdraws")
            print("    c) deposits")
            print("    d) fees")
            print("    e) search by date")
            print("    f) search by key word")
            print("")
            user_select_type = input("Which would you like to view? ")
            if user_select_type == "exit":
                exit_program()
            elif user_select_type in "abcdef": 
                break
            else:
                print("Invalid entry.")
 
        if user_select_type == "a":
            print("")
            print("Past transactions:")
            available_transaction = 0
            total = 0
            for x in data:
                print(x) #prints all transactions
                available_transaction += 1
                if x["type"] == "deposit": #totals transactions by deposits or withdraws or fees
                    total += float(x["amount"].strip("$"))
                elif x["type"] == "withdraw" or x["type"] == "fee":
                    total -= float(x["amount"].strip("$"))
            if available_transaction > 0: #checks for transactions matching criteria 
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
        elif user_select_type == "b":
            print("")
            print("Past withdraws:")
            available_transaction = 0
            total = 0
            for x in data:
                if x["type"] == "withdraw":
                    print(x) #prints all withdraws
                    available_transaction += 1
                    total += float(x["amount"].strip("$"))
            if available_transaction > 0: #checks for transactions matching criteria 
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
        elif user_select_type == "c":
            print("")
            print("Past deposits:")
            available_transaction = 0
            total = 0 
            for x in data:
                if x["type"] == "deposit":
                    print(x) #prints all deposits
                    available_transaction += 1
                    total += float(x["amount"].strip("$"))
            if available_transaction > 0: #checks for transactions matching criteria 
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
        elif user_select_type == "d":
            print("")
            print("Past fees:")
            available_transaction = 0
            total = 0 
            for x in data:
                if x["type"] == "fee":
                    print(x) #prints all fees
                    available_transaction += 1
                    total += float(x["amount"].strip("$"))
            if available_transaction > 0: #checks for transactions matching criteria 
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")

        elif user_select_type == "e":
            print("")
            while True: #repeats until valid entry
                select_date = input("Enter desired date (mm/dd/yy): ")       
                if select_date == "exit":
                    exit_program()
                elif len(select_date) != 8 or select_date[2] != '/' or select_date[5] != '/' or select_date.isalpha():
                    print("Invalid entry.")
                else:
                    break
            print("")
            print(f"Transactions on {select_date}:")
            available_transaction = 0
            total = 0
            for x in data:
                if x["date"] == select_date:
                    print(x) #prints all transactions on selected date
                    available_transaction += 1
                    total += float(x["amount"].strip("$"))
            if available_transaction > 0: #checks for transactions matching criteria 
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
        elif user_select_type == "f": 
            print("")
            select_key = input("Enter desired keyword: ")
            if select_key == "exit":
                exit_program()

            print("")
            print(f"Transactions with '{select_key}':")
            available_transaction = 0
            total = 0
            for x in data: 
                if x["description"].find(select_key) >= 0:
                    print(x) #prints all transactions with selected keyword
                    available_transaction += 1
                    total += float(x["amount"].strip("$"))
            if available_transaction > 0: #checks for transactions matching criteria 
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
    elif user_select == "5":
        print("")
        print("Note: You are only able to modify DESCRIPTIONS.")
        while True: #repeats until valid entry
            select_id = input("Select id of transaction to modify: ")
            if select_id == "exit":
                exit_program()
            elif select_id.isdigit() == False:
                print("Invalid entry.")
            else:
                break 
        count = 0
        for x in data:
            if x["id"] == int(select_id):
                count += 1
                print("Selected entry:")
                print(x) 
                print("")
                select_description = input("Enter new description: ") #inputs new description
                if select_description == "exit":
                    exit_program()
                select_description = {"description":select_description}
                x.update(select_description) #update description for selected entry
                print("New entry:")
                print(x)
                with open("transactions.txt", "w") as f:
                    json.dump(data, f) #dump data list into file
        if count == 0:
            print("")
            print("There are no records matching selected criteria.")
    else:
        exit_program()