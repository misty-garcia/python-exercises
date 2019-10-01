from pydataset import data
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from env import host, user, password

# 1. Use the iris database to answer the following quesitons:
iris = data("iris")
iris.head()

# 2. What does the distribution of petal lengths look like?
sns.distplot(iris["Petal.Length"])

# 3. Is there a correlation between petal length and petal width?
iris.corr()
iris["Petal.Length"].corr(iris["Petal.Width"])
r = iris.corr().loc["Petal.Length","Petal.Width"]

sns.relplot(data=iris, x="Petal.Length",y="Petal.Width")
plt.text(1.5, 2, f"r= {r:.2}")

# 3. Would it be reasonable to predict species based on sepal width and sepal length?
sns.relplot(data=iris, x="Sepal.Width",y="Sepal.Length", hue="Species")

iris['Sepal_lentowid'] = iris['Sepal.Length']/iris['Sepal.Width']
sns.boxplot(data = iris, x = 'Species', y = 'Sepal_lentowid')

print("no.")

# 4. Which features would be best used to predict species?
sns.pairplot(iris,hue="Species")

# 1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
anscombe = sns.load_dataset('anscombe')

df = pd.DataFrame(anscombe)
df.groupby("dataset").describe()
df.head()

# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.
sns.relplot(data=anscombe,x="x",y="y",col="dataset")
print("moral of the dataset: always visual")

# 2. Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows     the effectiveness of the different insect sprays.
insectsprays = sns.load_dataset("InsectSprays")
insectsprays.dtypes

sns.load_dataset
get_dataset_names()

insectsprays = data("InsectSprays")
insectsprays.describe()
insectsprays.info()
insectsprays.head() 

sns.boxplot(data=insectsprays, x="spray",y="count")

# 3. Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:
swiss = data("swiss")
data("swiss", show_doc=True)
swiss.describe()
swiss.info()
swiss.head()

# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)
sns.distplot(swiss.Catholic)
swiss["is.Catholic"] = swiss.Catholic > 49

# Does whether or not a province is Catholic influence fertility?
swiss.corr()
swiss.Fertility.corr(swiss["is.Catholic"])

sns.boxplot(data=swiss, y="Fertility", x="is.Catholic")
sns.relplot(data=swiss, x="Catholic", y="Fertility")

# What measure correlates most strongly with fertility?
swiss.corr().Fertility

# Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.
def get_db_url(username,hostname,password,db_name):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'
    return url

url = get_db_url(user,host,password,"chipotle")
df_chipotle = pd.read_sql('SELECT * FROM orders',url)
df_chipotle.head()

df_chipotle["revenue"]= df_chipotle.item_price.str.replace("$","").astype(float)

df_chipotle.groupby("item_name").sum().sort_values(by="revenue", ascending=False).head()

df_items = df_chipotle.groupby("item_name").sum().sort_values(by="revenue", ascending=False).head(4).revenue

df_items = df_items.reset_index()

sns.barplot(data =df_items, x=df_items.item_name, y=df_items.revenue)
plt.ylabel("")

# 5. Load the sleepstudy data and read it's documentation. Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.
sleepstudy = data("sleepstudy")
sleepstudy.describe()
sleepstudy.info()
sleepstudy.nunique()
sleepstudy.head()

data.find("sleepstudy")
type(data)
data.dataset_id.contains("sleepstudy")

sleepstudy.Subject = "subject" + sleepstudy.Subject.astype(str)

sns.lineplot(data=sleepstudy, x=sleepstudy.Days,y=sleepstudy.Reaction, hue=sleepstudy.Subject)
sns.lineplot(data=sleepstudy, x="Days", y="Reaction")

avg_reaction = sleepstudy.groupby("Days").mean().Reaction
avg_reaction = avg_reaction.reset_index()

sns.lineplot(data=sleepstudy, x=sleepstudy.Days,y=sleepstudy.Reaction, hue=sleepstudy.Subject)
sns.lineplot(data=avg_reaction, x=avg_reaction.Days, y=avg_reaction.Reaction, color='red')
sns.lineplot(data=avg_reaction, x=avg_reaction.Days, y=avg_reaction.Reaction, color='red', linewidth=8, alpha=.3)

plt.title("Individual's Reactions Time")

# sns.lineplot(data=sleepstudy, x=sleepstudy.Days, y=sleepstudy.groupby("Days").mean(), color='red')
# sns.lineplot(data=sleepstudy, x=sleepstudy.Days, y=sleepstudy.groupby("Days").mean().Reaction, color='red', linewidth=8, alpha=.3)


