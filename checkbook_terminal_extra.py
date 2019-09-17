import json
from datetime import date
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
    5) exit
    """) #shows user options every time

    while True: #repeats until user enters a valid entry
        user_select = input("What would you like to do today: ")
        if user_select in "12345": #only valid entries
            break
        else:
            print("Invalid entry.")
 
  
    if user_select == "1":
        balance = (open("balance.txt","r")) 
        print(f"Your balance is ${balance.readline()}.")  #reads current balance

    elif user_select == "2":
        balance = (open("balance.txt","r"))
        change_balance = input("How much would you like to withdraw? ")
        change_balance = format(float(change_balance), ".2f")

        after_change = format((float(balance.read()) - float(change_balance)), ".2f")
        print(f"Your balance is ${after_change}.") #shows new balance
    
        balance = (open("balance.txt", "w"))
        balance.write(after_change) #writes new balance to balance sheet

        data.append(
            {
            'type': 'withdraw',
            'amount': "$" + change_balance
            # 'date': date.today()
            }) #add withdraw to transaction sheet
    
    elif user_select == "3":
        balance = (open("balance.txt","r"))
        change_balance = input("How much would you like to deposit? ")
        change_balance = format(float(change_balance), ".2f")

        after_change = format((float(balance.read()) + float(change_balance)), ".2f")
        print(f"Your balance is ${after_change}.") #shows new balance
    
        balance = (open("balance.txt", "w"))
        balance.write(after_change) #writes new balance to balance sheet

        data.append(
            {
            'type': 'deposit',
            'amount': "$" + change_balance
            # 'date': date.today()
            }) #add withdraw to transaction sheet
    elif user_select == "4":
        print("Available transactions:")

        while True:
            print("    a) all transactions")
            print("    b) withdraws")
            print("    c) deposits")
            user_select_type = input("Which would you like to view? ")
            if user_select_type in "abc":
                break
            else:
                print("Invalid entry.")
        if user_select_type == "a":
            print("Past transactions:")
            for x in data:
                print(x) #prints all transactions   
        if user_select_type == "b":
            print("Past withdraws:")
            for x in data:
                print(x["withdraws"]) #prints all transactions   
        if user_select_type == "c":
            print("Past deposits:")
            for x in data:
                print(x["deposits"]) #prints all transactions   

    else: 
        print("Thanks! Have a great day!")
        print("")
        balance.close() 
        break #exits the program

