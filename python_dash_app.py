import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
#! dash library for Data Vis and Web applications
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html  
#! dcc is for Dash Core Components, html for HTML Components

df = pd.read_csv("./fixtures/chipotle.csv")

# check to see if the Data Frame has been successfully created (head is a method that shows the first 5 rows of the df)
print(f"print the df head: {df.head}")
print("-" * 50)  # line seperate for cleaner output

