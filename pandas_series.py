# Pandas
import pandas as pd 

# Use pandas to create a Series from the following data:
# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
#1a. Name the variable that holds the series fruits.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
fruits

# Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()

# Run the code necessary to produce only the unique fruit names.
fruits.unique()

# Determine how many times each value occurs in the series.
frequencies = fruits.value_counts()

# Determine the most frequently occurring fruit name from the series.
fruits.value_counts() [fruits.value_counts() == fruits.value_counts().max()]

frequencies.idxmax(),frequencies.max()

# Determine the least frequently occurring fruit name from the series.
fruits.value_counts() [fruits.value_counts() == fruits.value_counts().min()]

# Write the code to get the longest string from the fruits series.
fruits [fruits.str.len() == fruits.str.len().max()]

fruits[fruits.str.len().idxmax()],fruits.str.len().max()

# Find the fruit(s) with 5 or more letters in the name.
fruits [fruits.str.len() >= 5]

# Capitalize all the fruit strings in the series.
fruits.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization)
fruits.str.count("a")

fruit_names = fruits.unique()
list(zip(fruit_names,fruit_names.str.count("a")))

# Output the number of vowels in each and every fruit.
def count_vowels(word):
    count = 0
    for x in word:
        if x.lower() in "aeiou":
            count += 1
    return count

fruits.apply(count_vowels)

list(zip(fruits, fruits.apply(count_vowels)))

# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
fruits [fruits.apply( lambda x: x.count("o") > 1)]

# Write the code to get only the fruits containing "berry" in the name
def find_berry(word):
    return word.find("berry") != -1

fruits [fruits.apply(find_berry)]

fruits [fruits.apply( lambda x: x.find("berry") != - 1)]

# Write the code to get only the fruits containing "apple" in the name
fruits [fruits.apply( lambda x: x.find("apple") != - 1)]

# Which fruit has the highest amount of vowels?
fruits [fruits.apply(count_vowels) == fruits.apply(count_vowels).max()]

# 2. Use pandas to create a Series from the following data:
# ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

money = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# What is the data type of the series?
type(money)
money.describe()
money

# Use series operations to convert the series to a numeric data type.
moneys = money.str.replace(",","").str.slice(1).astype("float64")

# What is the maximum value? The minimum?
moneys.max()
moneys.min()

# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
moneys
pd.cut(moneys,4).value_counts()

# Plot a histogram of the data. Be sure to include a title and axis labels.
%matplotlib inline
import matplotlib.pyplot as plt

moneys.plot.hist(color="blue")
plt.title("Moneys")
plt.xlabel("Amount in millions")

pd.cut(moneys,4).value_counts().plot.hist(color="blue")
plt.title("Money equally distributed in four bins")
plt.xlabel("Amount in millions")

# 3. Use pandas to create a Series from the following exam scores:
# [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# What is the minimum exam score? The max, mean, median?
scores.min()
scores.max()
scores.mean()
scores.median()

# Plot a histogram of the scores.
scores.plot.hist(color="blue")

# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.


# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
scores + (100 - scores.max())

# Use pandas to create a Series from the following string:
# 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
longstring = pd.Series('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')

longlist = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

# What is the most frequently occuring letter? Least frequently occuring?
longlist.value_counts()

longlist.value_counts() [longlist.value_counts() == longlist.value_counts().max()]

longlist.value_counts() [longlist.value_counts() == longlist.value_counts().min()]

# How many vowels are in the list?
sum(longlist.apply(count_vowels))

# How many consonants are in the list?
longlist.count() - sum(longlist.apply(count_vowels))

# Create a series that has all of the same letters, but uppercased
longstring.str.upper()

# Create a bar plot of the frequencies of the 6 most frequently occuring letters.
longlist.value_counts().head(6).plot.bar()
plt.title("Six Most Popular Letters in Longstring")
plt.xlabel("letters")
plt.ylabel("frequency")
