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

# How many different ways can you combine two of the letters from "abcd"?
len(list(it.permutations('abcd',2)))

# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

import json

with open('profiles.json', 'r') as f:
    new_dict = json.load(f)

# load profiles.json

# Total number of users
len(new_dict)

# Number of active users
active_list = []
for x in new_dict:
    if x["isActive"]:
        active_list.append(x["name"])
        print(active_list)
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
balance_list = []
for x in new_dict:
    balance_list.append(x["balance"])
min(balance_list)

# User with the highest balance
balance_list = []
for x in new_dict:
    balance_list.append(x["balance"])
max(balance_list)

# Most common favorite fruit
fruit_list = []
for x in new_dict:
    fruit_list.append(x["favoriteFruit"])
max(fruit_list)

# Least most common favorite fruit
fruit_list = []
for x in new_dict:
    fruit_list.append(x["favoriteFruit"])
min(fruit_list)

# Total number of unread messages for all users
total = 0
for x in new_dict:
    num_index_begin = x["greeting"].find("have")
    num_index_end = x["greeting"].find("unread")
    num = int(x["greeting"][num_index_begin + 5:num_index_end])
    total += num
print(total)