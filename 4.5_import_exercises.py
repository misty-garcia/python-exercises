# Import and test 3 of the functions from your functions exercise file.
import function_exercises

function_exercises.multiply(3,4)

from function_exercises import add

add(5,2)

from function_exercises import is_two as is2

is2(4)
is2("2")

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools as it

len(list(it.permutations('abcd123')))
list(it.combinations("abcd","123"))

# How many different ways can you combine two of the letters from "abcd"?
len(list(it.permutations('abcd',2)))
list(it.combinations('abcd',2))
len(list(it.combinations('abcd',2)))


# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json

with open('profiles.json', 'r') as f:
    new_dict = json.load(f)

profiles = new_dict

# Total number of users
len(new_dict)

# Number of active users
active_list = []
for x in new_dict:
    if x["isActive"]:
        active_list.append(x["name"])
len(active_list)

# Number of inactive users
inactive_list = []
for x in new_dict:
    if x["isActive"] == False:
        inactive_list.append(x["name"])
len(inactive_list)

# Grand total of balances for all users
import function_exercises

total = 0
for x in new_dict:
    new_int = handle_commas(x["balance"].strip("$"))
    total += new_int
round(total,2)

# Average balance per user
round(total / len(new_dict),2)

# User with the lowest balance
def handle_balance(s):
    return float(s[1:].replace(',', ''))

user_with_the_lowest_balance = new_dict[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) < handle_balance(user_with_the_lowest_balance['balance']):
        user_with_the_lowest_balance = user
user_with_the_lowest_balance["name"]
user_with_the_lowest_balance["balance"]

min(profiles, key=lambda profile: handle_balance(profile["balance"]))

# User with the highest balance
user_with_the_highest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) > handle_balance(user_with_the_highest_balance['balance']):
        user_with_the_highest_balance = user
user_with_the_highest_balance["name"]
user_with_the_highest_balance["balance"]

max(profiles, key=lambda profile: handle_balance(profile["balance"]))

# Most common favorite fruit
from collections import Counter
max(Counter([p['favoriteFruit'] for p in profiles]))

fruit_count = {}
for profile in profiles:
    fruit = profile['favoriteFruit']
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
fruit_count

# Least most common favorite fruit
min(Counter([p['favoriteFruit'] for p in profiles]))

# Total number of unread messages for all users
total = 0
for x in new_dict:
    num_index_begin = x["greeting"].find("have")
    num_index_end = x["greeting"].find("unread")
    num = int(x["greeting"][num_index_begin + 5:num_index_end])
    total += num
total

def extract_digits(s):
    return int("".join([c for c in s if c.isdigit()]))

greetings = [profile['greeting'] for profile in profiles]
sum([extract_digits(greeting) for greeting in greetings])

