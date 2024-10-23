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