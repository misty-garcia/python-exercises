import json
from datetime import datetime
import time
import os.path
# import checkbook_functions as cf
data = []

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
    6) exit
    """) #shows user options every time

    while True: #repeats until user enters a valid entry
        time.sleep(.5)
        user_select = input("What would you like to do today? ")
        if user_select in "123456": #only valid entries
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
            data = json.load(f) #if data list doesnt exist yet, create it and open it

    if os.path.exists("balance.txt"):
        balance = (open("balance.txt","r")) #open balance sheet
    else: 
        f= open("balance.txt","w+")
        f.write("0")
        f.close() 
        balance = (open("balance.txt","r"))
 
    if user_select == "1":
        print(f"Your balance is ${balance.read()}.") 

    elif user_select == "2":
        while True: #repeats until numeric entry
            change_balance = input("How much would you like to withdraw? ")
            if change_balance.replace(".","").isdigit():
                break
            else:
                print("This is not a numeric value.")
        change_balance = format(float(change_balance), ".2f")
        print(f"Withdraw amount: ${change_balance}")
        change_description = input("Description (optional): ")

        after_change = format((float(balance.read()) - float(change_balance)), ".2f")
        print("")
        print(f"Your new balance is ${after_change}.") #shows new balance
        if float(after_change) < 0:
            print("***Warning: Negative balance. Will incur overdraft fees.***")

        balance = (open("balance.txt", "w"))
        balance.write(str(after_change)) #write new balance back to balance sheet

        data.append(
            {
            'type': 'withdraw',
            'amount': "$" + change_balance,
            'date': datetime.now().strftime("%m/%d/%y"),
            'time': datetime.now().strftime("%H:%M"),
            'description': change_description
            }) #add withdraw to data list
        
        with open("transactions.txt", "w") as f:
            json.dump(data,f) #dump data list into file
        
    elif user_select == "3":
        while True: #repeats enter numeric entry
            change_balance = input("How much would you like to deposit? ")
            if change_balance.replace(".","").isdigit():
                break
            else:
                print("This is not a numeric value.")
        change_balance = format(float(change_balance), ".2f")
        print(f"Deposit amount: ${change_balance}")
        change_description = input("Description (optional): ")

        after_change = format((float(balance.read()) + float(change_balance)), ".2f")
        print("")
        print(f"Your new balance is ${after_change}.") #shows new balance

        balance = (open("balance.txt", "w"))
        balance.write(str(after_change)) #write new balance back to balance sheet

        data.append(
            {
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

        while True:
            print("    a) all transactions")
            print("    b) withdraws")
            print("    c) deposits")
            print("    d) search by date")
            print("    e) search by key word")
            print("")
            user_select_type = input("Which would you like to view? ")
            if user_select_type in "abcde": #verifies valid selection
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
                total += float(x["amount"].strip("$"))
            if available_transaction > 0:
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
            if available_transaction > 0:
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
            if available_transaction > 0:
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
        elif user_select_type == "d":
            print("")
            while True:
                select_date = input("Enter desired date (mm/dd/yy): ")
                if select_date[2] != '/':
                    print("Invalid entry.")
                    continue
                elif select_date[5] != '/':
                    print("Invalid entry.")
                else:
                    break
            print("")
            print(f"Transactions on {select_date}:")
            available_transaction = 0
            total = 0
            for x in data:
                if x["date"] == select_date:
                    print(x)
                    available_transaction += 1
                    total += float(x["amount"].strip("$"))
            if available_transaction > 0:
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
        elif user_select_type == "e": 
            print("")
            select_key = input("Enter desired keyword: ")
            print("")
            print(f"Transactions with '{select_key}':")
            available_transaction = 0
            total = 0
            for x in data:
                if x["description"].find(select_key) >= 0:
                    print(x)
                    available_transaction += 1
                    total += float(x["amount"].strip("$"))
            if available_transaction > 0:
                print(f"Records returned: {available_transaction}")
                total = format(total,".2f") 
                print(f"Total: ${total}")
                average = format(float(total) / int(available_transaction),".2f")
                print(f"Average: ${average}")
            else:
                print("There are no records matching selected criteria.")
    elif user_select == "5":
        print("")
        print("You are only able to modify descriptions of past transactions.")
        while True:
            select_date = input("Enter desired date (mm/dd/yy): ")
            if select_date[2] != '/':
                print("Invalid entry.")
                continue
            elif select_date[5] != '/':
                print("Invalid entry.")
            else:
                break    
        count = 0
        print("")
        print(f"Transactions on {select_date}:")        
        for x in data:
            if x["date"] == select_date:
                print(x)
                count += 1
        if count == 0:
            print("There are no records matching selected critera")
        else:
            print("")
            while True:
                select_amount = input("Select transaction amount: ")
                if select_amount.replace(".","").strip("$").isdigit():
                    break
                else:
                    print("This is not a numeric value.")
            select_amount = '$' + format(float(select_amount.strip("$")), ".2f")
            count = 0
            for x in data:
                if x["date"] == select_date and x["amount"] == select_amount:
                    count += 1
            if count > 1:
                select_time = input("Select time of transaction (hh:mm): ")
                count = 0 
                for x in data:
                    if x["date"] == select_date and x["amount"] == select_amount and x["time"] == select_time:
                        count += 1
                        print("Selected entry:")
                        print(x)
                        print("")
                        select_description = input("Enter new description: ")
                        select_description = {"description":select_description}
                        x.update(select_description)
                        print("New entry:")
                        print(x)
                        with open("transactions.txt", "w") as f:
                            json.dump(data, f) #dump data list into file
                if count == 0:
                    print("There are no records matching selected criteria.")
            elif count == 1:
                print("")
                for x in data:
                    if x["date"] == select_date and x["amount"] == select_amount:
                        print("Selected entry:")
                        print(x)
                        print("")
                        select_description = input("Enter new description: ")
                        select_description = {"description":select_description}
                        x.update(select_description)
                        print("New entry:")
                        print(x)
                        with open("transactions.txt", "w") as f:
                            json.dump(data, f) #dump data list into file
            else:
                print("")
                print("There are no records matching selected criteria.")
    else:
        print("")
        print("Thanks! Have a great day!") 
        print("")  
        break #exits the program