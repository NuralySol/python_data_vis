import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
#! dash library for Data Vis and Web applications
import dash
from dash import dcc, html  #! dcc is for Dash Core Components, html for HTML Components

df = pd.read_csv("./fixtures/chipotle.csv")

# check to see if the Data Frame has been successfully created.
print(f"print the df head: {df.head}")

print("-" * 50)  # line seperate for cleaner output
# Renaming the 'item_price' column to 'order_price'
df.rename(columns={"item_price": "order_price"}, inplace=True)

# Dropping the 'order_id' column with in inplace=True to make sure that the df is saved and modified.
df.drop(columns=["order_id"], inplace=True)

# Convert 'order_price' to float after removing the dollar sign for cleaner output and be able to math on it.
df["order_price"] = df["order_price"].replace("[\$,]", "", regex=True).astype(float)

most_expensive_order = df["order_price"].max()
# Output of the most expenseive order is and is formatted again to dollar sign just for this output.
print(f"The most expensive order is: ${most_expensive_order:.2f}")
print("-" * 50)
print(f"new head of the df:{df.head}")
# How many times people ordered a Chicken Bowl
print("-" * 50)
chicken_bowl_orders = df[df["item_name"].str.contains("Chicken Bowl", case=False)]
chicken_bowl_count = chicken_bowl_orders["quantity"].sum()
# Print the output of the Chicken Bowl orders
print(f"People ordered Chicken Bowl {chicken_bowl_count} times.")

# What is the total revenue of the "Chicken Bowl"
chicken_bowl_total_revenue = chicken_bowl_orders["order_price"].sum()
print(f"Total Chicken Bowl revenue: ${chicken_bowl_total_revenue:.2f}")

#! Pandas have 2 Data Types (Series) which are 1-Dimensional and (Data Frame) which are 2-Dimensional
#! Not to be confused with NumPy arrays
# How many times people ordered more than one Chicken Bowl
print("-" * 50)
more_than_one_chicken_bowl_orders = chicken_bowl_orders[
    chicken_bowl_orders["quantity"] > 1
]
more_than_one_chicken_bowl_count = more_than_one_chicken_bowl_orders.shape[0]
print(
    f"People ordered more than one Chicken Bowl {type(more_than_one_chicken_bowl_count)} times."
)

# Plot as a pie-chart top five item_name by revenue (we want see to our bestsellers)
#! From now on always pass in always type of every output to see what data type it is.
top_five_items_bestsellers = df.groupby("item_name")["order_price"].sum().nlargest(5)
plt.pie(
    top_five_items_bestsellers,
    labels=top_five_items_bestsellers.index,
    explode=[0.1, 0, 0, 0, 0],
    shadow=True,
    autopct="%1.1f%%",
)
plt.title(
    "Top Five Item Sellers",
    color="black",
    fontsize=14,
)
plt.show()
print("-" * 50)
print(
    f"Top five items bestsellers are {type(top_five_items_bestsellers)}"
)  # Panda.Series not falling for that again.

