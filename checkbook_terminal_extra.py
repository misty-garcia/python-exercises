import json
from datetime import datetime
data = []

print("")
print("~~ Welcome to your checkbook~~") #prints opening statement, does not repeat

with open("transactions.txt") as f:
    data = json.load(f) #open latest data list as a string for transactions

while True: #repeats until the user exits
    print("""
These are your options via the terminal:
    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) view transactions
    5) exit
    """) #shows user options every time

    while True: #repeats until user enters a valid entry
        user_select = input("What would you like to do today? ")
        if user_select in "12345": #only valid entries
            break
        else:
            print("Invalid entry.")
 
  
    if user_select == "1":
        balance = (open("balance.txt","r")) 
        print("")
        print(f"Your balance is ${balance.readline()}.")  #reads current balance

    elif user_select == "2":
        balance = (open("balance.txt","r"))
        change_balance = input("How much would you like to withdraw? ")
        change_balance = format(float(change_balance), ".2f")
        change_description = input("Enter a description (optional): ")
        # if change_description = nulltype

        after_change = format((float(balance.read()) - float(change_balance)), ".2f")
        print(f"Your balance is ${after_change}.") #shows new balance
    
        balance = (open("balance.txt", "w"))
        balance.write(after_change) #writes new balance to balance sheet

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
        balance = (open("balance.txt","r"))
        change_balance = input("How much would you like to deposit? ")
        change_balance = format(float(change_balance), ".2f")
        change_description = input("Enter a description (optional): ")

        after_change = format((float(balance.read()) + float(change_balance)), ".2f")
        print(f"Your balance is ${after_change}.") #shows new balance
    
        balance = (open("balance.txt", "w"))
        balance.write(after_change) #writes new balance to balance sheet

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
        print("Available transactions:")
        with open("transactions.txt") as f:
            data = json.load(f) #load current transactions

        while True:
            print("    a) all transactions")
            print("    b) withdraws")
            print("    c) deposits")
            user_select_type = input("Which would you like to view? ")
            if user_select_type in "abc": #verifies valid selection
                break
            else:
                print("Invalid entry.")
        if user_select_type == "a":
            print("")
            print("Past transactions:")
            for x in data:
                print(x) #prints all transactions   
        elif user_select_type == "b":
            print("")
            print("Past withdraws:")
            for x in data:
                if x["type"] == "withdraw":
                    print(x) #prints all withdraws   
        elif user_select_type == "c":
            print("")
            print("Past deposits:")
            for x in data:
                if x["type"] == "deposit":
                    print(x) #prints all deposits 
    else: 
        print("")
        print("Thanks! Have a great day!")
        print("")
        balance.close() 
        break #exits the program

