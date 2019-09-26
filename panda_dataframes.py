from pydataset import data

# All the datasets loaded from the pydataset library will be pandas dataframes.

# 1. Copy the code from the lesson to create a dataframe full of student grades.

import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

# Create a column named passing_english that indicates whether each student has a passing grade in reading.
df["passing_english"]=df.english>70

# Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by="passing_english")

# Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=["passing_english","name"])

# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by=["passing_english","english"])

# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades. 
df["overall_grade"] = df.math + df.english + df.reading

# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
data('mpg', show_doc=True)

# How many rows and columns are there?
mpg.shape

# What are the data types of each column?
mpg.dtypes

# Summarize the dataframe with .info and .describe
mpg.info()
mpg.describe()

# Rename the cty column to city.
mpg.rename(columns={"cty":"city"},inplace=True)

# Rename the hwy column to highway.
mpg.rename(columns={"hwy":"highway"},inplace=True)

# Do any cars have better city mileage than highway mileage?
mpg [mpg.city > mpg.highway]

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg ["mileage_difference"] = mpg.highway - mpg.city

# Which car (or cars) has the highest mileage difference
mpg [mpg.mileage_difference == mpg.mileage_difference.max()]

# Which compact class car has the lowest highway mileage? The best?
mpg.rename(columns={"class":"type"},inplace=True)

mpg_compact = mpg [mpg.type=="compact"]    
mpg_compact [mpg_compact.highway == mpg_compact.highway.min()]
  
# Create a column named average_mileage that is the mean of the city and highway mileage.
mpg["average_mileage"]= (mpg.city + mpg.highway) / 2

# Which dodge car has the best average mileage? The worst?
mpg.info()

mpg_dodge = mpg [mpg.manufacturer == "dodge"]
mpg_dodge [mpg_dodge.average_mileage == mpg_dodge.average_mileage.max()]
mpg_dodge [mpg_dodge.average_mileage == mpg_dodge.average_mileage.min()]

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data("Mammals")
mammals.info()

# How many rows and columns are there?
mammals.shape

# What are the data types?
mammals.dtypes

# Summarize the dataframe with .info and .describe
mammals.info()
mammals.describe()

# What is the the weight of the fastest animal?
mammals.sort_values(by="speed",ascending=False).head()
mammals.sort_values(by="speed",ascending=False).head(1).weight
list(zip(mammals,mammals.sort_values(by="speed",ascending=False).head(1).weight))

list(zip(mammals, mammals [mammals.speed == mammals.speed.max()].weight))

# What is the overal percentage of specials?
special_mammals = len(mammals [mammals.specials==True]) / len(mammals) * 100
print(f'the percentage of specials is {round(float(special_mammals),2)}%')

# How many animals are hoppers that are above the median speed? What percentage is this?
len (mammals [(mammals.speed > mammals.speed.median()) & mammals.hoppers==True])

fast_hoppers = (len (mammals [(mammals.speed > mammals.speed.median()) & mammals.hoppers==True])) / len(mammals) * 100
print(f'the percentage of faster than average hoppers is {round(float(fast_hoppers),2)}%')