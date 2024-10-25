import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as npfrom
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("fixtures/Car_sales.csv")
print(f"Print the head of the df: {df.head()}")
# Line separator for cleaner output
print(f"-" * 90)
df.isna().sum()
df.dropna(inplace=True)
print(f"Print the new with dropped values of the df: {df.head()}")
# Line separator for cleaner output
print(f"-" * 90)

# What is the % difference between __year_resale_value and Price_in_thousands?
year_resale_value = df["__year_resale_value"]
price_in_thousands = df["Price_in_thousands"]
percent_diff = (year_resale_value - price_in_thousands) / price_in_thousands * 100
print(
    f"Print the % difference between __year_resale_value and Price_in_thousands: {percent_diff}"
)
# Line separator for cleaner output
print(f"-" * 90)

# On average is BMW more expensive than Ford?

bmw_price = df[df["Manufacturer"] == "BMW"]["Price_in_thousands"].mean()
ford_price = df[df["Manufacturer"] == "Ford"]["Price_in_thousands"].mean()
print(f"Print the average price of BMW: {type(bmw_price)} ${bmw_price}")
print(f"Print the average price of Ford: {type(ford_price)}${ford_price}")
difference_in_price = bmw_price - ford_price
print(f"-" * 90)
print(
    f"Print the difference between the average price of BMW and Ford: {type(difference_in_price)} $ {difference_in_price}"
)

# What make sells more popular based on sales_in_thousands?
most_popular_make = df.groupby("Manufacturer")["Sales_in_thousands"].sum().idxmax()
most_popular_model = df.groupby("Model")["Sales_in_thousands"].sum().idxmax()
print(f"-" * 90)
print(f"Printing the most popular make {type(most_popular_make)}: {most_popular_make}")
print(f"-" * 90)
print(
    f"Printing the most popular model {type(most_popular_model)}: {most_popular_model}"
)
print(f"-" * 90)
print(f"Combined most popular make and model: {most_popular_make} {most_popular_model}")

# Plot the top 5 Manufacturer as a pie chart based on sales_in_thousands
top_5_manufacturers = df.groupby("Manufacturer")["Sales_in_thousands"].sum().nlargest(5)
plt.figure(figsize=(10, 10))
plt.pie(
    top_5_manufacturers,
    labels=top_5_manufacturers.index,
    autopct="%1.1f%%",
    shadow=True,
    explode=[0.1, 0, 0, 0, 0],
)
plt.show()

# loc and iloc is just for slicing the data set
# Get 3 most expensive cars from the data set
most_expensive_cars = df.nlargest(3, "Price_in_thousands")
print(f"-" * 90)
models = most_expensive_cars["Model"]
print(
    f"Printing the 3 most expensive cars: {type(most_expensive_cars)} : {most_expensive_cars}"
)

# Plot the correlation matrix as a heatmap using the seaborn library
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(10, 10))
sns.heatmap(
    correlation_matrix,
    annot=True,
    annot_kws={"size": 10},
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
)
plt.title("Correlation Matrix")
plt.xticks(rotation=45, fontsize=10)
plt.yticks(rotation=45, fontsize=10)
plt.show()

#! Define features and target variable for the Linear Regression model
X = df[["Horsepower"]]
y = df["Price_in_thousands"]

# Split data into training and testing sets 20% testing and 80% training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
model_score = model.score(X_test, y_test)
y_pred = model.predict(X_test)

# Print the model score and prediction for the output
print("-" * 90)
print(f"Printing the prediction: {type(y_pred)} y_pred : {y_pred} : {type(model_score)} model score : {model_score}")

# Plot the actual price vs predicted price
plt.figure(figsize=(10, 10))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Price")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # regression line
plt.show()

mode_that_depreciates_the_most = df.groupby("Manufacturer")["__year_resale_value"].mean().idxmin()
print(f"-" * 90)
print(f"Printing the manufacturer that depreciates the most: {type(mode_that_depreciates_the_most)} : {mode_that_depreciates_the_most}")

