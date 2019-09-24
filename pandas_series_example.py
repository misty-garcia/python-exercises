# Given the pets series, output the number of vowels in each pet species

import pandas as pd
pets = pd.Series([
    "cat",
    "dog",
    "lizard",
    "rock",
    "dragon"
])

# Count the vowels of a given word
def count_vowels(word):
    word = word.lower()
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")

# gives us a series containing the number of vowels of each pet type.
vowel_counts = pets.apply(count_vowels)

# So we have our series of pets and we have our series containing vowel counts....
# It's almost as if we need to put together two series....

# How do we put them together?
# One way:
for i, pet in enumerate(pets):
    print(pet, "has", vowel_counts[i], "vowels")


# Another way:
list(zip(pets, vowel_counts))

# And a third way:
df = pd.DataFrame(list(zip(pets, vowel_counts)))
df.columns = ["pet", "vowel count"]
print(df)