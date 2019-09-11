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

for x  in range(10):
    print(user_number, "x", x + 1, "=", user_number * (x + 1)) 

# 2bii. Create a for loop that uses print to create the output shown below.
for x in range(1,10):
    for y in range(1,10):
        if x == y:
            print(x * str(y))

# 3ci. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
user_number = int(input("Enter a number: "))

user_odd_number = 5

count = 1
while count < 50:
    print