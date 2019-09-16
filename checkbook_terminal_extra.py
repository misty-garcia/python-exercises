print("")
print("~~ Welcome to your checkbook~~")

while True:
    print("""
These are your options via the terminal: 
    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit
    5) view transactions
    """)

    while True:
        user_select = input("What would you like to do today: ")
        if user_select in "12345":
            break
        else:
            print("Invalid entry.")

    balance = (open("balance.txt","r"))

    if user_select == "1":
        print(f"Your balance is ${balance.readline()}.")  

    elif user_select == "2":
        change_balance = int(input("How much would you like to withdraw? "))

        after_change = int(balance.read()) - change_balance
        print(f"Your balance is ${after_change}.")
    
        balance = (open("balance.txt", "a"))
        balance.write("\n + str(after_change)") 
    
    elif user_select == "3":
        change_balance = int(input("How much would you like to deposit? "))

        after_change = int(balance.read()) + change_balance
        print(f"Your balance is ${after_change}.")
    
        balance = (open("balance.txt", "w"))
        balance.write(str(after_change)) 

    elif user_select == "4": 
        print("Thanks! Have a great day!")
        print("")
        balance.close()
        break
    else: 
        print("You have chosen to see all transactions")
    
        mylines = []                             # Declare an empty list named mylines.
        with open ('balance.txt', 'rt') as myfile: # Open lorem.txt for reading text data.
            for myline in myfile:                # For each line, stored as myline,
                mylines.append(myline)           # add its contents to mylines.
        print(mylines) 

print(mylines[1])


