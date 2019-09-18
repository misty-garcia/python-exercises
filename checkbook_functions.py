def check_date_syntax(date):
    # for x in date.strip("/"):
    #     if x.isdigit() == False:
    #         print("Invalid entry.")
    #         return False
    if date[2] != '/':
        print("Invalid entry.")
        return False
    elif date[5] != '/':
        print("Invalid entry.")
        return False 
    else:
        return True