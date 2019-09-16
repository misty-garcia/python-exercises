print("")
print("~~ Welcome to your checkbook~~")

while True:
    print("""
These are your options via the terminal: 
    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit
    """)

    while True:
        user_select = input("What would you like to do today: ")
        if user_select in "1234":
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
    
        balance = (open("balance.txt", "w"))
        balance.write(str(after_change)) 
    
    elif user_select == "3":
        change_balance = int(input("How much would you like to deposit? "))

        after_change = int(balance.read()) + change_balance
        print(f"Your balance is ${after_change}.")
    
        balance = (open("balance.txt", "w"))
        balance.write(str(after_change)) 

    else: 
        print("Thanks! Have a great day!")
        print("")
        balance.close()
        break


