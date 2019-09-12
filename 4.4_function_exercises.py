# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    return x == 2 or x == "2"

is_two(2)
is_two(3)
is_two("2")
is_two("hello")

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    return x.lower() == "a" or x.lower() == "e" or x.lower() == "o" or x.lower() == "u" or x.lower() == "i"

is_vowel("o")
is_vowel("i")
is_vowel("ab")
is_vowel("A")

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    return not is_vowel(x)

is_consonant("e")
is_consonant("I")
is_consonant("t")
is_consonant("V")

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capital_word(word):
    return word.capitalize()

capital_word("hello")

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percent,bill):
    return tip_percent * bill + bill

calculate_tip(.15,20)

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(price, discount_percent):
    return round(price * (1 - discount_percent),2)

apply_discount(20, .2)
apply_discount(21, .31)

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(*args):
    x = ""
    for arg in args:
        print(str(arg))
        x = x + str(arg)
        print(x)
    return int(x)

handle_commas(23,255)
handle_commas(1,000,000)
handle_commas(89,123,567,867,234)

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num):
    if num >= 90:
        return "A"
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    elif num >= 60:
        return "D"
    else:
        return "F"

get_letter_grade(90)
get_letter_grade(55)
get_letter_grade(87)

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    for x in string:
        if is_vowel(x):
            new_string = string.replace(x,"")
    return new_string

def remove_vowels(string):
    new_list = list(string)
    print(new_list)
    for x in new_list:
        if is_vowel(x):
            new_list.remove(x)
    return new_list.join()

remove_vowels("hello")


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# B1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# B2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27