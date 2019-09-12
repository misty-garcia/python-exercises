## Conditional Basics

# 1a . prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input("What is the day of the week? (spell out whole day) ")
if day_of_week.lower() == "monday":
    print("Today is Monday.")
else:
    print("Today is not Monday. It's", day_of_week.capitalize())

# 1b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

if day_of_week.lower() == "monday" or day_of_week.lower() == "tuesday" or day_of_week.lower() == "wednesday" or day_of_week.lower() == "thursday" or day_of_week.lower() == "friday":
    print("It's a weekday.")
elif day_of_week.lower() == "saturday" or day_of_week.lower() == "sundday":
    print("It's the weekend!")
else:
    print("You did not enter an acceptable day.")

# 1c. create variables and make up values for
#         the number of hours worked in one week
#         the hourly rate
#         how much the week's paycheck will be
#     write the python code that calculates the weekly paycheck. You       get paid time and a half if you work more than 40 hours
hours_worked_in_week = 41
hourly_rate = 20

if hours_worked_in_week <= 40:
    week_paycheck = hours_worked_in_week * hourly_rate
    print('the weekly paycheck is', week_paycheck)
else:
    ot_hours = hours_worked_in_week - 40
    week_paycheck = ot_hours * hourly_rate * 1.5 + 40 * hourly_rate
    print('the weekly paycheck is', week_paycheck)

# 2a. While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# 2a. Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <=100:
    print(i)
    i += 2

# 2a. Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i > -10:
    print(i)
    i -= 5

# 2a. Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 
i = 2
while i < 1_000_000:
    print(i)
    i = i ** 2

# 2a. Write a loop that uses print to create the output shown below.
i = 100
while i > 0:
    print(i)
    i -= 5

# 2bi. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
user_number = int(input("Enter a number: "))

for x in range(10):
    print(user_number, "x", x + 1, "=", user_number * (x + 1)) 

# 2bii. Create a for loop that uses print to create the output shown below.
for x in range(1,10):
    for y in range(1,10):
        if x == y:
            print(x * str(y))

# 2ci. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# user_number = int(input("Enter a number: "))

while True:
    user_odd_number = input("Enter an odd number less than 50: ")
    if str(user_odd_number).isdigit() and int(user_odd_number) % 2 == 1 and int(user_odd_number) < 50:
        print("Number to skip:", user_odd_number)
        print()
        break
    else:
        print("Invalid input.")

user_odd_number = int(user_odd_number)
for x in range(1,50,2):
    if user_odd_number == x:
        print("Yikes! Skipping number:", user_odd_number)
        continue
    print("Here is an odd number:", x)

# 2d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
while True:
    user_positive_number = input("Enter a positive number: ")
    if str(user_positive_number).isdigit() and int(user_positive_number) > 0:
        for x in range(int(user_positive_number)+1):
            print(x)
        break
    else:
        print("Invalid input.")
# 2e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
while True:
    user_positive_number = input("Enter a positive number: ")
    if str(user_positive_number).isdigit() and int(user_positive_number) > 0:
        for x in range(int(user_positive_number),0,-1):
            print(x)
        break
    else:
        print("Invaild input.")

# 3. Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
        continue
    print(x)

# 4. Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

while True:
    user_integer = int(input("What number would you like to go up to? "))
    print("Here is your table!")
    print()
    for x in range(user_integer+1):
        print(x, x ** 2, x ** 3)
    again = input("Would you like to continue ('no' to exit)?")
    if again.lower() == "no":
        break

# 5. Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus: Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

while True:
    user_grade = int(input('Enter a numerical grade from 0 to 100: '))
    if user_grade >= 97:
        print("The letter grade: A+")
    elif user_grade >=93:
        print("The letter grade: A") 
    elif user_grade >=88:
        print("The letter grade: A-") 
    elif user_grade >=85:
        print("The letter grade: B+") 
    elif user_grade >=83:
        print("The letter grade: B") 
    elif user_grade >=80:
        print("The letter grade: B-") 
    elif user_grade >=77:
        print("The letter grade: C+") 
    elif user_grade >=73:
        print("The letter grade: C")
    elif user_grade >=67:
        print("The letter grade: C-") 
    elif user_grade >= 60:
        print("The letter grade: D")
    else:
        print("The letter grade: F")
    again = input("Would you like to continue ('no' to exit)?")
    if again.lower() == "no":
        break

# 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

books = [
    {"title":"1984", "author":"Emily Bronte", "genre":"Literature" }
]
print(books)